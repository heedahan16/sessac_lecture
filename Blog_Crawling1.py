import requests
from bs4 import BeautifulSoup

def get_blog(url):

    headers = {
        "Cookie":"BA_DEVICE=9e7cf893-1866-45c7-bced-8f6024c83aeb; NNB=EBHCWBDFIDSGI; nx_ssl=2; JSESSIONID=2F036FA7D27C18426CF9FAA7EFA39752.jvm1"
    }

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    URL = "https://blog.naver.com" + soup.select_one("iframe")["src"]
    res = requests.get(URL, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    category = soup.select_one("div.blog2_series a").text
    title = soup.select_one("div.pcol1 span").text
    writer = soup.select_one("span.writer span.nick a").text
    date = soup.select_one("span.se_publishDate").text
    content = soup.select_one("div.se-main-container").text.replace("\n", "").strip()

    return(category, title, writer, date, content)
