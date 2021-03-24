# -*- coding: utf-8-*-

import os
from robot import config, constants, logging
from robot.sdk.AbstractPlugin import AbstractPlugin
import urllib.request
import urllib3, json, base64

access_token ='24.68639f6965c10109665a92a44f23dd3a.2592000.1575118418.282335-17666374'
url='https://aip.baidubce.com/rest/2.0/image-classify/v2/advanced_general?access_token='+access_token

class Plugin(AbstractPlugin):

    SLUG = "trashcamer"
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
    def suggest(self,name):
        results,score=self.class_trash(name)
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


    def handle(self,text,parsed):
        cmd = "fswebcam --no-banner -S 1 -r 320x240 image.jpg"
        os.system(cmd)
        http = urllib3.PoolManager()
        f = open('image.jpg', 'rb')
        # 参数image：图像base64编码 以及top_num参数
        img = base64.b64encode(f.read())
        # img参数进行一下str转换
        params = {'image': str(img, 'utf-8')}
        # 对参数params数据进行json处理
        encoded_data = urllib.parse.urlencode(params)
        request = http.request('POST',
                               url,
                               body=encoded_data,
                               headers={'Content-Type': 'application/x-www-form-urlencoded'})
        result = str(request.data, 'utf-8')
        result = eval(result)
        obj_name = result['result'][0]['keyword']  # 检测出的数字个数
        print(obj_name)
        self.say("识别物品为" + obj_name, cache=False)

        self.suggest(obj_name)

    def isValid(self, text, parsed):
        return any(word in text for word in [u"智能分类模式"])

