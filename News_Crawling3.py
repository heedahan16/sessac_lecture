# 네이버 뉴스 목록에서 네이버 뉴스 링크를 가져오는 코드 작성

import requests
from bs4 import BeautifulSoup

res = requests.get("https://search.naver.com/search.naver?where=news&query=%ED%85%8C%EC%8A%AC%EB%9D%BC&sm=tab_opt&sort=1&photo=0&field=0&pd=2&ds=&de=&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Add%2Cp%3A1m&is_sug_officeid=0&office_category=0&service_area=0")
soup = BeautifulSoup(res.text, "html.parser")

links = []
for a in soup.select("ul.list_news div.info_group a"):
    if a["class"] == ["info"]:
        links.append(a["href"])
        