import time
from numba import jit,njit



# AudioSegment.converter = r"C:\Myfolder\ffmpeg\ffmpeg\bin\ffmpeg.exe"
# AudioSegment.ffprobe = r"C:\Myfolder\ffmpeg\ffmpeg\bin\ffprobe.exe"
#
# sound = AudioSegment.from_mp3(r'C:\Users\SISPC\PycharmProjects\pythonProject\shortMusic.mp3')
# sound.export("shortMusic.wav", format="wav")

# wf = wave.open("musicMP3ssssssssssss.wav", 'rb')
#
# # instantiate PyAudio (1)
# p = pyaudio.PyAudio()
#
# # define callback (2)
# def callback(in_data, frame_count, time_info, status):
#     data = wf.readframes(frame_count)
#     return (data, pyaudio.paContinue)
#
# # open stream using callback (3)
# stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
#                 channels=wf.getnchannels(),
#                 rate=wf.getframerate(),
#                 output=True,
#                 stream_callback=callback)
#
# # start the stream (4)
# stream.start_stream()
#
# # wait for stream to finish (5)
# while stream.is_active():
#     time.sleep(0.1)
#
# # stop stream (6)
# stream.stop_stream()
# stream.close()
# wf.close()
#
# # close PyAudio (7)
# p.terminate()
import sys

sys.path.append(r"C:\Users\SISPC\PycharmProjects\pythonProject\venv\Lib\site-packages")

@njit(cache=True)
def Count(value):
    count=0
    i,j=1,1
    while i<=value:
        while j<=i:
            if i % j == 0:
                count += 1
            j+=1
        if count == 2:
            return True
        i+=1
        j=1
        count=0
    # for i in range(value):
    #     for j in range(i):
    #         if i/j ==0:
    #             count+=1
    #     if count ==2:
    #         print(i)

start = time.perf_counter()
Count(1000000000)
end =time.perf_counter()-start
print(f"{end}")

