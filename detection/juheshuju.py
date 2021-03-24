import urllib.parse
import urllib.request
import base64
import urllib3
import json
http=urllib3.PoolManager()
def rubbish_search():
    url = 'http://apis.juhe.cn/rubbish/search'
    appkey = "c828134bacf94db8296b579e017916cc"
    params = {
            "key": appkey,
            "q": "苹果",
            "type":2,
            }

    textmod = urllib.parse.urlencode(params)
    print(textmod)
    req = urllib.request.Request(url='%s%s%s' % (url, '?', textmod))
    res = urllib.request.urlopen(req)
    res = res.read()
    res=res.decode(encoding='utf-8')
    #res= {"reason": "success", "result": [{"id": "2796", "itemName": "苹果", "itemCategory": "湿垃圾"}], "error_code": 0}
    print('dd',res)
    l_name=eval(res)['result'][0]['itemName']
    l_itemCategory=eval(res)['result'][0]['itemCategory']
    print(l_name,l_itemCategory)
#rubbish_search()


def rubbish_img():
    url = 'http://apis.juhe.cn/voiceRubbish/imgDisti'
    appkey = "f9b8539d000f45d38f50ff717fbd7fc8"
    f = open('m2.jpg', 'rb')
    # 参数image：图像base64编码 以及top_num参数
    img = base64.b64encode(f.read())
    img= img.decode()
    print(img)
    params = {
            "key": appkey,
            "image": img,
            "type":2,
            }
    headers = {'content-type': "application/x-www-form-urlencoded"}
    textmod = urllib.parse.urlencode(params)
    print(textmod)
    req = http.request('POST',
                           url,
                           body=textmod,
                            headers=headers
                           )
    #req = urllib.request.Request(url='%s%s%s' % (url, '?', textmod))
    print(req.data)
    result = str(req.data,'utf-8')
    print('a',result)
    # res = urllib.request.urlopen(req)
    # res = res.read()
    dict = json.loads(result)
    l_score=dict['result'][0]['score']
    l_name=dict['result'][0]['list'][0]['itemName']
    l_itemCategory=dict['result'][0]['list'][0]['itemCategory']
    print(l_score)
    print(l_name)
    print(l_itemCategory)
#rubbish_search()
rubbish_img()