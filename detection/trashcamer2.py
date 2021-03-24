# -*- coding: utf-8-*-

import os
from robot import config, constants, logging
from robot.sdk.AbstractPlugin import AbstractPlugin
import urllib.request
import urllib3, json, base64
access_token ="24.4e4dec0f353ab9ab8aabf26d1ce82bd3.2592000.1575372626.282335-17363427"
url='https://aip.baidubce.com/rest/2.0/image-classify/v2/advanced_general?access_token='+access_token

class Plugin(AbstractPlugin):
    def suggest(self,results,score):
        profile = config.get()
        suggestion = profile[self.SLUG]['suggestion']
        if float(score) > 0.4:
            if results == 'other':
                if(suggestion):
                    self.say(' 干垃圾，请尽量沥干水分；难以辨别的生活垃圾应投入干垃圾容器内', cache=True)
                else:
                    self.say('干垃圾', cache=True)
            elif results == 'kitchen':
                if (suggestion):
                    self.say(' 湿垃圾，餐厨垃圾应沥干水分后再投放，有包装物的应取出后分类投放', cache=True)
                else:
                    self.say(' 湿垃圾', cache=True)
            elif results == 'poison':
                if (suggestion):
                    self.say(' 有毒垃圾，请注意轻放，易破损易挥发的，应该做好密封或封装处理', cache=True)
                else:
                    self.say(' 有毒垃圾', cache=True)
            elif results == 'recycle':
                if(suggestion):
                    self.say(' 可回收垃圾，请轻投轻放；注意清洁干燥，避免污染；废纸尽量平整', cache=True)
                else:
                    self.say(' 可回收垃圾', cache=True)
        else:

            self.say('不好意思，我还不知道它的类别', cache=True)


    def handle(self,parsed):
        cmd = "fswebcam --no-banner -S 1 -r 320x240 image.jpg"
        os.system(cmd)
        http = urllib3.PoolManager()
        f = open('image.jpg', 'rb')
        # 参数image：图像base64编码 以及top_num参数
        img = base64.b64encode(f.read())
        # 对参数params数据进行json处理
        params = {'image': str(img, 'utf-8'), "top_num": 1}
        encoded_data = json.dumps(params).encode('utf-8')
        request = http.request('POST',
                               url,
                               body=encoded_data,
                               headers={"Content-Type": "application/json"})
        resultdata = str(request.data, 'utf-8')
        results = eval(resultdata)
        obj_name = results["results"][0]["name"]
        obj_score = results["results"][0]["score"]
        print(obj_name, obj_score)
        self.say("识别物品为" + obj_name, cache=False)
        self.suggest(obj_name,obj_score)
    def isValid(self, text, parsed):
        return any(word in text for word in [u"模式二"])


