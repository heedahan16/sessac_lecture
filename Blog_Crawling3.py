# 블로그 목록에서 링크를 가져와서 get_blog 함수와 연결하고 첫 페이지에 나오는 블로그 템플릿 유형별 처리 코드 작성

import requests
from bs4 import BeautifulSoup

def get_blog(URL):
    h = {
        "Cookie":"NNB=OURWEDJJKXKGI; nx_ssl=2; page_uid=ie6yTwprvhGssPin9eGssssstv0-488473; _naver_usersession_=egn4X5t/j74XmG/6Ez6sgQ=="
        , "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    }

    res = requests.get(URL, headers=h)
    soup = BeautifulSoup(res.text, "html.parser")

    urls = []
    for a in soup.select("div.total_area a"):
        if a["class"] == ['api_txt_lines', 'total_tit']:
            urls.append(a["href"])

    for url in urls:
        res = requests.get(url, headers=h)
        soup = BeautifulSoup(res.text, "html.parser")

        try:
            blogId = url.split("/")[-2]
            logNo = url.split("/")[-1]

            blog_url = f"https://blog.naver.com/PostView.naver?blogId={blogId}&logNo={logNo}"
            res = requests.get(blog_url, headers=h)
            soup = BeautifulSoup(res.text, "html.parser")

            category = soup.select_one("div.blog2_series a").text
            title = soup.select_one("div.pcol1").text.replace("\n", "").strip()
            writer = soup.select_one("span.nick a").text
            date = soup.select_one("span.se_publishDate").text
            content = soup.select_one("div.se-main-container").text.replace("\n", "").replace("\u200b", "").strip()

        except:

            blog_url = url
            res = requests.get(blog_url, headers=h)
            soup = BeautifulSoup(res.text, "html.parser")

            category = soup.select_one("span#cphMain_dlArtList_lbArtCateNm_0").text
            title = soup.select_one("span#cphMain_dlArtList_lbArtTitle_0").text
            writer = url.split("&")[0].split("=")[1]
            date = soup.select_one("span#cphMain_dlArtList_lbWriteDate_0").text
            content = soup.select_one("div.blogContArea").text.replace("\n", "").strip()
            
    return (category, title ,writer, date, content, blog_url)

print(get_blog("https://search.naver.com/search.naver?where=blog&query=%ED%85%8C%EC%8A%AC%EB%9D%BC&sm=tab_opt&nso=so:dd,p:from20230921to20230922"))