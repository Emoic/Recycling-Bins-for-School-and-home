#coding:utf-8
import sys
import os
reload(sys)
sys.setdefaultencoding('utf8')
import pygame

from aip import AipImageClassify
from picamera import PiCamera
from playsound import playsound
import RPi.GPIO as GPIO
import time
import json

APP_ID = '20457028'
API_KEY = 'HEPzpDvjK1DrEte0TRjER2UR'
SECRECT_KEY = 'qDIRA2mAL4yM7xeZPXqnvHfAXnWeSuWM'

cilent = AipImageClassify(APP_ID, API_KEY, SECRECT_KEY)
dis = 20
waitingInput = False	
inputKey = 4

camera = PiCamera()

GPIO.setmode(GPIO.BCM)

ServoPin1 = 21
ServoPin2 = 20
PWMFreq = 50
Trig_Pin = 4
Echo_Pin = 25
btn_1 = 27#yellow
btn_0 = 18#green
btn_3 = 16#red
btn_2 = 5
LED_0 = 6
LED_1 = 13
LED_2 = 19
LED_3 = 26
GPIO.setup(ServoPin1, GPIO.OUT)
GPIO.setup(ServoPin2, GPIO.OUT)

GPIO.setup(Trig_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Echo_Pin, GPIO.IN)

GPIO.setup(btn_0, GPIO.IN)
GPIO.setup(btn_1, GPIO.IN)
GPIO.setup(btn_2, GPIO.IN)
GPIO.setup(btn_3, GPIO.IN)

GPIO.setup(LED_0, GPIO.OUT)
GPIO.setup(LED_1, GPIO.OUT)
GPIO.setup(LED_2, GPIO.OUT)
GPIO.setup(LED_3, GPIO.OUT)

pwm1 = GPIO.PWM(ServoPin1, PWMFreq)
pwm2 = GPIO.PWM(ServoPin2, PWMFreq)

pygame.mixer.init()

#camera function
def getImage():
    #set the resolution of picture, smaller means fatster upload but bad accuracy
    camera.resolution = (1024,768)
    #begin shoot
    camera.start_preview()	
    print ('/->:Shooting image')
    #wait 2 sce to ensure camera have a good condition
    time.sleep(2)
    #shoot and storage
    camera.capture('Image.jpg')	
    time.sleep(2)
    print ('/->:Shoot successful')

#request baidu server
def apiRequest(image):
    #upload picture to baidu's server with application object
    print ('/->:Uploading image to server')
    returnedResult = cilent.advancedGeneral(image)
    print ('/->:Returing results')
    #build stander json format 
    json_str = json.dumps(returnedResult)
    #load json inmormation to memory
    jsonResult = json.loads(json_str)
    #decode jason and pick what we need
    result = jsonResult['result'][0]['keyword']
    return result

#trash classify list
def trashList(result):
    if result == '纸巾':
        return 0
    elif result == '餐巾纸':
        return 1
    elif result == '怡宝矿泉水':
        return 2
    elif result == '电池':
        return 3
    elif result == '模糊图像':
        return err('SRY, picture is not good enough to distinguish, plz try again!')
    #if trash didnt list upown, it will be classified in TYPE 2 
    else:
        return 1

#Print error message and exit function or application        
def err(err_msg):
    print ('\033[1;30;41m!!!!!!!!WARNING!!!!!!!!\033[0m')
    print (err_msg)
    print ('\033[1;30;41m!!!!!!!!!!!!!!!!!!!!!!!\033[0m')
    #print ('/->:Exiting function!')


def trashClassify():
    print('/->:Preparp tp distinguish')
    getImage()
    img = open('Image.jpg', 'rb').read()
    result = apiRequest(img)
    trash_type = trashList(result)
    print ('==========')
    print ('/->:This is :')
    print (result)
    print ('==========')
    print ('/->:Type is :')
    print (trash_type)
    print ('==========')
    #print ('/->:Finish!')
    return trash_type

#电机姿态控制
def motorCtrl(duty1, duty2):
    pwm2.ChangeDutyCycle(duty2)
    time.sleep(1)
    pwm1.ChangeDutyCycle(duty1)
    time.sleep(2)
    pwm1.ChangeDutyCycle(8.1)
    pwm2.ChangeDutyCycle(7)

