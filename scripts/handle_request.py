import requests
import json


class HandleRequest:
    def __init__(self):
        self.one_session = requests.session()

    def common_head(self, myhead):
        self.one_session.headers.update(myhead)

    def send(self, url, method='post', data=None, is_json=True, **kwargs):
        if isinstance(data, str):
            try:
                data = json.loads(data)
            except Exception as n:
                data = eval(data)

        method = method.lower()
        if method == 'get':
            my_result = self.one_session.request(method=method, url=url, params=data, **kwargs)
        elif method in ('post', 'delete', 'put', 'patch'):
            if is_json:
                my_result = self.one_session.request(method=method, url=url, json=data, **kwargs)
            else:
                my_result = self.one_session.request(method=method, url=url, data=data, **kwargs)
        else:
            my_result = None
            print(f'此方法：{method}不存在')
        return my_result

    def close(self):
        self.one_session.close()


if __name__ == '__main__':
    url = 'http://api.lemonban.com/futureloan/member/register'
    params = "{'mobile_phone' : '13900001003','pwd' : '12345678'}"
    heads = {
        'X-Lemonban-Media-Type': 'lemonban.v2'
    }
    mr = HandleRequest()
    mr.common_head(heads)
    res = mr.send(url, data=params)
