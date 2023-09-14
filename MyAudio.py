# import struct
# import pyaudio
# import wave
# from scipy.fft import fft
# import numpy as np
# import scipy
#
# chunk = 1024  # Record in chunks of 1024 samples
# sample_format = pyaudio.paInt16  # 16 bits per sample
# channels = 2
# fs = 44100  # Record at 44100 samples per second
# seconds = 3
# filename = "output.wav"
#
# wf = wave.open("music1.wav", 'rb')
#
#
# p = pyaudio.PyAudio()  # Create an interface to PortAudio
#
# print('Recording')
#
# stream = p.open(
#     format=p.get_format_from_width(wf.getsampwidth()),
#     channels=wf.getnchannels(),
#     rate=wf.getframerate(),
#     frames_per_buffer=chunk,
#     output=True)
#
#
#
# data = wf.readframes(chunk) #мы получаем фреймы(части аудио), chunk нам говорит о том, на какое количество частей нам необходимо разделить наш аудиофрагмент
# while data != '':
#     stream.write(data) #запускаем проигрывание трека, путём записи наших фреймов в поток
#     data_int = np.array(struct.unpack(str(len(data)) + 'B', data),dtype='float')[::2]+127 #получаем массива байт из нашего цифрового аудио
#     fs = scipy.fft.fft(data_int) #преобразуем байт по при помощи метода Фурье
#     for i in fs:
#         print(i.real) #получаем реальные значения numpy массива
#      sp = fftshift(fft(data_int))
#      freq = fftshift(fftfreq(data_int.shape[-1]))
#     # for i in (freq):
#     #     print("blue")
#         # if(i <= 0):
#         #     print("red")
#         # if (i >= 0):
#         #     print("blue")
#         # time.sleep(0.5)
#     # fs = scipy.fft.fft(data_int)
#     # for i in fs:
#     #     print(i)
#     # data = wf.readframes(chunk)
#
#
# # data1 = stream.read(chunk)
# #
# # while data:
# # #     # writing to the stream is what *actually* plays the sound.
# #
# #
# #         print(data_int)
#
#         # scipy.fft.fftfreq(struct.unpack(str(len(data)) + 'B', data),d=1.0)
#
# #      data = wf.readframes(chunk)
# #      # spec = librosa.stft(data)
# #      # spec_db = librosa.amplitude_to_db(abs(spec))
# #      # data_int = np.array(struct.unpack(str(len(data)) + 'B', data),dtype='int')[::2]+127
#
# # # ax = plt.subplot()
# # # ax.plot(data_int, '-')
# # # plt.show()
# #
# #
# #
# # # ss = stream.read(chunk)
# # # print(struct.unpack(str(chunk * 2) + 'B', ss))
# #
# #
# # frames = []  # Initialize array to store frames
# #
# # # Store data in chunks for 3 seconds
# # for i in range(0, int(fs / chunk * seconds)):
# #
# #     ampSample3 = abs(data[2])
# #     blockLinearRms =np.sqrt(np.mean(data ** 2))  # Linear value between 0 -> 1
# #     blockLogRms = 20 * math.log10(blockLinearRms)
# #     print(blockLogRms)
# #     frames.append(data)
# # for ss in data:
# #     print(ss)
# #     # t = np.arange(ss)
# #     # sp = np.fft.fft(np.sin(t))
# #     # freq = np.fft.fftfreq(t.shape[-1])
# #     # print(freq)
# # # Stop and close the stream
# # stream.stop_stream()
# # stream.close()
# # # Terminate the PortAudio interface
# # p.terminate()
# #
# # print('Finished recording')
# #
# # # Save the recorded data as a WAV file
# # wf = wave.open(filename, 'wb')
# # wf.setnchannels(channels)
# # wf.setsampwidth(p.get_sample_size(sample_format))
# # wf.setframerate(fs)
# # wf.writeframes(b''.join(frames))
# # wf.close()
#
# import pyaudio
# import wave
# import numpy as np
# # import scikits.audiolab
# # import scipy
# # x, fs, nbits = scikits.audiolab.wavread("music1.wav")











