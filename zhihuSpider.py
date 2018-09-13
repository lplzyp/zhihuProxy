# -*- coding: UTF-8 -*-
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
from bs4 import BeautifulSoup
import datetime
import requests
from DBProxy import DBProxy
from zhihuConfig import zhihuConfig
from logHandler import logHandler
from Libs import Libs

reload(sys)
sys.setdefaultencoding("utf-8")

class zhihuSpider:
    Log             = ""
    topicDao        = ""
    topicSquareDao  = ""
    questionDao     = ""
    userDao         = ""

    def __init__(self):
        self.Log = logHandler(zhihuConfig._log)
        self.topicDao = DBProxy()._setDB(zhihuConfig._database, zhihuConfig._topic)
        self.topicSquareDao = DBProxy()._setDB(zhihuConfig._database, zhihuConfig._squareTopic)
        self.questionDao = DBProxy()._setDB(zhihuConfig._database, zhihuConfig._question, zhihuConfig._question_num)
        self.userDao = DBProxy()._setDB(zhihuConfig._database, zhihuConfig._user, zhihuConfig._user_num)

    """
    抓取知乎话题广场
    """
    def grabSquareTopic(self):
        url = zhihuConfig._mainURL
        try:
            request     = urllib2.Request(url)
            response    = urllib2.urlopen(request)
            html        = response.read().decode('utf-8')
            soup        = BeautifulSoup(html, "html.parser")
            topicSqEles = soup.find_all('li', {'class': 'zm-topic-cat-item'})
            dataId      = self.getSquareTopicIds()
            data        = []
            now         = int(time.time())
            for ele in topicSqEles:
                data_id = ele.get('data-id')
                name    = ele.text
                if data_id in dataId:
                    continue

                data.append({
                    "topic_id"  : data_id,
                    "title"     : name,
                    "add_time"  : now
                })

            updateField = {
                "update_time": now
            }
            if data and False == self.topicSquareDao._batchInsert(data, updateField):
                self.Log._fatal("batch insert topic error,sql:%s" % self.topicSquareDao._getLastSql())
                return False

        except Exception as e:
            self.Log._fatal("GrabSquareTopic topic fail,except:%s" % e)
            return False

        return True

    """
    获取已处理的话题广场id
    """
    def getSquareTopicIds(self):
        result = self.topicSquareDao._getByPage(["topic_id"], "is_deleted = 0", -1)
        if not result:
            return []

        topic_id = []
        for key in result:
            topic_id.append("%s" % Libs().current(key))

        return topic_id

    """
    抓取话题广场下的话题
    """
    def grabTopic(self):
        squareTopicId = self.getSquareTopicIds()
        if not squareTopicId:
            self.Log._warning("getSquareTopicIds.Topic id is empty,please grab square topic id first")
            return False

        try:
            now = int(time.time())
            for id in squareTopicId:
                self.Log._notice("Start Grab Topic Beneath Square Topic Id:%s" % id)

                offset = 0
                while True:
                    param = {
                        'method': 'next',
                        'params': '{"topic_id":'+str(id)+',"offset":'+str(offset)+',"hash_id":""}'
                    }
                    response = requests.post(zhihuConfig._getTopicURL, data = param, headers = zhihuConfig._header)
                    response.encoding = "utf-8"
                    result = json.loads(response.text)
                    msg = result['msg']
                    if not msg:
                        break

                    soup = BeautifulSoup("%s" % msg, "html.parser")
                    topicEles = soup.find_all('div', {'class': 'item'})
                    data = []
                    for ele in topicEles:
                        uri = ele.find("a").get("href")
                        topic_id = uri.replace("/topic/", "")
                        title = ele.find("img").get("alt").decode('unicode_escape')
                        data.append({
                            "parent_topic_id"   : id,
                            "topic_id"          : topic_id,
                            "title"             : title,
                            "add_time"          : now,
                        })

                    updateField = {
                        "update_time": now
                    }
                    if data and False == self.topicDao._batchInsert(data, updateField):
                        self.Log._fatal("batch insert topic error,sql:%s" % self.topicDao._getLastSql())
                        return False

                    offset = (offset + 1) * 20

        except Exception as e:
            self.Log._fatal("grabTopic error,except:%s" % e)
            return False

        return True

    """
    获取已处理的话题广场id
    """
    def getTopicIds(self, page = 1, page_size = 100):
        result = self.topicDao._getByPage(["topic_id"], "is_deleted = 0", page, page_size)
        if not result:
            return []

        topic_id = []
        for key in result:
            topic_id.append("%s" % Libs().current(key))

        return topic_id

    """
    抓取话题下的相关活动
    """
    def grabActivity(self, page = 1, page_size = 100):
        while True:
            topicId = self.getTopicIds(page, page_size)
            if not topicId:
                self.Log._notice("Grab Activity finish...")
                return True

            for id in topicId:
                if False ==  self.grabDetailByTopicId(id):
                    self.Log._warning("grab detail end,id:%s" % id)
                    return False

            page = page + 1

    """
    抓取每个活动的关联信息
    """
    def grabDetailByTopicId(self, topicId):
        if not topicId:
            self.Log._warning("grabDetailByTopicId topicId empty")
            return False

        if False == self.grabHotList(topicId):
            return False

        if False == self.grabTopAnswerList(topicId):
            return False

        if False == self.grabUnanswerList(topicId):
            return False

        # if False == self.grabIndexList(topicId):
        #     return False

        return True

    # 讨论
    def grabHotList(self, topicId):
        self.Log._notice("Start to grab Hot activity,id:%s" % topicId)
        if False == self.handle(topicId, zhihuConfig._hot):
            self.Log._warning("grabHotList error,id:%s" % topicId)
            return False

        return True

    # 索引
    def grabIndexList(self, topicId):
        return True

    # 精华
    def grabTopAnswerList(self, topicId):
        self.Log._notice("Start to grab TopAnswer activity,id:%s" % topicId)
        if False == self.handle(topicId, zhihuConfig._top_answers):
            self.Log._warning("grabHotList error,id:%s" % topicId)
            return False

        return True

    # 等待回答
    def grabUnanswerList(self, topicId):
        self.Log._notice("Start to grab Unanswer activity,id:%s" % topicId)
        if False == self.handle(topicId, zhihuConfig._unanswered):
            self.Log._warning("grabHotList error,id:%s" % topicId)
            return False

        return True

    def handle(self, topicId, attr):
        url = zhihuConfig().getFeedsUrl(topicId, attr)
        param = zhihuConfig._include_param
        param['offset'] = 0
        param['limit'] = 10
        requestURL = "%s?%s" % (url, urllib.urlencode(param))

        try:
            while True:
                self.Log._notice("Start to grab url:%s" % requestURL)

                request = urllib2.Request(requestURL)
                response = urllib2.urlopen(request)
                response = response.read().decode('utf-8')
                result = json.loads(response)
                if result['paging']['is_end'] == True:
                    return True

                now = int(time.time())
                updateField = {
                    "update_time" : now
                }

                questionQueue = []
                data = result['data']
                for ele in data:
                    # 问答
                    singleQuestionQueue = {
                        "attached_info" : ele['attached_info'],
                        "topic_id"      : topicId,
                        "type"          : ele['type'],
                        "comment_count" : ele['target']['comment_count'],
                        "common_json"   : json.dumps(ele),
                        "add_time"      : now,
                    }
                    if ele['target'].has_key("question"):
                        singleQuestionQueue['title'] = ele['target']['question']['title']
                    else:
                        singleQuestionQueue['title'] = ele['target']['title']
                    if ele['target'].has_key('voteup_count'):
                        singleQuestionQueue['voteup_count'] = ele['target']['voteup_count']
                    else:
                        singleQuestionQueue['voteup_count'] = 0
                    if ele['target'].has_key('content'):
                        singleQuestionQueue['content'] = ele['target']['content']
                    else:
                        singleQuestionQueue['content'] = ""
                    questionQueue.append(singleQuestionQueue)

                    # 用户
                    if ele['target'].has_key('author'):
                        author = ele['target']['author']
                        singleUserQueue = {
                            "userId"                :   author['id'],
                            "name"                  :   author['name'],
                            "avatar_url"            :   author['avatar_url'],
                            "avatar_url_template"   :   author['avatar_url_template'],
                            "gender"                :   author['gender'],
                            "headline"              :   author['headline'],
                            "is_advertiser"         :   Libs().isset(author['is_advertiser'], 1, 0),
                            "is_org"                :   Libs().isset(author['is_org'], 1, 0),
                            "type"                  :   author['type'],
                            "user_type"             :   author['user_type'],
                            "url_token"             :   author['url_token'],
                            "badge"                 :   json.dumps(author['badge']),
                            "edu_member_tag"        :   json.dumps(author['edu_member_tag']),
                            "add_time"              :   now
                        }
                        if False == self.userDao._batchInsertByShardingParam(author['id'], [singleUserQueue], updateField):
                            self.Log._fatal("batch insert user error,sql:%s" % self.userDao._getLastSql())
                            return False

                if questionQueue and False == self.questionDao._batchInsertByShardingParam(topicId, questionQueue, updateField):
                    self.Log._fatal("batch insert question error,sql:%s" % self.questionDao._getLastSql())
                    return False

                requestURL = result['paging']['next']

        except Exception as e:
            self.Log._fatal("Handle Error,Except:%s" % e)
            return False




