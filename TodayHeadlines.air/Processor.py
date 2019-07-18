# -*- encoding=utf8 -*-
__author__ = "kokoro"

from airtest.core.api import *
import Operator as operator
import time

def open_today_headlines():
    print('开始执行 [打开今日头条]')
    # 点击两次主页键
    operator.touch_home()
    operator.touch_home()
    # 左滑三次, 抵达今日头条所在页
    swipe([1050, 800], [15, 800])
    swipe([1050, 800], [15, 800])
    swipe([1050, 800], [15, 800])
    # 滑动特效可能导致图像识别失败, 延时1s
    time.sleep(1)
    # 打开今日头条

    touch(Template(r"tpl1563417199187.png", record_pos=(0.115, -0.505), resolution=(1080, 1920)))


def search_five_times():
    time.sleep(1.5)
    print('开始执行[点击搜索框推荐词5次]')
    # 点击首页
    operator.touch_app_home()
    time.sleep(1.5)
    # 点击搜索框
    operator.touch_app_search_bar()
    time.sleep(1.5)
    # 点击第一个推荐词
    for i in range(5):
        touch([200, 250])
        time.sleep(1.5)
        operator.touch_back()
        time.sleep(1)
    operator.touch_back()
    time.sleep(2)


        
def read_loop():
    # 点击首页
    operator.touch_app_home()
    time.sleep(2)
    # 预防万一, 多看5次
    for i in range(35):
        # 置顶的文章貌似是不给金币的, 所以先上滑一次
        swipe([500, 1565], [500, 1065])
        time.sleep(1)
        touch(Template(r"tpl1563451046681.png", record_pos=(-0.168, -0.31), resolution=(1080, 1920)))
        time.sleep(1.5)
        if not exists(Template(r"tpl1563458236019.png", record_pos=(0.002, -0.766), resolution=(1080, 1920))):
            i = i - 1;
            operator.touch_back()
            time.sleep(2)
            continue
            
        start = time.time()
        period = time.time() - start
        # 在文章内停留35s, 期间上下滑动, 然后调用返回键
        while period <= 35:
            print(str(int(period)) + '/35s')
            swipe([500, 1565], [500, 1065])
            time.sleep(1.5)
            swipe([500, 1065], [500, 1565])
            period = time.time() - start
        operator.touch_back()
        time.sleep(2)
        print('当前进度: ' + str(i) + '/35')

        
def main():
#     processor.open_today_headlines()
    processor.search_five_times()
#     processor.read_loop()

if __name__ == 'airtest.cli.runner':
    main()


