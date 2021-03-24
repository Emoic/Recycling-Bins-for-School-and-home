from aip import AipSpeech
import os
""" 你的 APPID AK SK """
APP_ID = '17354277'
API_KEY = 'S9uM9eztVfUfN2AMhcH0ZVfu'
SECRET_KEY = 'RzoZHOnumiFgpG8VTQdRdG8GBRC8aWqO'
def text_to_speak(text,file_name):
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    result  = client.synthesis(text, 'zh', 3, {
        'vol': 4,'per':0,'spd':3
    })

    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open(file_name, 'wb') as f:
            f.write(result)
