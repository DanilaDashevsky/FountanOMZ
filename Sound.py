# -*- coding: utf-8 -*-
import time
# Form implementation generated from reading ui file 'Sound.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import tkinter as tk
import wave
import asyncio
import pyaudio
from pydub import AudioSegment
from tkinter import filedialog
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
import struct
import multiprocessing as mp
import pyaudio
import wave
from scipy.fft import fft
import numpy as np
import threading
import pydub
import scipy
import random
import snap7
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from typing import List

changeBack1 = 0
class Ui_MainWindow(object):
    def __init__(self):
        self.state = "Старт"
        self.parent_conn, self.child_conn = mp.Pipe()
        self.thread = mp.Process()

    # def playMusicLoop(list):
    #     for i in range(list.count() - 1):
    #         # list.item(i).setBackground(QBrush(Qt.gray, Qt.SolidPattern))
    #         # if i != 0:
    #         #     list.item(i - 1).setBackground(QBrush(Qt.white, Qt.SolidPattern))
    #         playMusic(list.item(i).text())
    def printWord1(self):
        if self.state == "Старт":
            self.state = "Стоп"
            if self.thread.is_alive():
                self.thread.terminate()
            ss = []
            for i in range(self.listWidget.count() - 1):
                ss.append(self.listWidget.item(i).text())
            self.thread = mp.Process(target=playMusic, args=(ss, self.child_conn))
            self.thread.start()

            self.pushButton_3.setText(self.state)
        else:

            self.thread.terminate()
            self.state = "Старт"
            self.pushButton_3.setText(self.state)

        # self.thread = threading.Thread(target=self.playMusic, args={nameMusic}, name=1,daemon=True)



    def playMusicThread(self, nameMusic):
        ss = [nameMusic]
        if self.thread.is_alive() == 0:
            self.thread = mp.Process(target=playMusic, args=[ss, self.child_conn])
            self.thread.start()
        else:
            self.thread.terminate()
            self.thread = mp.Process(target=playMusic, args=[ss,self.child_conn])
            self.thread.start()

    def loadFile(self):
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(filetypes=(("Music", '*.mp3'), ("Music", '*.wav')))
        if file_path != "":
            s = file_path.split('/')
            file_name = s[len(s) - 1].split('.')  # получение имени файла, без расширения
            sound1 = AudioSegment.from_mp3(file_path)
            sound1.export("music/" + file_name[0] + '.wav', format="wav")
            self.listWidget.addItem(file_name[0] + '.wav')

    def deleteItem(self):
        os.remove(r"music/"+self.listWidget.currentItem().text())
        self.listWidget.takeItem(self.listWidget.currentRow())
        # print(self.listWidget.currentItem().text())

    def add_function(self):
        self.pushButton_3.clicked.connect(lambda:
                                          self.printWord1())
        self.pushButton_4.clicked.connect(lambda: self.loadFile())
        self.pushButton_5.clicked.connect(lambda: self.deleteItem())
        self.pushButton.clicked.connect(lambda: self.changeBack())
        self.pushButton_2.clicked.connect(lambda: self.changeForward())


    def changeBack(self):
        while self.parent_conn.poll():
            ss = self.parent_conn.recv()
        arraymy = os.listdir("music")
        f = arraymy.index(ss)
        arraymyBlank = []
        if f != 0:
            f -= 1
            while f <= len(arraymy)-1:
                arraymyBlank.append(arraymy[f])
                f += 1
            self.Optimism(arraymyBlank)


    def Optimism(self,arraymyBlank): #Отправляет данные опять в уже обновлённый процесс
        if self.thread.is_alive():
            self.thread.terminate()
            self.thread = mp.Process(target=playMusic, args=(arraymyBlank, self.child_conn))
            self.thread.start()


    def changeForward(self):
        while self.parent_conn.poll():
            ss = self.parent_conn.recv()
        arraymy = os.listdir("music")
        f = arraymy.index(ss)
        f += 1
        arraymyBlank = []
        while f <= len(arraymy)-1:
            arraymyBlank.append(arraymy[f])
            f += 1
        self.Optimism(arraymyBlank)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Музыка фонтан"))
        MainWindow.setWindowIcon(QtGui.QIcon(r'Icons\FontanLogo.png'))
        self.pushButton.setText(_translate("MainWindow", "<"))
        self.pushButton_2.setText(_translate("MainWindow", ">"))
        self.pushButton_3.setText(_translate("MainWindow", self.state))
        self.pushButton_4.setText(_translate("MainWindow", "Загрузить"))
        self.pushButton_5.setText(_translate("MainWindow", "Удалить"))


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(440, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 230, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.resize(440, 200)
        for i in os.listdir("music"):
            self.listWidget.addItem(QListWidgetItem(i))
        self.listWidget.itemDoubleClicked.connect(lambda: self.playMusicThread(self.listWidget.currentItem().text()))

        # self.listWidget.itemSelectionChanged.connect(lambda:
        #                                              self.printWord())
        # self.listWidget.setDragDropMode(QtWidgets.QAbstractItemView)
        self.listWidget.setStyleSheet("margin-top:50%; ")
        # scroll = QScrollBar()
        # scroll.setGeometry(100, 50, 30, 200)
        # # scroll.setStyleSheet("background : lightgrey;")
        # self.listWidget.addScrollBarWidget(scroll,Qt.AlignRight)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 230, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(180, 230, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(60, 280, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(300, 280, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setStyleSheet("background-color:white;")
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 440, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        # self.setWindowIcon(QtGui.QIcon(r'C:\Users\SISPC\Desktop\Грфик.png'))
        # self.pushButton_2.setStyleSheet("cursor:pointer;")
        self.pushButton_3.setStyleSheet("cursor:pointer;")
        self.pushButton.setStyleSheet('''
        QPushButton {
        border-radius:10px; 
        border:2px solid black; 
        } 
        QPushButton:hover {
        background-color: LavenderBlush;
        }''')
        self.pushButton_2.setStyleSheet('''
        QPushButton {
        border-radius:10px; 
        border:2px solid black; 
        } 
        QPushButton:hover {
        background-color: LavenderBlush;
        }''')
        self.pushButton_3.setStyleSheet('''
        QPushButton {
        border-radius:10px; 
        border:2px solid black; 
        } 
        QPushButton:hover {
        background-color: LavenderBlush;
        }''')
        self.pushButton_4.setStyleSheet("border-radius:10px; border:2px solid black;background-color:rgb(1, 220, 30);")
        self.pushButton_5.setStyleSheet("border-radius:10px; border:2px solid black;background-color:rgb(213, 61, 47);")
        self.add_function()


db_number = 1 #адрес ячейки памяти, адрес дб
start_offset=27 #начало смещения
bit_offset=0 #смещение бита

plc = snap7.client.Client()
plc.connect('192.168.114.122',0,2) #0 -это стройка, 0-это слот для аппаратного обеспечения


def writeValue(): #Отправка случайного цвета в функцию, которая занимается отправкой цвета в контроллер
    # reading = plc.db_read(db_number,start_offset,1)
    # reading[0]=5 #перезаписываем единственное значенеи в нашем массиве байт, полученных от контроллера
    # plc.db_write(db_number,27,reading) #записываем наш массив данных в 27-ю ячейку
    #Если что-то не работает, попробуй увеличить байт на единицу, кроче вот это значение start_offset,у меня работало

    array_colors = [
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
    byte_array = bytearray(9)
    reading = [0 for _ in range(9)]
    count = 0
    for i in range(3):
        color = array_colors[random.randint(0, 14)]
        reading[count] = color[0]
        reading[count+1] = color[1]
        reading[count+2] = color[2]
        count += 3
    for i, x in enumerate(reading):
        snap7.util.set_byte(byte_array, i, x)
    plc.db_write(db_number,30, byte_array)

    # plc.as_db_write(db_number,30,6,reading)

def playMusic(sound_track: List, conn: mp.Pipe) -> None:
    srray = []
    for i in enumerate(sound_track):
        p = pyaudio.PyAudio()
        chunk = 1024
        ss = i[1]
        conn.send(ss)
        wf = wave.open(r"music/" + i[1], 'rb')
        stream = p.open(
            format=p.get_format_from_width(wf.getsampwidth()),
            channels=wf.getnchannels(),
            rate=wf.getframerate(),
            frames_per_buffer=chunk,
            output=True)
        data = wf.readframes(chunk)  # мы получаем фреймы(части аудио), chunk нам говорит о том, на какое количество частей нам необходимо разделить наш аудиофрагмент
        while data != None:
            stream.write(data)  # запускаем проигрывание трека, путём записи наших фреймов в поток
            data = wf.readframes(chunk)
            if len(data) != 0: #"""and self.state == "Стоп" """
                data_int = np.array(struct.unpack(str(len(data)) + 'B', data), dtype='float')[
                           ::2]  # получаем массива байт из нашего цифрового аудио
                fs = scipy.fft.fft(data_int)  # преобразуем байт по при помощи метода Фурье, логика таккова, что чем больше длинна массива data_int, тем выше частота
                for i in fs:
                    if i.real > 50:
                        if i.real < 1500:
                            # connMuz.send(i.real)
                            # writeValue()
                            print('red')
                            continue
                        else:
                            if i.real > 1500 and i.real < 2200:
                                # connMuz.send(i.real)
                                # writeValue()
                                print('blue')
                                continue
                            else:
                                if i.real > 2200:
                                    # connMuz.send(i.real)
                                    print('green')
                                    # writeValue()
                                    continue

            else:
                break
        wf.close()

    # if i.real>0:
    #     writeValue(array_colors[random.randint(0,19)]) #Отправка случайного цвета в функцию, которая занимается отправкой цвета в контроллер
    # else:
    #     writeValue(array_colors[random.randint(0, 19)]) #Отправка случайного цвета в функцию, которая занимается отправкой цвета в контроллер



ui=None
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    # threading.Thread(target=ui.setupUi,args={MainWindow}).start()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
