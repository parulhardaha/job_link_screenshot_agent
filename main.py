import pandas as pd
df = pd.read_excel("option1_job_links.xlsx") #reads  theExcel file and loads it into Python
urls = df["URL"].dropna().tolist() # drops any empty cells in the "URL" column and converts it to a list

print(urls)


