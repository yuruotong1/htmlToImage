# -*- coding: UTF-8 -*-
from selenium import webdriver
#from bs4 import BeautifulSoup\
import re


class Html():
    def __init__(self,name,background,two_dimension):
        self.name=name
        self.background=background
        self.two_dimension=two_dimension
        self.f = open(name+".html","w",encoding='utf-8')

    def setText(self,title,context):
        html = """   
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
        <style>
            *{
                margin: 0px;
                padding: 0px;
                            position: absolute;
            }
            #div{
      
                width: 1512px;
                height: 2259px;
                background-image: url(%s);
            }
            #div1{
                width: 230px;
                height: 218px;
                background-image: url(%s);
                top: 1580px;
                left: 1105px;
            }
            #div2{ 
                font-size: 75px;
                top: 330px;
                left: 80px;
                
            }
            #div3{  
             
                line-height:100px;
                font-size: 50px;
                letter-spacing:7px;
                top: 1480px;
                left: 135px;
            }

        </style>

    </head>
    <body>
         <div id="div">
             <div id="div1"></div>
             <div id="div2">
                <p style="width:900px">%s</p> 
            </div>
             <div id="div3">
                 <p style="width:700px">%s</p>
            </div>
         </div>
    </body>
    </html>    
    """%(self.background,self.two_dimension,title,context)
        self.f.write(html)
        self.f.close()    

    def toImage(self,html_path):
        driver = webdriver.PhantomJS();
        driver.get('file:///'+html_path+self.name+".html");
        driver.save_screenshot(self.name+'.png');
        driver.quit();

if __name__ == '__main__':
    html_path='C:/Users/RuotongYu/Desktop/techTex/knowledgeCard/'
    t=Html("yes","背景no.jpg","二维码.jpg")
    t.setText("啊打发法苦左","阿凡达发夺")
    t.toImage(html_path)
    
