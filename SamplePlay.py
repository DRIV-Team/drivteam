#from pydub import AudioSegment
#from pydub.playback import play

#sound = AudioSegment.from_wav('1000.mp3')
#play(sound)

import soundfile as sf
import os
import sounddevice as sd
import scipy
from scipy.io.wavfile import write
import threading
import time

class soundBox(object):
    """Docstring for soundBox"""
    def __init__(self):
        self.rate = 44100
        self.channels = 2
        #self.recording = 'output.wav' 

    def record(self, seconds, title):
        self.seconds = seconds
        myrecording = sd.rec(int(self.seconds * self.rate), samplerate=self.rate, channels=self.channels)
        sd.wait()  # Wait until recording is finished
        write(title, self.rate, myrecording)  # Save as WAV file 

    def play(self, title):
        # Extract data and sampling rate from file
        data, fs = sf.read(title, dtype='float32')  
        sd.play(data, fs)
        status = sd.wait()  # Wait until file is done playing



#microphone.record(110)
#microphone.play('output.wav')

#for dirpath, dirnames, files in os.walk('.'):
 #   print(f'Found directory: {dirpath}')
  #  for file_name in files:
   #     print(file_name)

#print(sd.query_devices())
#Prints all available output devices for sound connected to this computer

def keepRecording(name):
    while True:
        mic.record(1, name)


mic = soundBox()
message = input("do you want to stop the app? Y/N")
empty = 1
x = threading.Thread(target=keepRecording, args=('output.wav',))
x.start()
time.sleep(1)
while not (message == 'Y'):
    #x = threading.Thread(target=keepRecording, args=('output.wav',))
    #x.start()
    mic.play('output.wav')
    #if (empty == 1):
     #   mic.record(.5, 'output.wav')
      #  empty = 0
    #else:
     #   mic.play('output.wav')
      #  mic.record(.5, 'output.wav')
    #message = input("do you want to stop the app? Y/N")

