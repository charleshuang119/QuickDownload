import re
import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.youtube.com/results?search_query=python")
content = request.content
soup = BeautifulSoup(content,"html.parser")
# for element in soup.find_all('a',{"rel":"spf-prefetch"}):
#     #Get the value of each image, for example, 7lmCu8wz8ro
#     img_value=element.get('href').split("=")[1]
#     all_img=soup.find_all('img',{"alt":True,"width":True,"height":True,"onload":True})
#     #Insert the image value into href to get full address of image
#     img=re.findall("https://i.ytimg.com/vi/{}/[\S]+".format(img_value),str(all_img))
#     #delete char ([,",',]), since image return a list, which has []
#     img = str(img).strip("[\"\']")
#     print(img)
# #print(all_img)

#Second way to get image href

for element in soup.find_all('img',{"alt":True,"width":True,"height":True,"onload":True}):
    img = None
    if "i.ytimg.com/vi" in str(element.get("src")):
        img=element.get("src")
    elif "i.ytimg.com/vi" in str(element.get("data-thumb")):
        img = element.get("data-thumb")
    if img !=  None:
        print(img)



