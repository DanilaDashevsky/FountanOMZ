import struct
import pyaudio
import wave
from scipy.fft import fft
import numpy as np
import pydub
import scipy
import random
import snap7 #Отвечает за  отпарвку частот

db_number = 1 #адрес ячейки памяти, адрес дб
start_offset=27 #начало смещения
bit_offset=0 #смещение бита

def writeValue(color):
    # reading = plc.db_read(db_number,start_offset,1)
    # reading[0]=5 #перезаписываем единственное значенеи в нашем массиве байт, полученных от контроллера
    # plc.db_write(db_number,27,reading) #записываем наш массив данных в 27-ю ячейку
    #Если что-то не работает, попробуй увеличить байт на единицу, кроче вот это значение start_offset,у меня работало
    reading = plc.db_read(db_number, 30, 6)
    count=0
    for i in color:
        # match i:
        #     case "0":
        #         reading[count] = 0
        #     case "1":
        #         reading[count] = 1
        #     case "2":
        #         reading[count] = 2
        #     case "3":
        #         reading[count] = 3
        #     case "4":
        #         reading[count] = 4
        #     case "5":
        #         reading[count] = 5
        #     case "6":
        #         reading[count] = 6
        #     case "7":
        #         reading[count] = 7
        #     case "8":
        #         reading[count] = 8
        #     case "9":
        #         reading[count] = 9
        #     case "A":
        #         reading[count] = 10
        #     case "B":
        #         reading[count] = 11
        #     case "C":
        #         reading[count] = 12
        #     case "D":
        #         reading[count] = 13
        #     case "I":
        #         reading[count] = 14
        #     case "F":
        #         reading[count] = 15
        count+=1
    plc.db_write(db_number,30,reading)
    # plc.as_db_write(db_number,30,6,reading)


array_colors=[
[240, 128, 128],
[220, 20, 60],
[139, 0, 0],
[255, 20, 147],
[219, 112, 147],
[255, 69, 0],
[255, 165, 0],
[255, 0, 255],
[138, 43, 226],
[75, 0, 130],
[72, 61, 139],
[128, 0, 0],
[0, 0, 128],
[0, 128, 128],
[0, 255, 0],
]

plc = snap7.client.Client()
plc.connect('192.168.114.122',0,2) #0 -это стройка, 0-это слот для аппаратного обеспечения

chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 2
fs = 44100  # Record at 44100 samples per second
seconds = 3

wf = wave.open("musicMP3ssssssssssss.wav", 'rb')

openFileForWriteFrequencie = open("mytxt.txt","w")

p = pyaudio.PyAudio()  # Create an interface to PortAudio

print('Recording')

stream = p.open(
    format=p.get_format_from_width(wf.getsampwidth()),
    channels=wf.getnchannels(),
    rate=wf.getframerate(),
    frames_per_buffer=chunk,
    output=True)

def printColor():
    print(array_colors[random.randint(0,19)])

maxFrequencie = 0
data = wf.readframes(chunk) #мы получаем фреймы(части аудио), chunk нам говорит о том, на какое количество частей нам необходимо разделить наш аудиофрагмент
while data != '':
    stream.write(data) #запускаем проигрывание трека, путём записи наших фреймов в поток
    data = wf.readframes(chunk)
    data_int = np.array(struct.unpack(str(len(data)) + 'B', data),dtype='float')[::2]+127 #получаем массива байт из нашего цифрового аудио
    fs = scipy.fft.fft(data_int) #преобразуем байт по при помощи метода Фурье
    for i in fs:
        openFileForWriteFrequencie.writelines(str(abs(i.real))+ '\n')
        if i.real<800:
            print("red")
        else:
            if i.real>800 and i.real < 1600:
                print("green")
            else:
                if i.real > 1600:
                    print("blue")
        # if i.real>0:
        #     writeValue(array_colors[random.randint(0,19)]) #Отправка случайного цвета в функцию, которая занимается отправкой цвета в контроллер
        # else:
        #     writeValue(array_colors[random.randint(0, 19)]) #Отправка случайного цвета в функцию, которая занимается отправкой цвета в контроллер




"""Код отправки данных на данных на контроллер"""


"""
            db_number: number of the DB to be read.
            start: byte index from where is start to read from.
            size: amount of bytes to be read.
"""
def readValue():
    reading = plc.db_read(db_number, 31, 1)
    for i in reading:
        print(i)




# writeValue()
# readValue()