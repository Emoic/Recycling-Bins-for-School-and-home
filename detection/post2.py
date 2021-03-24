# pires_in":2592000,"session_key":"9mzdDZNgR43o9IsvYYWgbdNCF+bXGUwf4esCeKz9HspiaM\/GtTBFdrdlJRi5OkLp+eQUw8rIGVfSKr3VteoQ4y\/otuO80Q==","access_token":"24.6ea48452f492350c288bbe7a1dc0b605.2592000.1572170875.282335-17354277","scope":"ai_custom_lucastrash audio_voice_assistant_get brain_enhanced_asr audio_tts_post public brain_all_scope picchain_test_picchain_api_scope wise_adapt lebo_resource_base lightservice_public hetu_basic lightcms_map_poi kaidian_kaidian ApsMisTest_Test\u6743\u9650 vis-classify_flower lpq_\u5f00\u653e cop_helloScope ApsMis_fangdi_permission smartapp_snsapi_base iop_autocar oauth_tp_app smartapp_smart_game_openapi oauth_sessionkey smartapp_swanid_verify smartapp_opensource_openapi smartapp_opensource_recapi fake_face_detect_\u5f00\u653eScope","session_secret":"ef30f838cfed9ebc1bcf92086fed75bf"}
# API_KEY = 'S9uM9eztVfUfN2AMhcH0ZVfu'
# SECRET_KEY = 'RzoZHOnumiFgpG8VTQdRdG8GBRC8aWqO'
# # client_id 为官网获取的AK， client_secret 为官网获取的SK
# host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='+API_KEY+'&client_secret='+SECRET_KEY
# print(host)
# {"refresh_token":"25.371ac439acb830ab90171154eaeb8194.315360000.1884938875.282335-17354277",
#  "ex
# import urllib.request
# from urllib import parse
'''
easydl文本分类
'''
#encoding:utf-8
# request_url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/text_cls/lucastrash"
# access_token = '[25.371ac439acb830ab90171154eaeb8194.315360000.1884938875.282335-17354277]'
#
# params = {"西瓜"}
# print(params)
#
# data = urllib.parse.urlencode(params).encode(encoding='UTF8')
#
# print(data)
# request_url = request_url + "?access_token=" + access_token
#
# mess = urllib.request.Request(url=request_url,data=params)
# mess.add_header('Content-Type', 'application/json')
# response =  urllib.request.urlopen(mess)
# content = response.read()
# if content:
#     print(content)

import urllib.request
import urllib, json, base64
request_url = 'https://aip.baidubce.com/rpc/2.0/ai_custom/v1/text_cls/lucastrash'
access_token ='24.6ea48452f492350c288bbe7a1dc0b605.2592000.1572170875.282335-17354277'

params={
    "text": "一个盆子",
    "top_num": 2
}
params = json.dumps(params).encode('utf-8')
print(params)
headers={'Content-Type':'application/json'}
request_url = request_url+"?access_token="+access_token
print('1',request_url)
mess=urllib.request.Request(url=request_url, headers=headers, data=params)
mess = urllib.request.urlopen(mess)
logInfo = mess.read().decode()
print(logInfo)


# mess = urllib.request.Request(url=request_url,data=params)
# print('2',mess)
# mess.add_header('Content-Type', 'application/json')
# print('3',mess)
#
# html = urllib.request.urlopen(mess).read().decode('utf-8')
# print(html)
