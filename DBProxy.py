# -*- coding: UTF-8 -*-
from DBProxyConfig import DBProxyConfig
import MySQLdb as mdb
import hashlib
from Libs import Libs

class DBProxy:
    _dbConnectConfig    = {}
    _tableName          = ""
    _dbName             = ""
    _connect            = ""
    _cursor             = ""
    _isCommit           = True
    _errorMsg           = ""
    _sql                = ""
    _tableNum           = 0

    """
    Initialize db proxy connect config
    """
    def __init__(self, index = 'default'):
        dbConfig = DBProxyConfig().getConfig(index)
        self._dbConnectConfig = dbConfig

    """
    Initialize table and database
    """
    def _setDB(self, dbName, tableName, tableNum = 0):
        self._dbName = dbName
        self._tableName = tableName
        self._tableNum = tableNum
        self._connectToDb()
        self._setCursor()
        self._autoCommit(True)

        return self

    """
    Insert dictionary data into table
    If autoCommit is false, you can execute _commit method to commit your sql finally
    """
    def _insert(self, record = {}):
        if not record:
            self._writeErrorMsg("insert record empty")
            return False

        try:
            fieldSql = "`" + "`,`".join(record.keys()) + "`"
            dataSql = '"' + '","'.join("%s" % str for str in record.values()) + '"'
            self._sql = "INSERT INTO %s (%s) VALUES (%s)" % (self._tableName, fieldSql, dataSql)
            self._cursor.execute(self._sql)
            if self._isCommit:
                self._connect.commit()

            return True
        except Exception as e:
            self._writeErrorMsg("insert error,except:%s,sql:%s" % (e, self._sql))
            return False

    """
    Batch insert dictionary data into table
    """
    def _batchInsert(self, record = [], update = []):
        try:
            if not record:
                self._writeErrorMsg("batch insert record empty")
                return False

            if not Libs().current(record):
                self._writeErrorMsg("batch insert empty")
                return False

            updateCond = ""
            if update:
                duplicateUpdateArr = []
                for f in update.keys():
                    duplicateUpdateArr.append('`%s` = "%s"' % (f, update[f]))
                updateCond = " ON DUPLICATE KEY UPDATE " + ",".join(duplicateUpdateArr)

            field = Libs().current(record).keys()
            dataList = []
            for i in range(len(record)):
                data = []
                for f in field:
                    value = self._connect.escape_string("%s" % record[i][f])
                    data.append(value)
                str = '("' + '","'.join(data) + '")'
                dataList.append(str)
            dataStr = ",".join(dataList)
            fieldSql = "`" + "`,`".join(field) + "`"

            self._sql = "INSERT INTO %s (%s) VALUES %s %s" % (self._tableName, fieldSql, dataStr, updateCond)
            self._cursor.execute(self._sql)
            if self._isCommit:
                self._connect.commit()

            return True
        except Exception as e:
            self._writeErrorMsg("batch insert error,except:%s,sql:%s" % (e, self._sql))
            return False

    """
    Batch insert dictionary data into sharding table
    """
    def _batchInsertByShardingParam(self, shardingParam, record = [], update = []):
        try:
            if not shardingParam:
                self._writeErrorMsg("batch insert sharding_param empty")

            if not record:
                self._writeErrorMsg("batch insert record empty")
                return False

            if not Libs().current(record):
                self._writeErrorMsg("batch insert empty")
                return False

            updateCond = ""
            if update:
                duplicateUpdateArr = []
                for f in update.keys():
                    duplicateUpdateArr.append('`%s` = "%s"' % (f, update[f]))
                updateCond = " ON DUPLICATE KEY UPDATE " + ",".join(duplicateUpdateArr)

            field = Libs().current(record).keys()
            dataList = []
            for i in range(len(record)):
                data = []
                for f in field:
                    value = self._connect.escape_string("%s" % record[i][f])
                    data.append(value)
                str = '("' + '","'.join(data) + '")'
                dataList.append(str)
            dataStr = ",".join(dataList)
            fieldSql = "`" + "`,`".join(field) + "`"

            self._sql = "INSERT INTO %s (%s) VALUES %s %s" % (self._getShardingTableName(shardingParam), fieldSql, dataStr, updateCond)
            self._cursor.execute(self._sql)
            if self._isCommit:
                self._connect.commit()

            return True
        except Exception as e:
            self._writeErrorMsg("batch insert error,except:%s,sql:%s" % (e, self._sql))
            return False

    """
    Update table
    """
    def _updateByCond(self, record = {}, cond = ""):
        if not record:
            self._writeErrorMsg("update param empty")
            return False

        try:
            where = ""
            if cond:
                where = "where %s" % cond
            list = []
            for key in record:
                list.append("`%s` = '%s'" % (key, record[key]))
            dataStr = ",".join(list)
            self._sql = "UPDATE %s SET %s %s" % (self._tableName, dataStr, where)
            self._cursor.execute(self._sql)
            if self._isCommit:
                self._connect.commit()

            return True
        except Exception as e:
            self._writeErrorMsg("_updateByCond error,except:%s,sql:%s" % (e, self._sql))
            return False

    """
    Delete data
    """
    def _delete(self, cond = ""):
        try:
            where = ""
            if cond:
                where = "where %s" % cond
            self._sql = "DELETE FROM %s %s" % (self._tableName, where)
            self._cursor.execute(self._sql)
            if self._isCommit:
                self._connect.commit()

            return True
        except Exception as e:
            self._writeErrorMsg("_delete error,except:%s,sql:%s" % (e, self._sql))
            return False

    """
    Get the selected data If set cond
    If page less than -1, the method will search all result
    """
    def _getByPage(self, columns = [], cond = "", page = 1, page_size = 10, orderby = "id", order = "desc"):
        column = "*"
        if columns:
            column = "`" + "`,`".join(columns) + "`"

        where = ""
        if cond:
            where = " WHERE %s" % cond

        limit = ""
        if page > 0:
            start = (page - 1) * page_size
            limit = "LIMIT %s,%s" % (start, page_size)

        try:
            self._sql = "SELECT %s FROM %s %s ORDER BY %s %s %s" % (column, self._tableName, where, orderby, order, limit)
            self._cursor.execute(self._sql)
            result = self._cursor.fetchall()

            return result
        except Exception as e:
            self._writeErrorMsg("_getByPage error,except:%s,sql:%s" % (e, self._sql))
            return False

    """
    Batch get data by sharding param 
    """
    def _getByPageByShardingParam(self, shardingParam, columns = [], cond = "", page = 1, page_size = 10, orderby = "id", order = "desc"):
        if not shardingParam:
            self._writeErrorMsg("_getByPageByShardingParam shardingParam empty")
            return False

        column = "*"
        if columns:
            column = "`" + "`,`".join(columns) + "`"

        where = ""
        if cond:
            where = " WHERE %s" % cond

        limit = ""
        if page > 0:
            start = (page - 1) * page_size
            limit = "LIMIT %s,%s" % (start, page_size)

        try:
            self._sql = "SELECT %s FROM %s %s ORDER BY %s %s %s" % (column, self._getShardingTableName(shardingParam), where, orderby, order, limit)
            self._cursor.execute(self._sql)
            result = self._cursor.fetchall()

            return result
        except Exception as e:
            self._writeErrorMsg("_getByPage error,except:%s,sql:%s" % (e, self._sql))
            return False

    """
    Return the db optional object
    """
    def _connectToDb(self):
        self._connect = mdb.connect(
            host = self._dbConnectConfig['host'],
            port = self._dbConnectConfig['port'],
            user = self._dbConnectConfig['username'],
            passwd = self._dbConnectConfig['password'],
            db = self._dbName,
            charset = self._dbConnectConfig['charset']
        )

        return self

    """
    Set if auto-commit while execute sql
    """
    def _autoCommit(self, bool = False):
        self._connect.autocommit(bool)
        self._isCommit = bool

        return self

    """
    If autoCommit is false, you must execute this finally
    """
    def _commit(self):
        self._connect.commit();

    """
    Set cursor while is empty
    """
    def _setCursor(self):
        self._cursor = self._connect.cursor()

        return self

    """
    Store exception error
    """
    def _writeErrorMsg(self, msg):
        self._errorMsg = msg

    """
    Read exception error
    """
    def _readErrorMsg(self):
        return self._errorMsg

    """
    Return last execute sql
    """
    def _getLastSql(self):
        return self._sql

    def _getShardingTableName(self, shardingParam):
        num = self._generateTableNum(shardingParam)
        tableName = "%s_%s" % (self._tableName, num)

        return tableName

    """
    Generate table suffix number
    """
    def _generateTableNum(self, shardingParam):
        md5 = self._generateSign(shardingParam)
        subSign = md5[-4:]
        subSign = int(subSign, 16)
        num = subSign % self._tableNum + 1

        return num

    """
    hash and Return the modified shardingParam 
    """
    def _generateSign(self, shardingParam):
        try:
            sign = "%s_md5" % shardingParam
            obj = hashlib.md5()
            obj.update(sign)
            md5 = obj.hexdigest()
            return md5
        except Exception as e:
            raise Exception(e)




