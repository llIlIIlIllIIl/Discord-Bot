import requests
from bs4 import BeautifulSoup

# 웹사이트 지정
indeed_result = requests.get("https://kr.indeed.com/jobs?q=python&limit=50&radius=25&vjk=8111c2d5817c3e0e")

# HTML 출력
indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

# 특정 요소 찾기
pagination = indeed_soup.find("div", {"class": "pagination"})

# 특정 요소 찾기
pages = pagination.find_all('a')

# spans 출력
spans = []
for page in pages:
    spans.append(page.find("span"))

print(spans[:-1])