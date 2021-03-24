# -*- coding: utf-8-*-

import os
import urllib.request
import urllib3, json, base64
access_token2 ="24.6856a236614e7cdb8a0875e0779a03d6.2592000.1575371943.282335-17363427"
access_token ='24.68639f6965c10109665a92a44f23dd3a.2592000.1575118418.282335-17666374'
url='https://aip.baidubce.com/rpc/2.0/ai_custom_pro/v1/classification/pictrah?access_token='+access_token2

def handle():
    cmd = "fswebcam --no-banner -S 1 -r 320x240 image.jpg"
    os.system(cmd)
    http = urllib3.PoolManager()
    f = open('m3.jpg', 'rb')
    # 参数image：图像base64编码 以及top_num参数
    img = base64.b64encode(f.read())
    # img参数进行一下str转换
    params = {'image': str(img, 'utf-8'),"top_num":1}


    # 对参数params数据进行json处理
    encoded_data = json.dumps(params).encode('utf-8')
    request = http.request('POST',
                           url,
                           body=encoded_data,
                           headers={"Content-Type": "application/json"})
    print(request.data)
    result = str(request.data, 'utf-8')
    results = eval(result)
    obj_name=results["results"][0]["name"]
    obj_score=results["results"][0]["score"]
    print(obj_name,obj_score)


        # result = str(request.data, 'utf-8')
        # result = eval(result)
        # obj_name = result['result'][0]['keyword']  # 检测出的数字个数
        # print(obj_name)
        # say("识别物品为" + obj_name, cache=False)
        #
        # suggest(obj_name)
    #
    # def isValid(self, text, parsed):
    #     return any(word in text for word in [u"智能分类模式"])
    #
handle()