import requests
from bs4 import BeautifulSoup

request = requests.get("https://so.iqiyi.com/so/q_python?source=suggest&sr=1491347455602s_sr=1&s_token=main#p'y't")
content = request.content
soup = BeautifulSoup(content,"html.parser")
for element in soup.find_all('li',{"class":"list_item"}):
    video_title = element.get('data-searchpingback-albumname')
    #print(element)
    print(video_title)



