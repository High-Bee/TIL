from selenium import webdriver
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--diable-dev-shm-usage')

chrom_driver = webdriver.Chrome('C:/Users/student/Desktop/chromedriver.exe', options=options)
chrom_driver.implicitly_wait(3)
chrom_driver.get('https://goo.gl/VH1A5t')
chrom_driver.find_element_by_xpath('//*[@id="gnb_0_0"]').click()

gu_list_raw = chrom_driver.find_element_by_xpath('//*[@id="SIGUNGU_NM0"]')
gu_list = gu_list_raw.find_elements_by_tag_name("option")

gu_names = [option.get_attribute("value") for option in gu_list]

print(gu_names)



chrom_driver.close()