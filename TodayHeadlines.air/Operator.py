# -*- encoding=utf8 -*-
__author__ = "kokoro"

from airtest.core.api import *

def touch_home():
    ''' 主页键 '''
    keyevent("3")
       
def touch_back():
    ''' 返回键 '''
    keyevent("4")
    
def touch_app_home():
    ''' app左下角主页键 '''
    touch([105, 1830])

def touch_app_search_bar():
    ''' app正上方搜索框, 可以考虑改成识别放大镜图标 '''
    touch([895, 145])
    
    