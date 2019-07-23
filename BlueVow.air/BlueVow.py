# -*- encoding=utf8 -*-
__author__ = "kokoro"

from airtest.core.api import *
import Processor as processor

auto_setup(__file__)

def main():
    level = '3-4'
    times = 20
    # 点击出征
    processor.expedition()
    # 进入关卡
    processor.first_enter_level(level)
    # 切换为自律模式
    processor.switch_to_auto()
    for i in range(times):
        # 作战中
        processor.fighting()
        # 
        processor.enter_level(level)

def main2():
    processor.fighting()
    
if __name__ == 'airtest.cli.runner':
    print("开始执行脚本")
    main()
#     main2()