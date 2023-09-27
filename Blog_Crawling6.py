# total_page 전체 출력하는 코드 작성

import requests
from bs4 import BeautifulSoup
import re
import json
import pandas as pd

# def get_blog_list(keyword):

keyword = "테슬라"


blog_urls = []
Blog = []

h = {
    "Cookie":"NNB=OURWEDJJKXKGI; nx_ssl=2; _naver_usersession_=uvtwjB77yKbjyenRVbVFPA==; page_uid=ie7DZsp0J1Zssk0iLRdssssstyo-479506"
    , "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

page = 1
while True:

    print("page: ", page)

    start = (page * 30) + 1

    URL = f"https://s.search.naver.com/p/blog/search.naver?where=blog&sm=tab_pge&api_type=1&query={keyword}&rev=44&start={start}&dup_remove=1&post_blogurl=&post_blogurl_without=&nso=so%3Add%2Cp%3Afrom20230922to20230921&nlu_query=%7B%22r_category%22%3A%2233+25%22%7D&dkey=0&source_query=&nx_search_query={keyword}&spq=0&_callback=viewMoreContents"
    res = requests.get(URL, headers=h)

    try:
        for data in re.finditer("{.*}", res.text):
            total_page = int(json.loads(data.group())["total"]) // 30
            html = json.loads(data.group())["html"]
            soup = BeautifulSoup(html, "html.parser")

    except:
        for data in re.finditer("{.*}", res.text):
            total_page = int(data.group().split(":")[1].split(",")[0].replace('"', ""))
            for html in re.finditer("\<[^\>*].*\>", data.group()):
                html = re.sub("\\\\", "", str(html.group()))
                soup = BeautifulSoup(html, "html.parser")

    blogs = []
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

        if soup.select_one("span.se-fs-.se-ff-") != None:
            # 네이버 블로그
            category = soup.select_one("div.blog2_series a").text
            title = soup.select_one("span.se-fs-.se-ff-").text
            writer = soup.select_one("span.nick a").text
            date = soup.select_one("span.se_publishDate").text
            content = soup.select_one("div.se-main-container").text.replace("\n", "").strip()
        elif soup.select_one("h3.se_textarea") != None:
            # 네이버 블로그
            category = soup.select_one("div.blog2_series a").text
            title = soup.select_one("h3.se_textarea").text
            writer = soup.select_one("span.nick a").text
            date = soup.select_one("span.se_publishDate").text
            content = soup.select_one("div.se_component_wrap.sect_dsc.__se_component_area").text.replace("\n", "").strip()
        elif soup.select_one("h1") != None:
            # 티스토리 블로그
            blog_url = blog
            res = requests.get(blog_url, headers=h)
            soup = BeautifulSoup(res.text, "html.parser")
            
            try:
                category = soup.select_one("div.category").text
                title = soup.select_one("h1").text
                writer = soup.select_one("span.author").text
                date = soup.select_one("span.date").text
                content = soup.select_one("div.tt_article_useless_p_margin").text.replace("\n", "").strip()
            except:
                print("카테고리가 없대!!!!!")
        elif soup.select_one("h3.tit_post") != None:
            # 티스토리 블로그
            blog_url = blog
            res = requests.get(blog_url, headers=h)
            soup = BeautifulSoup(res.text, "html.parser")

            category = soup.select_one("strong.tit_category a").text
            title = soup.select_one("h3.tit_post").text
            writer = soup.select_one("span.info_post").text.split("\n")[0]
            date = soup.select_one("span.info_post").text.split("\n")[1].strip()
            content = soup.select_one("div.contents_style p").text
        elif soup.select_one("div.post-cover div.inner h1") != None:
            # 티스토리 블로그
            blog_url = blog
            res = requests.get(blog_url, headers=h)
            soup = BeautifulSoup(res.text, "html.parser")

            category = soup.select_one("span.category").text
            title = soup.select_one("div.post-cover div.inner h1").text
            writer = soup.select_one("span.author").text.split(" ")[1]
            date = soup.select_one("span.date").text
            content = soup.select_one("div.contents_style").text.replace("\n", "").strip()
        elif soup.select_one("div.post-cover h1") != None:
            # 티스토리 블로그
            blog_url = blog
            res = requests.get(blog_url)
            soup = BeautifulSoup(res.text, "html.parser")

            category = soup.select_one("span.category").text
            title = soup.select_one("div.post-cover h1").text
            writer = soup.select_one("span.author").text
            date = soup.select_one("span.date").text
            content = soup.select_one("div.tt_article_useless_p_margin").text.replace("\n", "").strip()
        elif soup.select_one("h2.title-article") != None:
            # 티스토리 블로그
            blog_url = blog
            res = requests.get(blog_url, headers=h)
            soup = BeautifulSoup(res.text, "html.parser")
            
            category = soup.select_one("p.category").text
            title = soup.select_one("h2.title-article").text
            writer = soup.select_one("span.writer").text
            date = soup.select_one("span.date").text
            content = soup.select_one("div.article-view").text.replace("\n", "").strip()
        elif soup.select_one("span#cphMain_dlArtList_lbArtTitle_0") != None:
            # yes24 블로그
            blog_url = blog
            res = requests.get(blog_url, headers=h)
            soup = BeautifulSoup(res.text, "html.parser")

            category = soup.select_one("span#cphMain_dlArtList_lbArtCateNm_0").text
            title = soup.select_one("span#cphMain_dlArtList_lbArtTitle_0").text
            writer = blog_url.split("&")[0].split("=")[1]
            date = soup.select_one("span#cphMain_dlArtList_lbWriteDate_0").text
            content = soup.select_one("span#cphMain_dlArtList_lbArtCont_0").text.replace("\n", "").strip()
        else:
            print("다른 타입의 블로그 발견!")
            print(blog)

        blog_urls.append(blog_url)
        print(blog_url)
        blog = (category, title, writer, date, content, blog_url)
        Blog.append(blog)           

    print(pd.DataFrame(Blog, columns=["카테고리", "제목", "작성자", "작성일시", "원문", "URL"]))

    if page == total_page:
        break 

    page += 1
    # print(get_blog_list("테슬라"))