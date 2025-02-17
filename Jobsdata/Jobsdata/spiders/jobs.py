import scrapy
from pymongo import MongoClient
from datetime import datetime, timezone, timedelta

client = MongoClient("mongodb://localhost:27017/")
db = client.Jobsdata

def insertToDb(title, job_detail, company, location, duration, stipend, posted_on, offer):
    collection = db["internships"]
    job_id = f"{title}-{company}".lower().replace(" ", "-")  # Unique ID

    data = {
        "_id": job_id,
        "job_detail": job_detail,
        "title": title,
        "company": company,
        "location": location,
        "duration": duration,
        "stipend": stipend,
        "posted_on": posted_on,
        "offer": offer,
        "date": datetime.now(timezone.utc)
    }
    result = collection.update_one({"_id": job_id}, {"$set": data}, upsert=True)
    return result.matched_count == 0  # Returns True if a new job was inserted

def delete_old_jobs(days=30):
    collection = db["internships"]
    cutoff_date = datetime.now(timezone.utc) - timedelta(days=days)
    result = collection.delete_many({"date": {"$lt": cutoff_date}})
    print(f"Deleted {result.deleted_count} old job listings.")

class JobsSpider(scrapy.Spider):
    name = "jobs"
    allowed_domains = ["internshala.com"]
    start_urls = ["https://internshala.com/internships/page-1"]

    max_consecutive_empty_pages = 5  # Stop after 5 empty pages *only if* total pages also exceed limit
    max_total_pages = 100  # Absolute max pages to prevent infinite crawling

    def start_requests(self):
        yield scrapy.Request(
            url="https://internshala.com/internships/",
            callback=self.parse,
            meta={"valid_pages": 0, "empty_pages": 0, "total_pages": 1}  # Initialize counters
        )

    def parse(self, response):
        delete_old_jobs(30)

        page_number = int(response.url.split("page-")[-1].replace("/", "")) if "page-" in response.url else 1
        total_pages = response.meta["total_pages"]  # Total pages scraped so far
        valid_pages = response.meta["valid_pages"]  # Pages with new jobs
        empty_pages = response.meta["empty_pages"]  # Consecutive empty pages

        cards = response.css("div.internship_meta")
        new_job_count = 0

        for card in cards:
            title = card.css(".job-title-href::text").get(default="N/A").strip()
            job_detail = card.css(".job-title-href::attr(href)").get(default="N/A").strip()
            company = card.css(".company-name::text").get(default="N/A").strip()
            location = card.css(".locations a::text").get(default="N/A").strip()
            duration_texts = card.css(".row-1-item span::text").getall()
            duration = duration_texts[-2].strip() if len(duration_texts) >= 2 else None
            stipend = duration_texts[-1].strip() if len(duration_texts) >= 2 else None
            posted_on = card.css(".detail-row-2 span::text").getall()[0].strip()
            offer_texts = card.css(".detail-row-2 span::text").getall()
            offer = offer_texts[1].strip() if len(offer_texts) > 1 else "N/A"

            if insertToDb(title, job_detail, company, location, duration, stipend, posted_on, offer):
                new_job_count += 1  

        if new_job_count > 0:
            valid_pages += 1
            empty_pages = 0  # Reset empty count since we found jobs
            print(f"✅ Page {page_number}: {new_job_count} new jobs found (Valid Pages: {valid_pages})")
        else:
            empty_pages += 1
            print(f"❌ Page {page_number}: No new jobs (Consecutive Empty Pages: {empty_pages})")

        # Check stop conditions
        if empty_pages >= self.max_consecutive_empty_pages and total_pages >= self.max_total_pages:
            print(f"🛑 Stopping: {empty_pages} empty pages reached and total pages = {total_pages}.")
            return

        # Continue scraping
        next_page = f"https://internshala.com/internships/page-{page_number + 1}/"
        yield response.follow(next_page, callback=self.parse, meta={
            "valid_pages": valid_pages,
            "empty_pages": empty_pages,
            "total_pages": total_pages + 1
        })
