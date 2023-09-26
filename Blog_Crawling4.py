# 블로그 페이지 처리 코드 작성

import requests
from bs4 import BeautifulSoup
import re
import json
import pandas as pd

keyword = "테슬라"

page = 1
start = (page * 30) + 1

print("page: ", page)

blogs = []
Blog = []

h = {
    "Cookie":"NNB=OURWEDJJKXKGI; nx_ssl=2; _naver_usersession_=uvtwjB77yKbjyenRVbVFPA==; page_uid=ie7DZsp0J1Zssk0iLRdssssstyo-479506"
    , "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}
URL = f"https://s.search.naver.com/p/blog/search.naver?where=blog&sm=tab_pge&api_type=1&query={keyword}&rev=44&start={start}&dup_remove=1&post_blogurl=&post_blogurl_without=&nso=so%3Add%2Cp%3Afrom20230922to20230921&nlu_query=%7B%22r_category%22%3A%2233+25%22%7D&dkey=0&source_query=&nx_search_query={keyword}&spq=0&_callback=viewMoreContents"
res = requests.get(URL, headers=h)
for data in re.finditer("{.*}", res.text):
    total_page = int(json.loads(data.group())["total"]) // 30
    html = json.loads(data.group())["html"]
    soup = BeautifulSoup(html, "html.parser")

    for a in soup.select("li.bx div.total_area a"):
        if a["class"] == ['api_txt_lines', 'total_tit']:
            blogs.append(a["href"])

for blog in blogs:
    res = requests.get(blog, headers=h)
    soup = BeautifulSoup(res.text, "html.parser")

    blogId = blog.split("/")[-2]
    logNo = blog.split("/")[-1]

    blog_url = f"https://blog.naver.com/PostView.naver?blogId={blogId}&logNo={logNo}"
    res = requests.get(blog_url, headers=h)
    soup = BeautifulSoup(res.text, "html.parser")

    category = soup.select_one("div.blog2_series a").text
    title = soup.select_one("div.pcol1 span").text
    writer = soup.select_one("span.nick a").text
    date = soup.select_one("span.se_publishDate").text
    content = soup.select_one("div.se-main-container").text.replace("\n", "").strip()

    blog = (category, title, writer, date, content, blog_url)
    Blog.append(blog)

print(pd.DataFrame(Blog, columns=["카테고리", "제목", "작성자", "작성일시", "원문", "URL"]))