#按照分类扔垃圾
def trashThrow(trash_type):
            pwm1.start(0)
            pwm2.start(0)
            pwm1.ChangeDutyCycle(8.1)
            pwm2.ChangeDutyCycle(7)
            if trash_type == 0:
               duty1 = 10.3
               duty2 = 8.4
               pwm1.ChangeDutyCycle(duty1)
               pwm2.ChangeDutyCycle(duty2)
               time.sleep(2)
               pwm1.ChangeDutyCycle(7.8)
               pwm2.ChangeDutyCycle(8.4)
            if trash_type == 1:
               duty1 = 5.3
               duty2 = 3.7
               pwm2.ChangeDutyCycle(duty2)
               time.sleep(1)
               pwm1.ChangeDutyCycle(duty1)
               time.sleep(2)
               pwm1.ChangeDutyCycle(7.8)
               pwm2.ChangeDutyCycle(8.4)
            if trash_type == 2:
               duty2 = 3.7
               duty1 = 11.3
               pwm2.ChangeDutyCycle(duty2)
               time.sleep(1)
               pwm1.ChangeDutyCycle(duty1)
               time.sleep(2)
               pwm1.ChangeDutyCycle(7.8)
               pwm2.ChangeDutyCycle(8.4)
            if trash_type == 3:
               duty2 = 8.4
               duty1 = 4
              
               pwm2.ChangeDutyCycle(duty2)
               pwm1.ChangeDutyCycle(duty1)
               time.sleep(2)
               pwm1.ChangeDutyCycle(7.8)
               pwm2.ChangeDutyCycle(8.4)

#获取距离
def getDistance():
    GPIO.output(Trig_Pin, GPIO.HIGH)
    time.sleep(0.00015)
    GPIO.output(Trig_Pin, GPIO.LOW)
    while not GPIO.input(Echo_Pin):
        pass
    t1 = time.time()
    while GPIO.input(Echo_Pin):
        pass
    t2 = time.time()
    return (t2 - t1) * 340 * 100 / 2
    
#用户输入状况判断
def usrInput():
    if GPIO.input(btn_0):
        return 0
    elif GPIO.input(btn_1):
        return 1
    elif GPIO.input(btn_2):
        return 2
    elif GPIO.input(btn_3):
        return 3
    #等待输入状态
    else:
        return 4
        
#验证输入对错
def compareInput(trash_type):
    if trash_type == usrInput():
        return True
    elif trash_type != usrInput():
        return False

#led控制 第一个参数为灯号 第二个参数控制开关（1为开，0为关）
def ledCtrl(trash_type, ctrl):
    if trash_type == 0 and ctrl == 1:
        GPIO.output(LED_0, GPIO.HIGH)
    elif trash_type == 1 and ctrl == 1:
        GPIO.output(LED_1, GPIO.HIGH)
    elif trash_type == 2 and ctrl == 1:
        GPIO.output(LED_2, GPIO.HIGH)
    elif trash_type == 3 and ctrl == 1:
        GPIO.output(LED_3, GPIO.HIGH)
    elif trash_type == 0 and ctrl == 0:
        GPIO.output(LED_0, GPIO.LOW)
    elif trash_type == 1 and ctrl == 0:
        GPIO.output(LED_1, GPIO.LOW)
    elif trash_type == 2 and ctrl == 0:
        GPIO.output(LED_2, GPIO.LOW)
    elif trash_type == 3 and ctrl == 0:
        GPIO.output(LED_3, GPIO.LOW)

#音乐播放控制
def musicCtrl(ans):
    if ans == 'wrong':
        pygame.mixer.music.load("3.mp3")#错误播放的语音
    elif ans == 'right':
        pygame.mixer.music.load("4.mp3")#正确播放的语音
    elif ans == 'wait':
        pygame.mixer.music.load("2.mp3")#等待用户输入的语音
    pygame.mixer.music.play()
    
#主函数
if __name__ == '__main__':
    try:
        while True:
            while dis > 18:
                dis = getDistance()
                time.sleep(0.3)
            
            if waitingInput == False:
                print ('/->:Trash has been putted in!')
                trash_type = trashClassify()
                musicCtrl('wait')
                #等待用户输入的语音放在这里
                waitingInput = True
                print ('/->:Waitting for user input......')
            elif waitingInput == True:
                while inputKey == 4:
                    inputKey = usrInput()
                print ('/->:Get users input successful!')
                if trash_type == inputKey:
                    musicCtrl('right')
                    print ('/->:User right!')
                    #正确播放的语音放在这里
                    pass
                else:
                    print ('/->:User wrong!')
                    musicCtrl('wrong')
                    #错误播放的语音放在这里
                    pass
                ledCtrl(trash_type, 1)
                trashThrow(trash_type)
                time.sleep(3)
                print ('/->:Throwing......')
                time.sleep(1)
                ledCtrl(trash_type, 0)
                print ('/->:Done')
                waitingInput = False
                dis = 20
                inputKey = 4
                print ('/->:This term wad Finished!')
                print ('/->:Sys Waitting for next term......')
            else:
                pass
    except KeyboardInterrupt:
        GPIO.cleanup()
