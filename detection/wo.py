# -*- coding: utf-8-*-
import urllib3
import json
import requests
from robot import config, logging
from robot.sdk.AbstractPlugin import AbstractPlugin


class Plugin(AbstractPlugin):
    SLUG="sortrash"
    #返回 垃圾名字
    def getname(self, text):
        trashname = text.replace('什么', '').replace('垃圾', '').replace('是', '')
        return trashname

    # 返回（类别，概率）
    def class_trash(self,params):
        params = "\'" + params + "\'"
        request_url = 'https://aip.baidubce.com/rpc/2.0/ai_custom/v1/text_cls/lucastrash1'
        access_token = '24.9fc9c86e121f8de09ea1ea094fcb1250.2592000.1575109966.282335-17363427'
        url = request_url + "?access_token=" + access_token
        http = urllib3.PoolManager()
        params = {'text': params, 'top_num': 1}
        params = json.dumps(params).encode('utf-8')
        print(params)
        request = http.request('POST',
                               url,
                               body=params,
                               headers={'Content-Type': 'application/json'})
        # 对返回的byte字节进行处理。Python3输出位串，而不是可读的字符串，需要进行转换
        print(request.data)
        result = str(request.data, 'utf-8')
        results = eval(result)['results'][0]['name']
        score = eval(result)['results'][0]['score']
        print(results, score)
        return results, score


    def handle(self, text, parsed):
        trashname=self.getname(text)
        results,score=self.class_trash(trashname)
        if float(score) > 0.4:
            if results == 'other':
                self.say(' 干垃圾，请尽量沥干水分；难以辨别的生活垃圾应投入干垃圾容器内', cache=True)
            elif results == 'kitchen':
                self.say(' 湿垃圾，餐厨垃圾应沥干水分后再投放，有包装物的应取出后分类投放', cache=True)
            elif results == 'poison':
                self.say(' 有毒垃圾，请注意轻放，易破损易挥发的，应该做好密封或封装处理', cache=True)
            elif results == 'recycle':
                self.say(' 可回收垃圾，请轻投轻放；注意清洁干燥，避免污染；废纸尽量平整；立体包装物请清空内容物，清洁后压扁投放；有尖锐边角的，应包裹后投放', cache=True)
        else:

            self.say('不好意思，我还不知道它的类别', cache=True)

    def isValid(self, text, parsed):
        return any(word in text for word in [u"垃圾", u"是什么垃圾", u"什么垃圾"])
