# -*- coding: UTF-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
from PIL import Image
import re


class Html():
    def __init__(self,name):
        self.name=name
    def openHtml(self):
        self.file =  open("./html/"+self.name+".html",encoding='utf-8')
        self.soup=BeautifulSoup(self.file,"lxml")
    def closeHtml(self):
        self.file.close()
    def saveHtml(self,context):
        self.file.close()
        f = open("./html/"+self.name+".html","w",encoding='utf-8')
        f.write(context)
        f.close()
            
    def setTitle(self,title=""):
        self.openHtml()
        # 第一个p标签是问题
        self.soup.find(id='title').p.string = title          
        self.saveHtml(self.soup.prettify())
        
     # tag对应html中div的id   
     # width设置了每行文字的个数，用来自动换行
     # lineHeight是行间距，默认100px
     # letterspacing是字与字之间的距离，默认7px
     # location设置字的位置，是二元组，用百分百来设置，比如(1,1)表示在背景图片的右下角
    def setText(self,tag,text,fontSize,location,width=900,lineHeight=100,letterSpacing=7):  
        self.openHtml()
        spacing16 =  " "*16
        pattern = "(?<=\#%s\{\n)[\s\S]*?(?=\})"%(tag)
        setLineHeight = spacing16+"line-height:%spx;\n"%(lineHeight)
        setLetterSpacing = spacing16+"letter-spacing:%spx;\n"%(letterSpacing)
        setFontSize = spacing16+"font-size: %spx;\n"%(fontSize)
        setLeft = spacing16+"left: %spx;\n"%(location[0]* self.backgroundWidth)
        setTop = spacing16+"top: %spx;\n"%(location[1]*self.backgroundHeight)
        result = re.sub(pattern,setLineHeight+setLetterSpacing+setFontSize+setLeft+ setTop,self.soup.prettify())
        self.saveHtml(result)
        self.openHtml()
        self.soup.find(id=tag).p.string = text
        self.soup.find(id=tag).p['style'] = "width:%s"%(width)
        self.saveHtml( self.soup.prettify())
        
        
    
    def setBackground(self,filePath):
        self.openHtml()
        spacing16 =  " "*16
        pattern = "(?<=\#div\{\n)[\s\S]*?(?=\})"
        im = Image.open(filePath)
        self.backgroundWidth = im.size[0]
        self.backgroundHeight = im.size[1]
        width = spacing16+"width: %spx;\n"%(self.backgroundWidth)
        height = spacing16+"height: %spx;\n"%(self.backgroundHeight)
        background = spacing16+"background-image: url(%s);\n"%(filePath)
        result = re.sub(pattern,width+height+background,self.soup.prettify())
        self.saveHtml(result)

    def setTwoDim(self,filePath,location):
        self.openHtml()
        spacing16 =  " "*16
        pattern = "(?<=\#dimen\{\n)[\s\S]*?(?=\})"
        im = Image.open(filePath)
        width = spacing16+"width: %spx;\n"%(im.size[0])
        height = spacing16+"height: %spx;\n"%(im.size[1])
        background = spacing16+"background-image: url(%s);\n"%(filePath)
        left = spacing16+"left: %spx;\n"%(location[0]* self.backgroundWidth)
        top = spacing16+"top: %spx;\n"%(location[1]*self.backgroundHeight)
        result = re.sub(pattern,width+height+background+top+left,self.soup.prettify())
        self.saveHtml(result)
    
    
    def toImage(self,html_path):
        driver = webdriver.PhantomJS(executable_path="./driver/phantomjs");
        driver.get('file:///'+html_path+self.name+".html");
        driver.save_screenshot(self.name+'.png');
        driver.quit();

if __name__ == '__main__':
    html_path='C:/Users/RuotongYu/Desktop/techTex/knowledgeCard/html/'
    t=Html("1")
    t.setBackground("./background/背景yes.jpg")
    t.setText("text1","111111222111",100,(0.5,0.5),2,2,2)
    #t.setTwoDim("./two-dimsion/二维码.jpg",(0.7,0.7))
    #t.toImage(html_path)
	
    
