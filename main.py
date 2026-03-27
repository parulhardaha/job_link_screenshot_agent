import pandas as pd

df = pd.read_excel("option1_job_links.xlsx")

urls = df["URL"].dropna().tolist()