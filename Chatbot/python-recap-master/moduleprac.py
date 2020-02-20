import urllib.request as ur
# # URL과 저장 경로 지정하기
# url = "http://uta.pw/shodou/img/28/214.png"
# savename = "test.png"
# # 다운로드 
# urllib.request.urlretrieve(url, savename)
# print("저장되었습니다...!")

# res = ur.urlopen("http://www.naver.com/")
# print(type(res))
# print(res.status)
# print(res.version)
# print(res.msg)
# res_header = res.getheaders()
# print("###############[header 정보]#############")
# for s in res_header:
#     print(s)

# res = ur.urlopen("http://70.12.116.160:8080/login/login.html")
# print(res)
# res_header = res.getheaders()
# print("###############[header 정보]#############")
# for s in res_header:
#     print(s)

# print("\n","\n")
# print("###############[body 정보]#############")
# print(res.read().decode('utf-8'))

# url = 'http://www.python.org/'
# f = ur.urlopen(url)
# print(type(f))
# print(type(f.info()))
# encoding = f.info().get_content_charset()
# print(url, '페이지 인코딩 정보 : ', encoding)
# text = f.read(1000).decode(encoding)
# print(text)


# url 주소 해석 parse 모듈 실습
from urllib.parse import urlparse

url2 = urlparse('https://docs.python.org:8080/ko/3/library/urllib.request.html#odule-urllib.requdst')

print("도메인 정보", url2.netloc)
print("패스 정보", url2.path)
print("쿼리 문자열 정보", url2.query)
print("url 스킴 정보", url2.scheme)
print("포트 정보", url2.port)
print("프레그먼트 정보", url2.fragment)
print("url 문자열 정보", url2.geturl())
print("url 객체 정보", url2)

