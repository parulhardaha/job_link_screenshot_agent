from playwright.sync_api import sync_playwright

def take_screenshots(urls):
    results = []
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        for i, url in enumerate(urls):
            try:
                page.goto(url, timeout=15000)
                file_name = f"screenshot_{i}.png"
                page.screenshot(path=file_name, full_page=True)

                results.append({
                    "url": url,
                    "status": "success",
                    "file": file_name
                })

            except Exception as e:
                results.append({
                    "url": url,
                    "status": "failed",
                    "error": str(e)
                })

        browser.close()

    return results

# test_urls=[
#     "https://www.linkedin.com/jobs/",
#     "https://www.linkedin.com/jobs/view/0987654321/"

# ]

# output=take_screenshots(test_urls)
# for i in output:
#     print(i)