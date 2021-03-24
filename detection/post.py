import urllib3,base64
import json

#params = "{\"text\":\"西瓜\"}"

def class_trash():
    request_url = 'https://aip.baidubce.com/rpc/2.0/ai_custom/v1/classification/camerawater'
    access_token = '24.1ed3321f16a6cc66861ef48cbcd9beb5.2592000.1575776760.282335-17363427'
    url = request_url + "?access_token=" + access_token
    http = urllib3.PoolManager()
    f = open('m2.jpg', 'rb')
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
    print(results)

class_trash()

#strtext="{'text':"+ss+",'top_num':1}"
# strtext={'text':ss,'top_num':1}
# print(strtext)
# strtext=eval(strtext)
# print(strtext)

