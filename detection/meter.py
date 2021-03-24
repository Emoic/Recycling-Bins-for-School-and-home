import urllib.request
import urllib3, json, base64
#import pycocotools.mask as mask_util
import numpy as np
# request_url = 'https://aip.baidubce.com/rpc/2.0/ai_custom/v1/text_cls/lucastrash'
access_token ='24.13a22b45be1aff2066e86169416cee9b.2592000.1572178180.282335-17363427'

http=urllib3.PoolManager()
url='https://aip.baidubce.com/rpc/2.0/ai_custom/v1/segmentation/lucasmeter?access_token='+access_token
f = open('m1.jpg','rb')
#参数image：图像base64编码 以及top_num参数
img = base64.b64encode(f.read())
print(img)
#img参数进行一下str转换
params={'image':''+str(img,'utf-8')+'','top_num':5}
#对参数params数据进行json处理
encoded_data = json.dumps(params).encode('utf-8')
print(encoded_data)
print('***************************')

request=http.request('POST',
                      url,
                      body=encoded_data,
                      headers={'Content-Type':'application/json'})
#对返回的byte字节进行处理。Python3输出位串，而不是可读的字符串，需要进行转换
result = str(request.data,'utf-8')
print(result)