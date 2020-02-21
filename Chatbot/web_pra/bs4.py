from bs4 import BeautifulSoup

bs = BeautifulSoup(html_doc, 'html.parser')
print(bs.find_all('p'))
print(bs.find('p'))
print("--"*10)

p_tags = bs.find_all('p')
for tag in p_tags:
    print(tag)