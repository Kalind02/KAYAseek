def sanitize_text(text):
    return text.strip() if text else "N/A"

def extract_from_css(selector, response, default="N/A"):
    return sanitize_text(response.css(selector).get(default=default))
