# -*- coding: UTF-8 -*-

class Libs:

    #  Return the values from a single column in the input list
    def array_column(self, list = [], column = "", index = ""):
        if not list:
            raise Exception("list is empty")

        if not isinstance(column, str):
            raise Exception("column must be string")

        try:
            array = []
            for ele in list:
                if not index:
                    array.append(ele[column])
                else:
                    dic = {ele[index]: ele[column]}
                    array.append(dic)

            return array
        except Exception as e:
            raise Exception(e)


    """
    Return first list ele
    """
    def current(self, list):
        if list[0]:
            return list[0]

        return ""

    """
    Default
    """
    def isset(self, value, firstChoose, secondChose):
        if value:
            return firstChoose

        return secondChose



