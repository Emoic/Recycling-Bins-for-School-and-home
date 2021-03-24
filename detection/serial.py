import serial
import time
# # 打开串口
ser = serial.Serial("/dev/ttyUSB0", 9600)
def main():
    while True:
        # 获得接收缓冲区字符
        count = ser.inWaiting()
        if count != 0:
            # 读取内容并回显
            recv = ser.read(count)
            ser.write(recv)
            # 清空接收缓冲区
        ser.flushInput()
        # 必要的软件延时
        time.sleep(0.1)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        if ser != None:
            ser.close()


import serial    #import serial module
ser = serial.Serial('/dev/ttyUSB0', 9600,timeout=1)   #open named port at 9600,1s timeot

#try and exceptstructure are exception handler
try:
  while 1:
    ser.write('s')#writ a string to port
    response = ser.readall()#read a string from port
    print(response)
except:
  ser.close()

  import serial
  import time

  # 打开串口
  ser = serial.Serial("/dev/ttyAMA0", 9600)


  def main():
      while True:
          # 获得接收缓冲区字符
          count = ser.inWaiting()
          if count != 0:
              # 读取内容并回显
              recv = ser.read(count)
              ser.write(recv)
          # 清空接收缓冲区
          ser.flushInput()
          # 必要的软件延时
          time.sleep(0.1)


  if __name__ == '__main__':
      try:
          main()
      except KeyboardInterrupt:
          if ser != None:
              ser.close()