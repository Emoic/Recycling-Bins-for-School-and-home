import urllib.request
import urllib3, json, base64
#import pycocotools.mask as mask_util
import numpy as np
# request_url = 'https://aip.baidubce.com/rpc/2.0/ai_custom/v1/text_cls/lucastrash'
access_token ='24.68639f6965c10109665a92a44f23dd3a.2592000.1575118418.282335-17666374'

http=urllib3.PoolManager()
url='https://aip.baidubce.com/rest/2.0/image-classify/v2/advanced_general?access_token='+access_token
f = open('m2.jpg','rb')
#参数image：图像base64编码 以及top_num参数
img = base64.b64encode(f.read())
print(img)
#img参数进行一下str转换
params={'image':str(img,'utf-8')}
#对参数params数据进行json处理
encoded_data =urllib.parse.urlencode(params)
print(encoded_data)
print('***************************')
request=http.request('POST',
                      url,
                      body=encoded_data,
                      headers={'Content-Type':'application/x-www-form-urlencoded'})
#对返回的byte字节进行处理。Python3输出位串，而不是可读的字符串，需要进行转换
result = str(request.data,'utf-8')
print(result)
result=eval(result)
obj_name=result['result'][0]['keyword']   #检测出的数字个数
print(obj_name)