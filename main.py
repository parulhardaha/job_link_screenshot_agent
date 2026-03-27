import pandas as pd
from screenshot import take_screenshots
from send_email import send_email

df = pd.read_excel("option1_job_links.xlsx")
urls = df["URL"].dropna().tolist()

if __name__ == "__main__":
    results = take_screenshots(urls)
    send_email(results)