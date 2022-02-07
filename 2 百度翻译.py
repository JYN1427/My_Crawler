import requests
import json
import execjs

class Baidu_translate:
    def translate(self, query_string):
        # 1 设置url
        post_url = 'https://fanyi.baidu.com/v2transapi'

        # 2 设置headers，包含UA伪装
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',
            'Cookie': '...'
        }

        # 3 设置post携带参数
        sign = self.get_sign(query_string)
        print(sign)
        data = {
            'from': 'en',
            'to': 'zh',
            'query': query_string,
            'sign': sign,
            'token': '53f62f65dd97c6c6cfd0c8d38e777ab2',
        }

        # 4 发送请求
        response = requests.post(url=post_url, data=data, headers=headers)

        # 5 获取响应数据
        # json方法返回的是obj，如果确认响应的数据是json类型，才用
        return response.json()


    def get_sign(self, s):
        with open('./data/index.js') as f:
            JSdata = f.read()
        return execjs.compile(JSdata).call('e', s)


if __name__ == '__main__':
    b = Baidu_translate()
    res = b.translate('She is a beautiful girl')
    print(res)



