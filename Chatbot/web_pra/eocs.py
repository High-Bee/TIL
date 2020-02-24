# import urllib.request

# url = 'http://ecos.bok.or.kr/api/KeyStatisticList/UI437J5Y2Y6JZ26C9LZX/xml/kr/1/10/'

# request = urllib.request.Request(url)

# print(request)
# response = urllib.request.urlopen(request)
# print(response.read())
# print(response.getcode())


from bs4 import BeautifulSoup
import urllib.request as req
import io

key = '4WQ7X833TXC370SUTDX4'
contentType = 'xml'
startIndex = '1'
endIndex = '100'

url = 'http://ecos.bok.or.kr/api/KeyStatisticList/'+key+'/'+contentType+'/kr/'+startIndex+'/'+endIndex+'/'
savename = 'C:/Temp/ecos.xml'
req.urlretrieve(url, savename)

xml = open(savename, 'r', encoding='utf-8').read()
soup = BeautifulSoup(xml, 'xml')


ecoList = []
for itemList in soup.find_all('row') :
    class_name = itemList.find('CLASS_NAME').string
    class_name = '없음' if class_name is None else class_name
    keystat_name = itemList.find('KEYSTAT_NAME').string
    keystat_name = '없음' if keystat_name is None else keystat_name
    data_value = itemList.find('DATA_VALUE').string
    data_value = '없음' if data_value is None else data_value
    cycle = itemList.find('CYCLE').string
    cycle = '없음' if cycle is None else cycle
    unit_name = itemList.find('UNIT_NAME').string
    unit_name = '없음' if unit_name is None else unit_name
    ecoList.append((class_name, keystat_name, data_value, cycle, unit_name))

print('[ 100대 통계 지표 ]')
for class_name, keystat_name, data_value, cycle, unit_name in ecoList :
    print(class_name+','+keystat_name+','+data_value+','+cycle+','+unit_name)