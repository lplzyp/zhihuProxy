# coding:utf-8
from __future__ import division  # 精确除法
from Queue import Queue
from __builtin__ import False
import json
import os
import re
import platform
import uuid
import urllib
import urllib2
import sys
import time
import MySQLdb as mdb
from Libs import Libs
from bs4 import BeautifulSoup
from DBProxy import DBProxy
from logHandler import logHandler
from zhihuSpider import zhihuSpider

reload(sys)
sys.setdefaultencoding("utf-8")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
}

if __name__ == '__main__':
    # # step one: 抓取广场话题
    # if False == zhihuSpider().grabSquareTopic():
    #     print("广场话题抓取失败")
    #
    # # step two: 抓取广场话题下对应的话题
    # if False == zhihuSpider().grabTopic():
    #     print("话题抓取失败")

    # step three: 抓取话题下对应的问答
    if False == zhihuSpider().grabActivity():
        print("问答抓取失败")