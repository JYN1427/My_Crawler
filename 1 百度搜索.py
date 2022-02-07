import requests

class Baidu_search:
    def keyword(self, keyword):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
        }
        url = 'https://www.baidu.com/s'
        params = {
            'ie': 'utf-8',
            'wd': keyword
        }
        response = requests.get(url=url, params=params, headers=headers)
        return response.status_code, response.headers



if __name__ == '__main__':
    b = Baidu_search()
    code, head = b.keyword('王者荣耀')
    print(code)
    print(head)
