# 검색어를 입력했을 때 첫 페이지에서 목록을 가져와서 블로그를 수집하는 함수와 연결해서 DataFrame으로 리턴하는 코드 작성

import requests
from bs4 import BeautifulSoup
import re
import json
import pandas as pd

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

    return(category, title, writer, date, content, url)


def get_blog_list(keyword):

    blog = []

    headers = {
            "Cookie":"BA_DEVICE=9e7cf893-1866-45c7-bced-8f6024c83aeb; NNB=EBHCWBDFIDSGI; nx_ssl=2; JSESSIONID=2F036FA7D27C18426CF9FAA7EFA39752.jvm1"
        }

    url = f"https://s.search.naver.com/p/blog/search.naver?where=blog&sm=tab_pge&api_type=1&query={keyword}&rev=44&start=1&dup_remove=1&post_blogurl=&post_blogurl_without=&nso=&nlu_query=%7B%22r_category%22%3A%2233+25%22%7D&dkey=0&source_query=&nx_search_query={keyword}&spq=0&_callback=viewMoreContents"
    res = requests.get(url, headers=headers)

    for data in re.finditer("{.*}", res.text):
        # total = int(json.loads(data.group())["total"]) // 30
        html = json.loads(data.group())["html"]
        soup = BeautifulSoup(html, "html.parser")

    for a in soup.select("li.bx div.total_area a"):
        if a["class"] == ['api_txt_lines', 'total_tit']:
            blog.append(get_blog(a["href"]))

    return pd.DataFrame(blog, columns = ["카테고리", "제목", "작성자", "작성일시", "원문", "URL"])

print(get_blog_list("테슬라"))

    