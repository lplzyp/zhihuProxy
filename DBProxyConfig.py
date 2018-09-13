# -*- coding: UTF-8 -*-
class DBProxyConfig:
    _DBProxyServer = {
        "default": {
            "username"          : "root",
            "password"          : "root",
            "host"              : "127.0.0.1",
            "port"              : 3306,
            "connect_timeout"   : 5,
            "read_timeout"      : 5,
            "write_timeout"     : 5,
            "charset"           : "utf8"
        }
    }

    def getConfig(self, index = 'default'):
        try:
            return self._DBProxyServer[index]

        except Exception as e:
            print "Search database proxy config error, current index is %s, error:%s" % (index, e)