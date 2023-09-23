# 네이버 뉴스 목록에서 네이버 뉴스 링크를 가져와서 기사 제목, 날짜, 매체명, 본문, URL을 수집하는 함수를 연결하고 데이터프레임으로 만들기

import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

def get_news_list(URL):

    res = requests.get(URL)
    soup = BeautifulSoup(res.text, "html.parser")

    links = []
    for a in soup.select("ul.list_news div.info_group a"):
        if (a.text == "네이버뉴스"):
            links.append(a["href"])

    Data = []
    for link in links:
        res = requests.get(link)
        soup = BeautifulSoup(res.text, "html.parser")

        title = soup.select_one("h2#title_area span").text
        date = soup.select_one("span.media_end_head_info_datestamp_time")["data-date-time"]
        media = soup.select_one("img.media_end_head_top_logo_img.light_type")["title"]
        for reg in re.finditer("[0-9[가-힣].*", (re.sub("\(사진=.{3}\)|<[^\>]*>|&lt;|&gt;", "", str(soup.select_one("div#newsct_article")).replace("\n", "").replace("◀ 리포 트 ▶", "◀ 리포트 ▶")))):
            content = reg.group().replace("  ", " ").strip()

        data = (title, date, media, content, link)
        Data.append(data)

    return pd.DataFrame(Data, columns=["제목", "날짜", "매체명", "본문", "URL"])

