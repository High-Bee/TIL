from selenium import webdriver

# chrom_driver = webdriver.Chrome('C:/Users/student/Desktop/chromedriver.exe')
# chrom_driver.implicitly_wait(3)
# chrom_driver.get('https://google.com')
# chrom_driver.save_screenshot('./output/google_site.png')
# chrom_driver.close()


## phantomJS 사용 브라우저 제어

# url = "http://www.naver.com"
# browser = webdriver.PhantomJS('C:/Users/student/Desktop/phantomjs-2.1.1-windows/bin/phantomjs.exe')
# browser.implicitly_wait(3)
# browser.get('https://www.naver.com')
# browser.save_screenshot('./output/naver_site.png')
# browser.quit()

#############################################################
## selenium web page 가져오기
from selenium import webdriver
from bs4 import BeautifulSoup

# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# options.add_argument('--diable-dev-shm-usage')

# chrom_driver = webdriver.Chrome('C:/Users/student/Desktop/chromedriver.exe', options=options)
# chrom_driver.implicitly_wait(3)
# chrom_driver.get('https://www.hanbit.co.kr/member/login.html')

# # id pswd
# chrom_driver.find_element_by_name('m_id').send_keys('ykyb1211')
# chrom_driver.find_element_by_name('m_passwd').send_keys('qwer1121')

# # login button event
# chrom_driver.find_element_by_xpath('//*[@id="login_btn"]').click()

# chrom_driver.get('https://www.hanbit.co.kr/myhanbit/myhanbit.html')
# html = chrom_driver.page_source
# soup = BeautifulSoup(html, 'html.parser')

# mileage = soup.select_one('.mileage_section1 > dd > span').text
# ecoin = soup.select_one('.mileage_section2 > dd > span').text
# print('마일리지 :' +mileage)
# print('이코인 :' +ecoin )

# rank = soup.select_one('.my_rating > p > span').text
# print('회원등급 :' +rank )

#####################################################

'https://accounts.kakao.com/login?continue=https%3A%2F%2Flogins.daum.net%2Faccounts%2Fksso.do%3Frescue%3Dtrue%26url%3Dhttps%253A%252F%252Fwww.daum.net%252F'


options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--diable-dev-shm-usage')

chrom_driver = webdriver.Chrome('C:/Users/student/Desktop/chromedriver.exe', options=options)
chrom_driver.implicitly_wait(3)
chrom_driver.get('https://accounts.kakao.com/login?continue=https%3A%2F%2Flogins.daum.net%2Faccounts%2Fksso.do%3Frescue%3Dtrue%26url%3Dhttps%253A%252F%252Fwww.daum.net%252F'
)

# # id pswd
chrom_driver.find_element_by_name('email').send_keys('ykyb1211@gmail.com')
chrom_driver.find_element_by_name('password').send_keys('qwer1121')


# login
chrom_driver.find_element_by_xpath('//*[@id="login-form"]/fieldset/div[8]/button').click()

chrom_driver.get('https://www.daum.net')
html = chrom_driver.page_source
soup = BeautifulSoup(html, 'html.parser')
unread = soup.select_one("ul > li> em > a")
print("읽지 않은 메일 : " ,unread)
chrom_driver.close()