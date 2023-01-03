

class XdclassTestCase:

    def loadAllCaseByApp(self,app):
        """
        根据APP来加载所有测试用例
        :param app:
        :return:
        """
        print("loadAllCaseByApp")

    def findCaseById(self,case_id):
        """
        通过id找测试用例
        :param case_id:
        :return:
        """
        print("findCaseById")

    def loadConfigByAppAndKey(self,app,key):
        """
        通过APP 和 key 来加载配置文件
        :param app:
        :param key:
        :return:
        """
        print("loadConfigByAppAndKey")

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