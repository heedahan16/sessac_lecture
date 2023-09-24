# 기간을 입력했을 때, 하루씩 이동하면서 데이터를 수집하고 결과를 csv 파일로 저장하는 코드 작성

import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

def get_news(keyword, start_date, end_date):

    urls = []
    Data = []

    for date in pd.date_range(start_date, end_date):
        print("date :", str(date).split(" ")[0])

        page = 1
        while True:

            print("page: ", page)

            start = (int(page) - 1) * 10 + 1

            res = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_pge&query={keyword}&sort=1&photo=0&field=0&pd=3&ds={start_date}&de={end_date}&mynews=0&office_type=0&office_section_code=0&news_office_checked=&office_category=0&service_area=0&nso=so:dd,p:from{start_date}to{end_date},a:all&start={start}")
            soup = BeautifulSoup(res.text, "html.parser")

            if soup.select_one("div.not_found02") != None:
                break

            page += 1

            for a in soup.select("ul.list_news div.news_area a"):
                if a.text == "네이버뉴스":
                    urls.append(a["href"])

            for url in urls:
                res = requests.get(url)
                soup = BeautifulSoup(res.text, "html.parser")
                
                title = soup.select_one("h2#title_area > span").text
                date = soup.select_one("div.media_end_head_info_datestamp span")["data-date-time"]
                media = soup.select_one("div.media_end_head_top img.media_end_head_top_logo_img.light_type")["title"]
                content = re.sub("\<br\/>|\<em.*\>.*\<\/em\>|[a-zA-Z]*\@[a-zA-Z]*\.com|뉴욕=.*|\<[^\>]*\>", "", str(soup.select_one("article#dic_area")).replace("\t", "").replace("\n", "").strip())

                data = (title, date, media, content, url)
                Data.append(data)

    News = pd.DataFrame(Data, columns=["제목", "날짜", "매체명", "본문", "URL"])

    return News.to_csv("News.csv", mode="w")

print(get_news("테슬라", "2023.09.23", "2023.09.24"))