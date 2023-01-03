
import requests
class RequestUtil:

    def __init__(self):
        pass

    def request(self,url,method,headers=None,param=None,content_type=None):
        """
        通用请求工具类
        :param url:
        :param method:
        :param headers:
        :param param:
        :param content_type:
        :return:
        """
        try:
            if method == 'get':
                result = requests.get(url=url,headers=headers,params=param).json()
                return result
            elif method == 'post':
                if content_type == 'application/json':
                    result = requests.post(url=url,headers=headers,json=param).json()
                    return result
                else:
                    result = requests.post(url=url,headers=headers,data=param).json()
                    return result
            else:
                print('Http Request is not allowed')



        except Exception as e:
            print(f'HTTP请求异常，内容是{e}')

if __name__ == '__main__':
    # url='https://api-v2.xdclass.net/api/product/v1/detail'
    login_url = 'https://api-v2.xdclass.net/api/account/v1/login'
    info_url = 'https://api-v2.xdclass.net/api/account/v1/detai'
    param = {"identifier":"18723132997","credential":"jc18723132997"}
    content_type = 'application/json'
    re = RequestUtil()
    # response = re.request(url=url,method=method,param=param)

    headers = {"Content-Type":"application/json"}
    response = re.request(url=login_url,method='post',param=param,content_type=content_type)
    print(response)

    # headers = response.get('data')
    # print(headers)
    # user_info = re.request(url=info_url,headers=headers,method='get')
    # print(f'登录的用户信息是：{user_info}')