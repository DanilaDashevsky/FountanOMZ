import time
from threading import *
import librosa
import numpy
import numpy as np
import soundfile as sf
import wave
import sounddevice
from audiosegment import AudioSegment
from numba import njit, prange, jit
# load the audio signal and its sample rate
# sacrifice_signal, sample_rate = librosa.load("musicMP3ssssssssssss.wav")
import librosa.display
from scipy.io import wavfile
from scipy.fftpack import fft
# We'll need IPython.display's Audio widget
from IPython.display import Audio

# We'll also use `mir_eval` to synthesize a signal for us
import mir_eval.sonify
import matplotlib.pyplot as plt
from pydub import AudioSegment
from pydub.playback import play
# plt.figure(figsize=(10, 3))
# librosa.display.waveshow(sacrifice_signal, sr=sample_rate) # use waveplot should waveshow be unavailable
# plt.show()
# Load an audio file

def myFunction(n):
    sr = 22050
    # y, sr = librosa.load("music.wav")
    # f0, voiced_flag, voiced_probs = librosa.pyin(y,
    #                                              sr=sr,
    #                                              fmin=librosa.note_to_hz('C2'),
    #                                              fmax=librosa.note_to_hz('C7'),
    #                                            fill_na=None)
    #
    #
    # spec = librosa.stft(y)
    # spec_db = librosa.amplitude_to_db(abs(spec))
    # for im in spec_db:
    #     print(im)
    # To synthesize the f0, we'll need sample times
    # times = librosa.times_like(f0)
    # vneg = (-1) ** (~voiced_flag)
    # y_f0 = mir_eval.sonify.pitch_contour(times, f0 * vneg, sr)
    # for y_f01 in y_f0:
    #     print(y_f01)
    # y, sr = librosa.load("musicMP3ssssssssssss.wav")  # Загружаем наш файл
    # # Compute pitch using the PEPLOs algorithm
    # #y - это количесво семплов
    # f0, voiced_flag, voiced_probs = librosa.pyin(y, fmin=librosa.note_to_hz('C2'), fmax=librosa.note_to_hz('C7'))  #fmin - отвечает за какую-то рукомендуемую минимальную частоту, допустимую в спектре, котороя по документации должна быть равна librosa.note_to_hz('C2') =65 Гц
    # print("Voiced_flag:",voiced_flag,"Voiced_probs:",voiced_probs)
    # # Plot pitch contour
    # plt.figure(figsize=(12, 4)) #размер фигуры, нашего полотна на котором мы отрисовываем
    # librosa.display.waveshow(y, sr=sr, alpha=0.5) #отвечает за нанесение высоты тона поверх полотна
    # plt.plot(librosa.frames_to_time(range(len(f0))), f0, color='r') # range(len(f0))) - это количество сэмплов в одном аудио, которое мы разбили f0- это массив этих сэмплов
    # print(f0)
    # plt.xlabel('Time (s)')
    # plt.ylabel('Frequency (Hz)')
    # plt.title('Pitch Contour')
    # plt.show()


    f= open("mytxt.txt","r")


    print("Hello")
    # librosa.display.specshow(spec_db, sr=sr, x_axis='time', y_axis='hz')
    # for spec_db1 in spec_db:
    #     for spec_db2 in spec_db1:
    #         f.writelines(str(spec_db2))
    # for item in f:
    #     print(item)
    #     time.sleep(0.93)
    #     if float(item) <50:
    #         print("red")

    # plt.plot(librosa.frames_to_time(range(len(f0))), f0, color='r') # range(len(f0))) - это количество сэмплов в одном аудио, которое мы разбили f0- это массив этих сэмплов
    # plt.xlabel('Time (s)')
    # plt.ylabel('Frequency (Hz)')
    # plt.title('Pitch Contour')
    # plt.show()

    # myAudio = "musicMP3ssssssssssss.wav"
    #
    # # Чтение файла и получение частоты дискретизации и звукового объект
    # samplingFreq, mySound = wavfile.read(myAudio)
    #
    # # Проверяем является ли wave-файл 16-битным или 32-битным. (24 бит не поддерживается)
    # mySoundDataType = mySound.dtype
    #
    # # Мы можем преобразовать наш звуковой массив в значения с плавающей запятой в диапазоне от -1 до 1 следующим образом
    #
    # mySound = mySound / (2. ** 15)
    #
    # # Проверим точки отсчета и звуковой канал для двух каналов или для моноканала
    #
    # mySoundShape = mySound.shape
    # samplePoints = float(mySound.shape[0])
    #
    # # Если два канала, то выберем только один кана
    # mySoundOneChannel = mySound[0:]
    #
    # # График частотного содержания
    # # Мы можем получить частоту из амплитуды и времени с помощью БПФ, быстрого алгоритма преобразования Фурье
    # # Получим длину моего массива звуковых объектов
    # mySoundLength = len(mySound)
    #
    # # Возьмем преобразование Фурье для данной точки отсчета
    # fftArray = fft(mySoundOneChannel)
    #
    # numUniquePoints = int(numpy.ceil((mySoundLength + 1) / 2.0))
    # fftArray = fftArray[0:numUniquePoints]
    #
    # # БПФ содержит как величину, так и фазу и задается комплексными числами в формате действительных + мнимых частей (a + ib).
    # # Принимая абсолютное значение, мы получаем только действительную часть.
    #
    # fftArray = abs(fftArray)
    #
    # # Масштабируйте массив fft по длине точек выборки, чтобы величина не зависела отдлина сигнала или его частота дискретизации
    #
    # fftArray = fftArray / float(mySoundLength)
    #
    # # БПФ имеет как положительную, так и отрицательную информацию. Площадь возводим в квадрат, чтобы получить только положительные значения
    # fftArray = fftArray ** 2
    #
    # if mySoundLength % 2 > 0:  # у нас есть нечетное число точек в FFT
    #     fftArray[1:len(fftArray)] = fftArray[1:len(fftArray)] * 2
    #
    # else:  # У нас есть чётное количество точек в БПФ
    #     fftArray[1:len(fftArray) - 1] = fftArray[1:len(fftArray) - 1] * 2
    #
    # freqArray = numpy.arange(0, numUniquePoints, 1.0) * (samplingFreq / mySoundLength)
    #
    #
    # for i in freqArray:
    #     print(i)
def playAudio():
    tape = AudioSegment.from_wav('music1.wav')
    play(tape)

def readFrequencie():
    textFile =  open("mytxt1.txt")
    textList = textFile.readlines()
    t = 25000/1124425
    for i in textList:
        time.sleep(t)
        if float(i) > -50:
            print(i)
            print("red")
        # print(file.readlines())
        # print("Heeeeeeeeeeeeeeeeeelllllllllllllllllllllllllpoooooooooooooooooo")




f1 = Thread(target=playAudio)
f2 = Thread(target=readFrequencie)

f1.start()
f2.start()

def writeFrequencie():
    y, sr = librosa.load("music.wav")
    f0, voiced_flag, voiced_probs = librosa.pyin(y,
                                                 sr=sr,
                                                 fmin=librosa.note_to_hz('C2'),
                                                 fmax=librosa.note_to_hz('C7'),
                                                 fill_na=None)
    f = open("mytxt1.txt", "w")
    spec = librosa.stft(y)
    spec_db = librosa.amplitude_to_db(abs(spec))
    for im in spec_db:
        for im1 in im:
            f.writelines(str(im1)+"\n")
    f.close()

# writeFrequencie()
