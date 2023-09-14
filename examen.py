# import wave
#
# import pyaudio
# import numpy as np
#
# # Определение пороговых значений частоты (в Гц)
# low_freq_threshold = 80428.68482440244  # Низкая частота
# high_freq_threshold = 139428.68482440244 # Высокая частота
#
# # Создаем объект для работы с аудио
# p = pyaudio.PyAudio()
#
# # Открываем файл .wav для чтения (замени 'input.wav' на имя своего файла)
# wf = wave.open('music/2E-Type_-_Set_The_World_On_Fire_47962776.wav', 'rb')
#
# # Определение параметров аудио
# chunk = 1024  # Количество сэмплов за один "кадр"
# sample_format = pyaudio.paInt16
# channels = wf.getnchannels()
# rate = wf.getframerate()
#
# # Создаем поток для проигрывания аудио
# stream = p.open(format=sample_format,
#                 channels=channels,
#                 rate=rate,
#                 output=True)
#
# print("Воспроизведение аудио...")
# ss =[]
# while True:
#     data = wf.readframes(chunk)
#     if not data:
#         break
#
#     # Преобразование байтовых данных в массив NumPy
#     audio_data = np.frombuffer(data, dtype=np.int16)
#
#     # Вычисляем среднюю частоту звука
#     avg_frequency = np.mean(np.abs(np.fft.fft(audio_data)))
#     ss.append(avg_frequency)
#     # Определяем цвет на основе частоты
#     if avg_frequency < low_freq_threshold:
#         print("red")
#     elif avg_frequency < high_freq_threshold:
#         print("blue")
#     else:
#         print("green")
#
#     # Воспроизводим аудио
#     stream.write(data)
import wave

# # Закрываем потоки и объекты PyAudio
# print(sum(ss)/len(ss))
# stream.stop_stream()
# stream.close()
# wf.close()
# p.terminate()


import pyaudio
import numpy as np

# Определение пороговых значений частоты (в Гц)
import pyaudio
import numpy as np

# Определение пороговых значений частоты (в Гц)
import pyaudio
import librosa
import numpy as np

# Определение пороговых значений частоты (в Гц)
low_freq_threshold = 20  # Низкая частота (20 Гц)
high_freq_threshold = 20000  # Высокая частота (20 000 Гц)

# Создаем объект для работы с аудио
p = pyaudio.PyAudio()

# Загрузка аудиофайла с использованием librosa
audio_path = 'music/2E-Type_-_Set_The_World_On_Fire_47962776.wav'  # Замените на свой путь к файлу
audio_data, sample_rate = librosa.load(audio_path, sr=None)

# Создаем поток для воспроизведения аудио
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=sample_rate,
                output=True)

print("Воспроизведение аудио...")

block_size = 1024  # Размер блока анализа (количество сэмплов)
for i in range(0, len(audio_data), block_size):
    block = audio_data[i:i + block_size]

    # Вычисляем FFT спектр для блока аудио
    spectrum = np.fft.fft(block)

    # Находим индекс частоты с максимальной амплитудой
    max_freq_index = np.argmax(np.abs(spectrum))

    # Вычисляем частоту в Гц с использованием индекса и частоты дискретизации
    max_frequency = max_freq_index * sample_rate / len(block)

    # Определяем цвет на основе частоты, убедившись, что она находится в допустимом диапазоне
    print(low_freq_threshold)
    if low_freq_threshold <= max_frequency <= high_freq_threshold:
        if max_frequency < 500:
            print("red")
        elif max_frequency < 2000:
            print("blue")
        else:
            print("green")
    else:
        pass

    # Воспроизводим блок аудио
    stream.write(block.tobytes())

# Завершение проигрывания
stream.stop_stream()
stream.close()
p.terminate()


