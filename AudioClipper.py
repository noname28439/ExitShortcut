import pyaudio
import wave
from threading import Thread
from datetime import datetime
from win10toast import ToastNotifier

toast = ToastNotifier()

def notitfy(header, text):
    toast.show_toast(header,text,duration=20)


CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100

frameList = []

def current_date():
    now = datetime.now()
    return now.strftime("%d_%m_%Y-%H_%M_%S")


def record(sec):
    frames = []
    #print("* recording")
    for i in range(0, int(RATE / CHUNK * sec)):
        data = stream.read(CHUNK)
        frames.append(data)
    #print("* done recording")
    return frames

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)


SETTINGS = {
    "CLIP_LENGTH": 2,
    "MAX_STORE": 60
}

def thr_listener():
    global frameList
    while True:
        frameList.append(record(SETTINGS.get("CLIP_LENGTH")))
        if(len(frameList)*SETTINGS.get("CLIP_LENGTH")>SETTINGS.get("MAX_STORE")):
            frameList = frameList[1:]
        #print("len: "+str(len(frameList)))



def clip():
    calcFrames = []
    for frameData in frameList:
        for data in frameData:
            calcFrames.append(data)
    save_file(calcFrames, "./AudioClip-"+current_date()+".wav")
    notitfy("AudioClipper", "Clip successfully created")


def save_file(frms, path):
    wf = wave.open(path, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frms))
    wf.close()


t = Thread(target=thr_listener)
t.daemon = True
t.start()


# stream.stop_stream()
# stream.close()
# p.terminate()