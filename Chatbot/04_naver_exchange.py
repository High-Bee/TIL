# 0. 관련 모듈 import
import requests
from bs4 import BeautifulSoup


# 1. 문자열 형태로 문서가져오기
result = requests.get("https://finance.naver.com/marketindex/").text
html = result

# 2. BeautifulSoup 클래스 객체 받기
soup = BeautifulSoup(html, "html.parser")
print(type(soup))
# 3. 원하는 선택자 내용 가져오기

Exchange = soup.select_one("#worldExchangeList > li:nth-child(1) > a.head.jpy_usd > div > span.value").text


# 4. 결과물 출력
print(Exchange)

