import time
import pandas as pd
import requests
from selenium import webdriver
from bs4 import BeautifulSoup

steam = []
temp = []
names = []
p1 = []
p2 = []
p3 = []
p4 = []
for x in range(10, 10000, 10):
    req = requests.get("https://store.steampowered.com/app/"+str(x))
    soup = BeautifulSoup(req.content,'lxml')
    i = 0
    t = 1
    name = soup.find_all("div", class_="apphub_AppName")
    t1 = soup.find_all("span", class_="responsive_hidden")
    t2 = soup.find_all("span", class_="game_review_summary")
    if x % 1000 == 0:
        dic = {'name': names, 'Recent Reviews': p1, 'Recent Reviews Number': p2, 'Overall Reviews': p3, 'Overall Reviews Names': p4}    
        df = pd.DataFrame(dic)
        df.to_csv('checkpoint'+str(x)+'.csv') 
    if len(t2) == 0:
        continue
    if len(t1) == 0:
        continue
    if len(name) == 0:
        continue
    names.append(name[0].text)
    p1.append(t2[0].text)
    p2.append(t1[0].text.replace('\r', '').replace('\t','').replace('\n','').replace('(','').replace(')',''))
    p3.append(t2[0].text)
    p4.append(t1[0].text.replace('\r', '').replace('\t','').replace('\n','').replace('(','').replace(')',''))
    steam.append(temp)  
    req.close() 
    print(name[0].text + " DONE; " + str(x))

        
    
print(names)
print(type(steam))
dic = {'name': names, 'Recent Reviews': p1, 'Recent Reviews Number': p2, 'Overall Reviews': p3, 'Overall Reviews Names': p4}    
df = pd.DataFrame(dic)
df.to_csv('GFG.csv') 
