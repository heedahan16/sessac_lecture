# 기사 제목, 원문, 날짜, 매체명 수집 함수 작성

import requests
from bs4 import BeautifulSoup
import re

def get_news(URL):
    res = requests.get(URL)
    soup = BeautifulSoup(res.text, "html.parser")

    title = soup.select_one("h2#title_area span").text
    content = re.sub("\<[^\>]*\>", "", str(soup.select_one("article#dic_area"))).replace("(사진=연합뉴스)", "").replace("\n", "")
    date = soup.select_one("span.media_end_head_info_datestamp_time")["data-date-time"]
    media = soup.select_one("img.media_end_head_top_logo_img")["title"]

    return (title, content, date, media, URL)

get_news("https://n.news.naver.com/mnews/article/215/0001126161?sid=101")