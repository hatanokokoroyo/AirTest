# -*- encoding=utf8 -*-
__author__ = "kokoro"

from airtest.core.api import *
import Processor as processor

auto_setup(__file__)


def main():
    print('开始执行脚本')
#     processor.open_today_headlines()
#     processor.search_five_times()
    processor.read_loop()

if __name__ == 'airtest.cli.runner':
    main()