# import struct
#
# import pyaudio
# import wave
# import numpy as np
# chunk = 2048
# # open up a wave
# wf = wave.open('music/2E-Type_-_Set_The_World_On_Fire_47962776.wav', 'rb')
# swidth = wf.getsampwidth()
# RATE = wf.getframerate()
# # use a Blackman window
# window = np.blackman(chunk)
# # open stream
# p = pyaudio.PyAudio()
# stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
#                 channels = wf.getnchannels(),
#                 rate = RATE,
#                 output = True)
# # read some data
# data = wf.readframes(chunk)
# # play stream and find the frequency of each chunk]
# mt = open("mytxt.txt", "w")
# while len(data) == (chunk*swidth)*2:
#     # write data out to the audio stream
#     stream.write(data)
#     # unpack the data and times by the hamming window
#     indata = np.array(struct.unpack(str(len(data)) + 'B', data), dtype='float')[
#                ::2] + 127
#     # Take the fft and square each value
#     fftData=abs(np.fft.rfft(indata))**2
#     # find the maximum
#     which = fftData[1:].argmax() + 1
#     # use quadratic interpolation around the max
#     if which != len(fftData)-1:
#         y0,y1,y2 = np.log(fftData[which-1:which+2:])
#         x1 = (y2 - y0) * .5 / (2 * y1 - y2 - y0)
#         # find the frequency and output it
#         thefreq = (which+x1)*RATE/chunk
#         mt.write('\n'+str(thefreq))
#         # print ("The freq is %f Hz." % (thefreq))
#     else:
#         thefreq = which*RATE/chunk
#         mt.write('\n'+str(thefreq))
#         # print ("The freq is %f Hz." % (thefreq))
#     # read some more data
#     data = wf.readframes(chunk)
# if data:
#     stream.write(data)
# stream.close()
# p.terminate()









import librosa
import sys
import numpy as np
import matplotlib.pyplot as plt
import librosa.display

np.set_printoptions(threshold=sys.maxsize)

filename = 'music/2E-Type_-_Set_The_World_On_Fire_47962776.wav'
Fs = 44100
clip, sample_rate = librosa.load(filename, sr=Fs)

n_fft = 1024  # frame length
start = 0

hop_length=512

#commented out code to display Spectrogram
X = librosa.stft(clip, n_fft=n_fft, hop_length=hop_length)
#Xdb = librosa.amplitude_to_db(abs(X))
#plt.figure(figsize=(14, 5))
#librosa.display.specshow(Xdb, sr=Fs, x_axis='time', y_axis='hz')
#If to pring log of frequencies
#librosa.display.specshow(Xdb, sr=Fs, x_axis='time', y_axis='log')
#plt.colorbar()

#librosa.display.waveplot(clip, sr=Fs)
#plt.show()

#now print all values

t_samples = np.arange(clip.shape[0]) / Fs
t_frames = np.arange(X.shape[1]) * hop_length / Fs
#f_hertz = np.arange(N / 2 + 1) * Fs / N       # Works only when N is even
f_hertz = np.fft.rfftfreq(n_fft, 1 / Fs)  # Works also when N is odd



print('Frequency (Hz) : ', f_hertz.max())


#This code is working to printout frame by frame intensity of each frequency
#on top line gives freq bins
curLine = 'Bins,'
for b in range(1, len(f_hertz)):
    curLine += str(f_hertz[b]) + ','

curLine = ''
for f in range(1, len(t_frames)):
    curLine = str(t_frames[f]) + ','
    for b in range(1, len(f_hertz)): #for each frame, we get list of bin values printed
        curLine += str("%.02f" % np.abs(X[b, f])) + ','
        #remove format of the float for full details if needed
        curLine += str(np.abs(X[b, f])) + ','
        print(curLine)
        #print other useful info like phase of frequency bin b at frame f.
        # curLine += str("%.02f" % np.angle(X[b, f])) + ','
        # print(curLine)