import scrapy
from Jobsdata.db.database import insert_to_db, delete_old_jobs  
from Jobsdata.utils.scraper_utils import extract_from_css

class JobsSpider(scrapy.Spider):
    name = "jobs"
    allowed_domains = ["internshala.com"]
    start_urls = ["https://internshala.com/internships/page-1"]

    max_consecutive_empty_pages = 5
    max_total_pages = 100  

    def start_requests(self):
        yield scrapy.Request(
            url="https://internshala.com/internships/",
            callback=self.parse,
            meta={"valid_pages": 0, "empty_pages": 0, "total_pages": 1}
        )

    def parse(self, response):
        delete_old_jobs(30)  # Remove old listings
        page_number = response.meta["total_pages"]
        valid_pages = response.meta["valid_pages"]
        empty_pages = response.meta["empty_pages"]

        cards = response.css("div.internship_meta")
        new_job_count = 0

        for card in cards:
            title = extract_from_css(".job-title-href::text", card)
            job_detail = extract_from_css(".job-title-href::attr(href)", card)
            company = extract_from_css(".company-name::text", card)
            location = extract_from_css(".locations a::text", card)

            duration_texts = card.css(".row-1-item span::text").getall()
            duration = duration_texts[-2] if len(duration_texts) >= 2 else None
            stipend = duration_texts[-1] if len(duration_texts) >= 2 else None

            posted_on = extract_from_css(".detail-row-2 span::text", card)
            offer_texts = card.css(".detail-row-2 span::text").getall()
            offer = offer_texts[1] if len(offer_texts) > 1 else "N/A"

            if insert_to_db(title, job_detail, company, location, duration, stipend, posted_on, offer):
                new_job_count += 1

        if new_job_count > 0:
            valid_pages += 1
            empty_pages = 0
            print(f"✅ Page {page_number}: {new_job_count} new jobs found")
        else:
            empty_pages += 1
            print(f"❌ Page {page_number}: No new jobs found (Empty Pages: {empty_pages})")

        # Stop conditions
        if empty_pages >= self.max_consecutive_empty_pages and page_number >= self.max_total_pages:
            print(f"🛑 Stopping: {empty_pages} empty pages reached and total pages = {page_number}.")
            return

        next_page = f"https://internshala.com/internships/page-{page_number + 1}/"
        yield response.follow(next_page, callback=self.parse, meta={
            "valid_pages": valid_pages,
            "empty_pages": empty_pages,
            "total_pages": page_number + 1
        })
