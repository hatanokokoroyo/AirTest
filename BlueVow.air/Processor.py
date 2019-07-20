# -*- encoding=utf8 -*-
__author__ = "kokoro"

from airtest.core.api import *
import Operator as operator

def expedition():
    ''' 执行出征 '''
    operator.touch_button_expedition()
    sleep(2)
    
def first_enter_level(level):
    # 根据level, 判断章节
    target_chapter = int(level[0])
    # 判断当前章节(目前仅支持前三章)
    current_chapter = judge_current_chapter()
    print('目标章节: ' + str(target_chapter) + ' , 当前章节: ' + str(current_chapter))
    if current_chapter == 0:
        raise NotFoundChapter()
    if current_chapter < target_chapter:
        print('当前章节不符, 向右切换')
        for i in range(target_chapter - current_chapter):
            operator.touch_right_chapter()
            sleep(2)
    elif current_chapter > target_chapter:
        print('当前章节不符, 向左切换')
        for i in range(current_chapter - target_chapter):
            operator.touch_left_chapter()
            sleep(2)
    enter_level(level)
    
def enter_level(level):
    operator.touch_level(level)
    sleep(1.5)
    operator.touch_button_expedition()
    
def switch_to_auto():
    sleep(4)
    if exists(Template(r"tpl1563630274251.png", record_pos=(0.43, -0.203), resolution=(2340, 1080))):
        touch(Template(r"tpl1563630274251.png", record_pos=(0.43, -0.203), resolution=(2340, 1080)))

        
        
def fighting():
    sleep(3)
    second = 0
    while True:
        touch([2140, 990])
        sleep(0.5)
        second += 0.5
        if second % 10 != 0:
            continue
        if exists(Template(r"tpl1563630394833.png", record_pos=(0.0, 0.183), resolution=(2340, 1080))):
            break

def judge_current_chapter():
    if exists(Template(r"tpl1563630424761.png", record_pos=(0.35, 0.009), resolution=(2340, 1080))):
        return 1
    if exists(Template(r"tpl1563630439009.png", record_pos=(0.316, -0.085), resolution=(2340, 1080))):
        return 2
    if exists(Template(r"tpl1563630451281.png", record_pos=(-0.318, -0.108), resolution=(2340, 1080))):
        return 3
    return 0
    
class NotFoundChapter():
    pass
