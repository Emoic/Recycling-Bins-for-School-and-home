import wave
from pyaudio import PyAudio,paInt16
from pydub import AudioSegment

framerate=16000
NUM_SAMPLES=2000
channels=1
sampwidth=2
TIME=2
def save_wave_file(filename,data):
    '''save the date to the wavfile'''
    wf=wave.open(filename,'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(sampwidth)
    wf.setframerate(framerate)
    wf.writeframes(b"".join(data))
    wf.close()

def my_record(file_name):
    pa=PyAudio()
    stream=pa.open(format = paInt16,channels=1,
                   rate=framerate,input=True,
                   frames_per_buffer=NUM_SAMPLES)
    my_buf=[]
    count=0
    while count<TIME*8:#控制录音时间
        string_audio_data = stream.read(NUM_SAMPLES)
        my_buf.append(string_audio_data)
        count+=1
        print('.')
    save_wave_file(file_name,my_buf)
    stream.close()

chunk=2014
def play(file_name):
    wf=wave.open(file_name,'rb')
    p=PyAudio()
    stream=p.open(format=p.get_format_from_width(wf.getsampwidth()),channels=
    wf.getnchannels(),rate=wf.getframerate(),output=True)
    data = wf.readframes(chunk)
    while data != b'':
        stream.write(data)
        data = wf.readframes(chunk)
    stream.stop_stream()            # 停止数据流
    stream.close()
    p.terminate()
    print('end')

def changefromt(source_file,output_file):
    song = AudioSegment.from_mp3(source_file)
    song.export(output_file, format="wav")
    print('\n转换已完成')

if __name__ == '__main__':
    my_record('01.pcm')
    print('Over!')
    play('01.pcm')
