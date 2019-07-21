# -*- encoding=utf8 -*-
__author__ = "kokoro"

from airtest.core.api import *

def touch_home():
    ''' 主页键 '''
    keyevent("3")
       
def touch_back():
    ''' 返回键 '''
    keyevent("4")
    
def touch_button_expedition():
    touch(Template(r"tpl1563630478629.png", record_pos=(0.323, 0.126), resolution=(2340, 1080)))


    
def touch_left_chapter():
    touch([180, 530])

    
def touch_right_chapter():
    touch([2230, 530])
    
def touch_level(level):
    location = {
        '1-1': [400, 265],
        '1-2': [650, 610],
        '1-3': [1080, 150],
        '1-4': [1030, 535],
        '2-1': [400, 665],
        '2-2': [645, 255],
        '2-3': [1080, 650],
        '2-4': [1330, 215],
        '3-1': [360, 600],
        '3-2': [700, 210],
        '3-3': [1070, 630],
        '3-4': [1310, 300]
    }
    touch(location.get(level, None))
