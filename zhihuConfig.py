# -*- coding: UTF-8 -*-
class zhihuConfig:
    # 爬取的主要入口
    _mainURL        = "https://www.zhihu.com/topics"

    # 获取话题接口
    _getTopicURL    = "https://www.zhihu.com/node/TopicsPlazzaListV2"

    # 话题链接
    _topicURL       = "https://www.zhihu.com/topic/{topic-id}"

    # 话题属性
    _hot            = "hot"                 # 讨论
    _index          = "index"               # 索引
    _top_answers    = "top-answers"         # 精华
    _unanswered     = "unanswered"          # 等待回答

    # 数据库
    _database       = "zhihu"

    # 数据表
    _topic          = "zhihu_topic"
    _squareTopic    = "zhihu_topic_square"
    _question       = "zhihu_question"
    _user           = "zhihu_user"

    # 分表量
    _question_num   = 100
    _user_num = 100

    # 日志
    _log            = "zhihu.log"

    # 请求头
    _header         = {
        'User-Agent'    : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
        'Referer'       : 'https://www.zhihu.com/topics',
        'accept'        : 'application/json, text/plain, */*',
    }

    _include_param = {
        "include" : "data[?(target.type=topic_sticky_module)].target.data[?(target.type=answer)].target.content,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp;data[?(target.type=topic_sticky_module)].target.data[?(target.type=answer)].target.is_normal,comment_count,voteup_count,content,relevant_info,excerpt.author.badge[?(type=best_answerer)].topics;data[?(target.type=topic_sticky_module)].target.data[?(target.type=article)].target.content,voteup_count,comment_count,voting,author.badge[?(type=best_answerer)].topics;data[?(target.type=topic_sticky_module)].target.data[?(target.type=people)].target.answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics;data[?(target.type=answer)].target.content,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp;data[?(target.type=answer)].target.author.badge[?(type=best_answerer)].topics;data[?(target.type=article)].target.content,author.badge[?(type=best_answerer)].topics;data[?(target.type=question)].target.comment_count",
    }

    _feed_url = "https://www.zhihu.com/api/v4/topics/{topic-id}/feeds/{flag}"
    _feed_url_map = {}

    def __init__(self):
        self._feed_url_map = {
            self._hot           : "top_activity",
            self._top_answers   : "essence",
            self._unanswered    : "top_question",
        }

    def getTopicURLById(self, id, attr):
        if not id:
            raise Exception("getTopicURLById id empty")

        url = self._topicURL.replace("{topic-id}", "%s" % id)
        url = "%s/%s" % (url, attr)

        return url

    def getFeedsUrl(self, id, attr):
        if not id:
            raise Exception("getFeedsUrl id empty")

        try:
            flag = self._feed_url_map[attr]
            url = self._feed_url.replace("{topic-id}", "%s" % id).replace("{flag}", '%s' % flag)
            return url
        except Exception as e:
            return False