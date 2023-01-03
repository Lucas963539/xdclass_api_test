import unittest
from util.RequestUtil import RequestUtil
class LoginTestCase(unittest.TestCase):

    def test_login(self):
        login_url = 'https://api-v2.xdclass.net/api/account/v1/login'
        param = {"identifier":"18723132997","credential":"jc18723132997"}
        re = RequestUtil()
        response = re.request(url=login_url,method='post',param=param,content_type='application/json')
        self.assertEqual(response['code'], 0)