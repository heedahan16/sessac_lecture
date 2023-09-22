# 기사 제목, 원문, 날짜, 매체명 수집 코드 작성

import requests
from bs4 import BeautifulSoup
import re

res = requests.get("https://n.news.naver.com/mnews/article/215/0001126161?sid=101")
soup = BeautifulSoup(res.text, "html.parser")

title = soup.select_one("#title_area span").text
content = re.sub("\<[^\>]*\>", "", str(soup.select_one("#dic_area"))).replace("\n", "").replace("(사진=연합뉴스)", "")
date = soup.select_one(".media_end_head_info_datestamp_time")["data-date-time"]
media = soup.select_one("img.media_end_head_top_logo_img.light_type")["title"]

result = (title, content, date, media)
