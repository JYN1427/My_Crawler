import requests
import json


class douban_movie:
    # 获取所有电影信息
    def batch_obtain(self, num):
        data_list = []
        for i in range(0, num, 20):
            data_list += [self.get_movie_info(i)]
        return data_list

    # 仅获取电影名称
    def get_names(self, num):
        data_list = self.batch_obtain(num)
        res = []
        for data in data_list:
            for x in data["subjects"]:
                res.append(x["title"])
        return res

    # 发起请求
    def get_movie_info(self, index):
        url = 'https://movie.douban.com/j/search_subjects'
        params = {
            'type': 'movie',
            'tag': '豆瓣高分',
            'sort': 'recommend',
            'page_limit': '20', # 每页显示
            'page_start': str(index),  # 起始号
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',
        }
        response = requests.get(url=url, params=params, headers=headers)

        return response.json()


        '''
        f = open('./download files/douban.json', 'w', encoding='utf-8')
        json.dump(list_data, fp=f, ensure_ascii=False)
        
        >>> print json.dumps('中国')
        "\u4e2d\u56fd"
         
        输出的会是'中国' 的ascii 字符码，而不是真正的中文。
         
        这是因为json.dumps 序列化时对中文默认使用的ascii编码.想输出真正的中文需要指定ensure_ascii=False
        '''


if __name__ == '__main__':
    d = douban_movie()
    res = d.get_names(110)
    print(res)