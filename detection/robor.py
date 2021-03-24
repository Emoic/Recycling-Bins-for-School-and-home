from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '17354277'
API_KEY = 'S9uM9eztVfUfN2AMhcH0ZVfu'
SECRET_KEY = 'RzoZHOnumiFgpG8VTQdRdG8GBRC8aWqO'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 识别本地文件
def output_txt(file_name):
    li=client.asr(get_file_content(file_name), 'pcm', 16000, {'dev_pid': 1536,})
    print(li)
    return li

