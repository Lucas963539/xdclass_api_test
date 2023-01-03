from util.db_util import MySqlUtil


class XdclassTestCase:

    def loadAllCaseByApp(self,app):
        """
        根据APP来加载所有测试用例
        :param app:
        :return:
        """
        print("loadAllCaseByApp")
        my_db = MySqlUtil()
        sql = "select * from `case` where app='{0}'".format(app)
        results = my_db.query(sql)
        return results

    def findCaseById(self,case_id):
        """
        通过id找测试用例
        :param case_id:
        :return:
        """
        print("findCaseById")
        my_db = MySqlUtil()
        sql = "select * from `case` where id='{0}'".format(case_id)
        results = my_db.query(sql, state="one")
        return results

    def loadConfigByAppAndKey(self,app,key):
        """
        通过APP 和 key 来加载配置文件
        :param app:
        :param key:
        :return:
        """
        print("loadConfigByAppAndKey")
        my_db = MySqlUtil()
        sql = "select * from `config` where app='{0}' and dict_key='{1}'".format(app, key)
        results = my_db.query(sql, state="one")
        return results

    def updateResultByCaseId(self,response, is_pass, msg, case_id):
        """
        根据测试用例id，更新响应内容和测试内容
        :param response:
        :param is_pass:
        :param msg:
        :param case_id:
        :return:
        """
        print("updateResultByCaseId")

    def runAllCase(self,app):
        """
        执行全部用例
        :param app:
        :return:
        """
        print("runAllCase")

    def runCase(self):
        """
        执行单个用例
        :return:
        """
        print('runCase')