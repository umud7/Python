import requests
from bs4 import BeautifulSoup

headers_param ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}
glassdor = requests.get("https://www.glassdoor.com/Job/front-end-developer-jobs-SRCH_KO0,19.htm",headers=headers_param)

print(glassdor.content)