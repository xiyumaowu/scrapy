from urllib import request
from bs4 import BeautifulSoup
import re
first_url = "http://www.xiaohuar.com/hua"
header = {"User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}
req = request.Request(url=first_url, headers=header)
response = request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, 'html.parser', from_encoding='gbk')
imgs = soup.find_all('img', src=re.compile(r'/d/file/\d+/\w+\.jpg'))
for img in imgs:
	url = "http://www.xiaohuar.com" + img['src']
	req = request.Request(url=url, headers=header)
	data = request.urlopen(req)
	f = open('./img/' + img['alt']+'.jpg', 'wb')
	f.write(data.read())
	f.close()
