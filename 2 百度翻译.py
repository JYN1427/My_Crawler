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
            'Cookie': 'BIDUPSID=97EE93C0AC0066461A6BA5CDD7EDB8CF; PSTM=1602590428; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; __yjs_duid=1_76a9c4662136444ffdfa5ab9b98f91ba1617887653154; BAIDUID=75F0EB85A735E8BB1AE758C1DB443F30:FG=1; BDUSS=HhYSDlGQ2NTYkVzWHVPWDd1anJ-U2xFdmN4Y25SY2VmS2k1NEo0M2xLMmpTUk5pRUFBQUFBJCQAAAAAAAAAAAEAAADb~po5dGltZcTjtcTE0LqiTk4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKO862GjvOthR; BDUSS_BFESS=HhYSDlGQ2NTYkVzWHVPWDd1anJ-U2xFdmN4Y25SY2VmS2k1NEo0M2xLMmpTUk5pRUFBQUFBJCQAAAAAAAAAAAEAAADb~po5dGltZcTjtcTE0LqiTk4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKO862GjvOthR; H_WISE_SIDS=107318_110085_127969_131861_176399_179350_184716_185268_185635_186844_188332_189037_189326_189755_190247_190798_191068_191245_191287_192206_192385_192957_193283_193291_193559_194085_194520_194604_195003_195016_195329_195343_195631_196046_196427_196527_197241_197286_197469_197472_197711_197783_197957_198033_198069_198078_198253_198446_198515_198650_199082_199176_199305_199469_199582_199598_199752_200037_200127_200272_200349_200435_200445_200550_200744_200969_201055_201328_201358_201444_201518_201534_201576_201580_201599_201700_201734_201979_201995_202177_202179_202297_202554_202566_202867_202927_203071; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=35410_35702_35105_31660_35488_35775_34584_35490_35246_35802_35797_35316_26350_35746; BDSFRCVID=By4OJexroG0R276HpScBb4dYqAwed9vTDYrEOwXPsp3LGJLVgxpIEG0PtElln_8-ox8EogKK0mOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tbut_KDMJDK3j-_kh4nb-P4ObqKX5-RLf2Tm_p7F5l8-h4oODPJJXUv-0M79-47XLPjmLKQIbMjxOKQphPRRK-0H-4jBKxRyLm78bP3N3KJmqpC9bT3v5tDjBNru2-biWbRL2MbdJqvP_IoG2Mn8M4bb3qOpBtQmJeTxoUJ25DnJhbLGe6--DTc-jH_Dqbbfb-oKQJOS54ooqTrnhPF3K58FXP6-35KH3Kbw0pntWP3BHfQGh-TmqtrXQ4teWh37JDFeLb5v3nRzEJnV3h5n25_pQ-oxJpOi5JbMopvaBRcCepvvbURvD-ug3-AqBM5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-j5JIEVCI2tD_KhCvPMR-_5-LO5eT22jnzJjT9aJ5nJDonhCbR3P51hxIZefKJKpcDJD7j5DIaQpP-eCOu0xnv-xCnDJo-BTcMaHbzKl0MLpnYbb0xyn_VbM_J3MnMBMPjamOnaU5I3fAKftnOM46JehL3346-35543bRTLnLy5KJYMDFljTu2jTQBeU5eetjK2CntsJOOaCvBO-5Oy4oWK441DbKHt557-N7fMb_25UTaEt3Nb5r-3M04K4o9-hvT-54e2p3FBUQJJ-JVQft20b0khMvXy5kLa5-OKR7jWhk2Dq72y5jvQlRX5q79atTMfNTJ-qcH0KQpsIJM5-DWbT8IjHCDt5FjJbIqVbobHJoHjJbGq4bohjPY2HO9BtQO-DOxoU_-JKQ1qMOnL4KMbhFLLqJ-KTcqQgnkQq5vbMnmqPtRXMJkXhKs2h3A0x-jLTn4WnR8XKPVDPP9QtnJyUnQhtnnBT5i3H8HL4nv2JcJbM5m3x6qLTKkQN3T-PKO5bRu_CcJ-J8XMCDljj5P; BAIDUID_BFESS=75F0EB85A735E8BB1AE758C1DB443F30:FG=1; BDSFRCVID_BFESS=By4OJexroG0R276HpScBb4dYqAwed9vTDYrEOwXPsp3LGJLVgxpIEG0PtElln_8-ox8EogKK0mOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tbut_KDMJDK3j-_kh4nb-P4ObqKX5-RLf2Tm_p7F5l8-h4oODPJJXUv-0M79-47XLPjmLKQIbMjxOKQphPRRK-0H-4jBKxRyLm78bP3N3KJmqpC9bT3v5tDjBNru2-biWbRL2MbdJqvP_IoG2Mn8M4bb3qOpBtQmJeTxoUJ25DnJhbLGe6--DTc-jH_Dqbbfb-oKQJOS54ooqTrnhPF3K58FXP6-35KH3Kbw0pntWP3BHfQGh-TmqtrXQ4teWh37JDFeLb5v3nRzEJnV3h5n25_pQ-oxJpOi5JbMopvaBRcCepvvbURvD-ug3-AqBM5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-j5JIEVCI2tD_KhCvPMR-_5-LO5eT22jnzJjT9aJ5nJDonhCbR3P51hxIZefKJKpcDJD7j5DIaQpP-eCOu0xnv-xCnDJo-BTcMaHbzKl0MLpnYbb0xyn_VbM_J3MnMBMPjamOnaU5I3fAKftnOM46JehL3346-35543bRTLnLy5KJYMDFljTu2jTQBeU5eetjK2CntsJOOaCvBO-5Oy4oWK441DbKHt557-N7fMb_25UTaEt3Nb5r-3M04K4o9-hvT-54e2p3FBUQJJ-JVQft20b0khMvXy5kLa5-OKR7jWhk2Dq72y5jvQlRX5q79atTMfNTJ-qcH0KQpsIJM5-DWbT8IjHCDt5FjJbIqVbobHJoHjJbGq4bohjPY2HO9BtQO-DOxoU_-JKQ1qMOnL4KMbhFLLqJ-KTcqQgnkQq5vbMnmqPtRXMJkXhKs2h3A0x-jLTn4WnR8XKPVDPP9QtnJyUnQhtnnBT5i3H8HL4nv2JcJbM5m3x6qLTKkQN3T-PKO5bRu_CcJ-J8XMCDljj5P; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1644029014; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1644029014; APPGUIDE_10_0_2=1; ab_sr=1.0.1_MTY2NThhZTAyM2Y0ODVmNTMzNmUyYTljN2E3MGU4NzUzN2NhY2JiNWU1NmQ1YWI5MWIxMzU0Y2UyYjhiNmFlNmZjMDY5NmRiMTU0ZTQxMDNmYmRlOTUyYjNkOTc4YTZmZjc3NDI0ZDQ1Yzg0YWU4OWVlZTg1ZmI1M2ZjZGUzM2I='

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
