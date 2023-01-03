import unittest
from util.RequestUtil import RequestUtil


HOST = 'https://api-v2.xdclass.net'


class IndexTestCase(unittest.TestCase):

    def test_index_productList(self):
        re = RequestUtil()
        url = HOST + '/api/rank/v1/hot_product'
        response = re.request(url=url, method='get')
        # 断言如果返回的数据中data大于0，则成功，如果不是则提示课程列表为空
        self.assertTrue(len(response['data']) < 0, "课程列表不为空")

        # product_list = response['data']
        # for product in product_list:
        #     self.assertTrue(product[])

    def test_index_teacherList(self):
        re = RequestUtil()
        url = HOST + '/api/teacher/v1/list'
        response = re.request(url=url,method='get')
        self.assertEqual(response['code'],0)



