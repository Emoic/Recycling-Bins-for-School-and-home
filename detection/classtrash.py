import wavrecord
import robor
import ttsp
import post

wavrecord.my_record('people_speak.pcm')             #录制音频（人）
wavrecord.play('people_speak.pcm')                  #播放音频（人）
text=robor.output_txt('people_speak.pcm')           #音频转文字
text=str(text['result'][0])                         #从字典中提取需要结果，转成字符格式
print('text',text)
post_test="\'"+text+"\'"
print(post_test)
results,score=post.class_trash(post_test)
if float(score)>0.5:
    if results=='other':
        resultd='其他垃圾'
    elif results=='kitchen':
        resultd = '厨余垃圾'
    elif results=='poison':
        resultd = '有毒垃圾'
    elif results=='recycle':
        resultd = '可回收垃圾'
    ttsp.text_to_speak(resultd, 'robot_speak.mp3')
else:
    ttsp.text_to_speak('无法准确区分该垃圾种类', 'robot_speak.mp3')
wavrecord.changefromt('robot_speak.mp3','robot_speak.wav')
wavrecord.play('robot_speak.wav')
