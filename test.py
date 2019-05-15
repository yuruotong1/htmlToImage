# -*- coding: UTF-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import re


class Html():
    def __init__(self,name):
        self.name=name
        self.soup=BeautifulSoup(open("./html/"+name+".html",encoding='utf-8'),"lxml")
    def saveHtml(self,context):
        f = open("./html/"+self.name+".html","w",encoding='utf-8')
        f.write(context)
        f.close()
        
    def setText(self,title="",context=""):
        # 第一个p标签是问题
        self.soup.find_all('p')[0].string = title
        # 第二个p标签是回答
        self.soup.find_all('p')[1].string = context
        self.saveHtml(self.soup.prettify())

  
    def toImage(self,html_path):
        driver = webdriver.PhantomJS(executable_path="./driver/phantomjs");
        driver.get('file:///'+html_path+self.name+".html");
        driver.save_screenshot(self.name+'.png');
        driver.quit();

if __name__ == '__main__':
    html_path='C:/Users/RuotongYu/Desktop/techTex/knowledgeCard/html/'
    t=Html("1")
    t.setText("daffa11111afda","11111adfafa")
    t.toImage(html_path)
	
    
