# -*- coding: UTF-8 -*-
import os, sys
import platform
import datetime

"""
日志控制类
"""
class logHandler:

    # 日志路径
    log         = ""

    # 不同系统间的换行符
    lineBreak   = ""

    def __init__(self, log):
        if not log:
            raise Exception("log path is empty")

        if not os.path.exists(log):
            os.mkdir(log)

        if not os.access(log, os.R_OK | os.W_OK):
            os.chmod(log, '0777')

        self.log = log
        self._setLineBreak()

    def _notice(self, msg):
        level = "NOTICE"
        self._write(msg, level)

    def _warning(self, msg):
        level = "WARNING"
        self._write(msg, level)

    def _fatal(self, msg):
        level = "FATAL"
        self._write(msg, level)

    def _write(self, msg, level):
        try:
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            str = "%s: %s: %s %s" % (level, now, msg, self.lineBreak)
            handle = open(self.log, "a+")
            handle.write(str)
            handle.close()
        except Exception as e:
            raise Exception("write log error,result:%s" % e)

    def _setLineBreak(self):
        system = platform.system()
        if system == "Windows":
            self.lineBreak = "\n"
        else:
            self.lineBreak = "\r\n"

