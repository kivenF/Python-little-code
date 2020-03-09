import requests
from bs4 import BeautifulSoup
import re
import time


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'
}
url = 'https://www.dytt8.net/'

print('开始连接')
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'lxml')
print('开始爬虫')

soup = str(soup)
movie_links = re.findall(r'<a href="/(.*?\.html)">(\d.*?)</a>', soup)


mo_len = len(movie_links)
movie_seeds=[]

for catch_cycle in range(mo_len):
    try:
        print('正在爬取,已经完成:%.2f%%' % (catch_cycle/mo_len*100))
        res = requests.get(url+movie_links[catch_cycle][0], headers=headers)

    except :
        print('重新连接')
        try:
            print('正在爬取,已经完成:%.2f%%' % (catch_cycle/mo_len*100))
            res = requests.get(url+movie_links[catch_cycle][0], headers=headers)
            
        except:
            print('连接超时')
        
    soup = BeautifulSoup(res.content, 'lxml')
    soup = str(soup)
    temp=re.findall(r'"(ftp://.*?.mkv)"', soup)
    
    if len(temp) ==0:
        movie_seeds.append('未找到链接')
    
    else:
        movie_seeds.append(temp[0])
        
print('100%')


file_name = 'movie_list.text'
with open(file_name, 'w', encoding='utf-8') as f:
    for i in range(mo_len):
        f.write(movie_links[i][1]+':'+movie_seeds[i]+'\n')

print("成功！")
