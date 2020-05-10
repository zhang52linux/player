from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtMultimedia import QMediaPlayer,QMediaContent
from PyQt5.QtMultimedia import QMediaPlaylist
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtGui import QPixmap,QBitmap
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import  QPainter
from PyQt5.QtCore import QRect
import pymysql
import sys,os
import requests
import threading
from time import sleep


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1124, 764)
        self.MusicName = QtWidgets.QLabel(Form)
        self.MusicName.setGeometry(QtCore.QRect(30, 24, 72, 31))
        self.MusicName.setStyleSheet("font: 11pt \"MingLiU_HKSCS-ExtB\";")
        self.MusicName.setObjectName("MusicName")
        self.SongName = QtWidgets.QLineEdit(Form)
        self.SongName.setGeometry(QtCore.QRect(120, 20, 371, 31))
        self.SongName.setStyleSheet("font: 11pt \"MingLiU_HKSCS-ExtB\";")
        self.SongName.setObjectName("SongName")
        self.MusicianName = QtWidgets.QLabel(Form)
        self.MusicianName.setGeometry(QtCore.QRect(510, 20, 72, 31))
        self.MusicianName.setStyleSheet("font: 11pt \"MingLiU_HKSCS-ExtB\";")
        self.MusicianName.setObjectName("MusicianName")
        self.Musician = QtWidgets.QLineEdit(Form)
        self.Musician.setGeometry(QtCore.QRect(600, 20, 341, 31))
        self.Musician.setStyleSheet("font: 11pt \"MingLiU_HKSCS-ExtB\";")
        self.Musician.setObjectName("Musician")
        self.search = QtWidgets.QPushButton(Form)
        self.search.setGeometry(QtCore.QRect(980, 20, 111, 31))
        self.search.setStyleSheet("font: 11pt \"MingLiU_HKSCS-ExtB\";")
        self.search.setObjectName("search")
        self.Local = QtWidgets.QListWidget(Form)
        self.Local.setGeometry(QtCore.QRect(30, 100, 521, 481))
        self.Local.setObjectName("Local")
        self.LocalList = QtWidgets.QLabel(Form)
        self.LocalList.setGeometry(QtCore.QRect(30, 60, 131, 31))
        self.LocalList.setStyleSheet("font: 11pt \"MingLiU_HKSCS-ExtB\";")
        self.LocalList.setObjectName("LocalList")
        self.LoadSong = QtWidgets.QPushButton(Form)
        self.LoadSong.setGeometry(QtCore.QRect(360, 60, 131, 31))
        self.LoadSong.setStyleSheet("font: 11pt \"MingLiU_HKSCS-ExtB\";")
        self.LoadSong.setObjectName("LoadSong")
        self.Internet = QtWidgets.QListWidget(Form)
        self.Internet.setGeometry(QtCore.QRect(560, 100, 531, 481))
        self.Internet.setObjectName("Internet")
        self.InternetList = QtWidgets.QLabel(Form)
        self.InternetList.setGeometry(QtCore.QRect(560, 60, 131, 31))
        self.InternetList.setStyleSheet("font: 11pt \"MingLiU_HKSCS-ExtB\";")
        self.InternetList.setObjectName("InternetList")
        self.toolButton = QtWidgets.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(450, 700, 41, 41))
        self.toolButton.setStyleSheet("border-image: url(image/1.png);\n"
"background-color:transparent;")
        self.toolButton.setText("")
        self.toolButton.setObjectName("toolButton")
        self.labelEnd = QtWidgets.QLabel(Form)
        self.labelEnd.setGeometry(QtCore.QRect(610, 658, 51, 21))
        self.labelEnd.setStyleSheet("font: 75 12pt \"Arial\";\n"
"color: rgb(0, 255, 0);")
        self.labelEnd.setText("")
        self.labelEnd.setObjectName("labelEnd")
        self.CurMusic = QtWidgets.QLineEdit(Form)
        self.CurMusic.setGeometry(QtCore.QRect(130, 600, 961, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CurMusic.sizePolicy().hasHeightForWidth())
        self.CurMusic.setSizePolicy(sizePolicy)
        self.CurMusic.setStyleSheet("background-color:rgb(0,0,255);\n"
"font: 75 12pt \"Arial\";\n"
"\n"
"")
        self.CurMusic.setReadOnly(True)
        self.CurMusic.setObjectName("CurMusic")
        self.labelVolume = QtWidgets.QLabel(Form)
        self.labelVolume.setGeometry(QtCore.QRect(940, 658, 51, 20))
        self.labelVolume.setStyleSheet("font: 75 12pt \"Arial\";\n"
"color: rgb(0, 255, 0);")
        self.labelVolume.setText("")
        self.labelVolume.setObjectName("labelVolume")
        self.pushButtonNext = QtWidgets.QPushButton(Form)
        self.pushButtonNext.setGeometry(QtCore.QRect(340, 700, 41, 41))
        self.pushButtonNext.setStyleSheet("border-image: url(image/next1.png);\n"
        "\n"
        "\n"
        "\n"
        "\n"
        "")
        self.pushButtonNext.setText("")
        self.pushButtonNext.setObjectName("pushButtonNext")
        self.VolumeSlider = QtWidgets.QSlider(Form)
        self.VolumeSlider.setGeometry(QtCore.QRect(730, 658, 361, 20))
        self.VolumeSlider.setStyleSheet("QSlider::groove:horizontal {\n"
        "border: 1px solid #cococo;\n"
        "height:5px; \n"
        "background: #C0C0C0;\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal \n"
        "{\n"
        "    background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, \n"
        "    stop:0.6 rgb(255,0,0), stop:0.778409 rgb(0, 255, 0));\n"
        "    margin-top: -3px;\n"
        "    margin-bottom: -3px;\n"
        "    border-radius: 5px;\n"
        "    width:11px;\n"
        "    \n"
        "}\n"
        "\n"
        "QSlider::sub-page:horizontal {\n"
        "background: qlineargradient(spread:pad, x1:0, y1:0,x2:1, y2:0, \n"
        "    stop:0 rgb(255,0,0),stop:0.5 rgb(0,255,0) stop:1 rgb(0, 0, 255));\n"
        "border-radius:2px;\n"
        "}")
        self.VolumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.VolumeSlider.setObjectName("VolumeSlider")
        self.pushButtonVolume = QtWidgets.QPushButton(Form)
        self.pushButtonVolume.setGeometry(QtCore.QRect(670, 658, 31, 21))
        self.pushButtonVolume.setStyleSheet("background-color:transparent;\n"
"border-image: url(image/Volume.png);")
        self.pushButtonVolume.setText("")
        self.pushButtonVolume.setObjectName("pushButtonVolume")
        self.current_song = QtWidgets.QLabel(Form)
        self.current_song.setGeometry(QtCore.QRect(30, 600, 91, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.current_song.sizePolicy().hasHeightForWidth())
        self.current_song.setSizePolicy(sizePolicy)
        self.current_song.setStyleSheet("background-color:transparent;\n"
"font: 75 12pt \"Arial\";\n"
"")
        self.current_song.setObjectName("current_song")
        self.pushButtonplay = QtWidgets.QPushButton(Form)
        self.pushButtonplay.setGeometry(QtCore.QRect(210, 700, 51, 41))
        self.pushButtonplay.setToolTipDuration(1)
        self.pushButtonplay.setStyleSheet("background-color:transparent;\n"
"border-image: url(image/play.png);\n"
"\n"
"\n"
"")
        self.pushButtonplay.setText("")
        self.pushButtonplay.setObjectName("pushButtonplay")
        self.ProgressSlider = QtWidgets.QSlider(Form)
        self.ProgressSlider.setGeometry(QtCore.QRect(110, 658, 481, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ProgressSlider.sizePolicy().hasHeightForWidth())
        self.ProgressSlider.setSizePolicy(sizePolicy)
        self.ProgressSlider.setStyleSheet("QSlider::groove:horizontal {\n"
        "border: 1px solid #cococo;\n"
        "height:5px; \n"
        "background: #C0C0C0;\n"
        "}\n"
        "\n"
        "QSlider::handle:horizontal \n"
        "{\n"
        "    background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, \n"
        "    stop:0.6 rgb(255,0,0), stop:0.778409 rgb(0, 255, 0));\n"
        "    margin-top: -3px;\n"
        "    margin-bottom: -3px;\n"
        "    border-radius: 5px;\n"
        "    width:11px;\n"
        "    \n"
        "}\n"
        "\n"
        "QSlider::sub-page:horizontal {\n"
        "background: qlineargradient(spread:pad, x1:0, y1:0,x2:1, y2:0, \n"
        "    stop:0 rgb(255,0,0),stop:0.5 rgb(0,255,0) stop:1 rgb(0, 0, 255));\n"
        "border-radius:2px;\n"
        "}")
        self.ProgressSlider.setOrientation(QtCore.Qt.Horizontal)
        self.ProgressSlider.setObjectName("ProgressSlider")
        self.pushButtonBefore = QtWidgets.QPushButton(Form)
        self.pushButtonBefore.setGeometry(QtCore.QRect(80, 700, 41, 41))
        self.pushButtonBefore.setStyleSheet("border-image: url(image/before.png);\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.pushButtonBefore.setText("")
        self.pushButtonBefore.setObjectName("pushButtonBefore")
        self.Title = QtWidgets.QLabel(Form)
        self.Title.setGeometry(QtCore.QRect(630, 703, 471, 31))
        self.Title.setStyleSheet("background-color: rgba(255, 85, 127,0.5);\n"
"font: 75 14pt \"Arial\";")
        self.Title.setObjectName("Title")
        self.labelStart = QtWidgets.QLabel(Form)
        self.labelStart.setGeometry(QtCore.QRect(30, 658, 71, 21))
        self.labelStart.setStyleSheet("font: 75 12pt \"Arial\";\n"
"color: rgb(0, 255, 0);")
        self.labelStart.setText("")
        self.labelStart.setObjectName("labelStart")
        self.toolButtonMV = QtWidgets.QToolButton(Form)
        self.toolButtonMV.setGeometry(QtCore.QRect(540, 700, 41, 41))
        self.toolButtonMV.setStyleSheet("border-image: url(image/MV.png);\n"
"background-color:transparent;")
        self.toolButtonMV.setText("")
        self.toolButtonMV.setObjectName("toolButtonMV")
        self.Internet.setStyleSheet("background:rgba(123,123,123,0.8);color:aqua;font-weight:bold")
        self.Local.setStyleSheet("background:rgba(123,123,123,0.8);color:aqua;font-weight:bold")
        self.CurMusic.setStyleSheet("background:rgba(123,123,123,0.8);color:aqua;font-weight:bold")
        self.LoadSong.setStyleSheet("background:rgba(123,123,123,0.8);color:aqua;font-weight:bold")
        self.search.setStyleSheet("background:rgba(123,123,123,0.8);color:aqua;font-weight:bold")
        self.Musician.setStyleSheet("background:rgba(123,123,123,0.8);color:aqua;font-weight:bold")
        self.SongName.setStyleSheet("background:rgba(123,123,123,0.8);color:aqua;font-weight:bold")


        self.retranslateUi(Form)
        self.search.clicked.connect(Form.start_search) #进行网络歌曲的搜索时用
        self.LoadSong.clicked.connect(Form.Load_Song) #进行本地歌曲的加载
        self.Local.clicked.connect(Form.custom_current_music) #当用户自己点击切换歌曲的时候触发
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.MusicName.setText(_translate("Form", "歌曲名字:"))
        self.MusicianName.setText(_translate("Form", "歌手名字:"))
        self.search.setText(_translate("Form", "搜索"))
        self.LocalList.setText(_translate("Form", "本地歌曲列表:"))
        self.LoadSong.setText(_translate("Form", "导入歌曲"))
        self.InternetList.setText(_translate("Form", "网络歌曲列表:"))
        self.pushButtonNext.setToolTip(_translate("Form", "下一首"))
        self.current_song.setText(_translate("Form", "当前歌曲:"))
        self.pushButtonplay.setStatusTip(_translate("Form", "播放/暂停"))
        self.pushButtonBefore.setToolTip(_translate("Form", "下一首"))
        self.Title.setText(_translate("Form", "                BY SZW_ZHANG 2020-04-18"))

class db():
    def __init__(self):
        host = 'localhost'
        user = 'root'
        password = 'zhang842563'
        database = 'vip_music'
        self.db = pymysql.connect(host,user,password,database)
        #创建游标对象
        self.cursor = self.db.cursor()

    def edit_db(self,name,title,author,music):
        try:
            sql = "INSERT INTO %s VALUES('%s','%s','%s');" % (name,title,author,music)
            return self.cursor.execute(sql)
        except Exception as e:
            print('插入信息出错:{}'.format(e))
            return 0

    def create_table(self,name):
        try:
            sql = "CREATE TABLE IF NOT EXISTS %s(music_title VARCHAR(1000),music_author VARCHAR(1000),music_url VARCHAR(255) PRIMARY KEY);" % (name)
            self.cursor.execute(sql)
        except Exception as e:
            print(e)



    def get_data(self,name,music):
        try:
            sql = "SELECT * FROM {} WHERE music_title LIKE '{}%';".format(name,music)
            self.cursor.execute(sql)
        except Exception as e:
            print('查询信息出错:{}'.format(e))
            self.create_table(name)
            print('重新开始查询......')
        else:
            return self.cursor.fetchone()

    def close_DB(self):
        self.db.close()

class Example(QThread):
    signal = pyqtSignal(str)    # 括号里填写信号传递的参数
    def __init__(self):
        super().__init__()

    def __del__(self):
        self.wait()

    def run(self):

        self.signal.emit()


class search_song(QThread):
    song = pyqtSignal(str)

    def __init__(self,music_name,musician_name):
        super(search_song,self).__init__()
        self.music_name = music_name
        self.musician_name = musician_name
        print(self.music_name)

    def run(self):
        self.SaveData = db()
        music_data = self.SaveData.get_data(self.musician_name, self.music_name)
        self.SaveData.close_DB()
        self.song.emit(str(music_data))


class music_play(QtWidgets.QMainWindow,Ui_Form):
    #初始化一些操作
    def __init__(self):
        super(music_play,self).__init__()   #调用该类的父类的初始化函数，完成窗口布局操作
        self.setupUi(self)
        self.setWindowTitle("VIP音乐播放器")
        self.setWindowIcon(QIcon("format.ico"))
        #self.SaveData = db()
        self.m_filepath = 'E:/MusicMedia/MusicMedia/music/'
        self.player = QMediaPlayer()
        self.PlayList = QMediaPlaylist()
        self.player.setPlaylist(self.PlayList)
    #网络歌曲的搜索模块
    def start_search(self):
        music_name = self.SongName.text()
        musician_name = self.Musician.text()
        search = search_song(self.music_name,self.musician_name)
        search.song.connect(self.search_song2)
        search_song.start()

    def search_song2(self,music_data):
        #music_data = self.SaveData.get_data(musician_name,music_name)
        #在此处构建一个url实现在线播放
        print(music_data)
        file_url = music_data[2]
        file_name = "{} - {}".format(music_data[0],music_data[1])
        self.down_music(file_url,file_name)
        self.Internet.addItem(file_name)
    #当地歌曲的加载模块
    def Load_Song(self):
        self.PlayList.clear() #便于网络歌曲加入
        self.Local.clear() #刷新播放列表
        list = os.listdir(self.m_filepath)
        for cur_music in list:
            self.Local.addItem(cur_music)
            self.PlayList.addMedia(QMediaContent(QUrl.fromLocalFile(self.m_filepath + cur_music)))

    #在线歌曲下载模块
    def down_music(self,url,name):
        header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',}
        response = requests.get(url,headers=header)
        with open("{}/{}.mp3".format(self.m_filepath,name),"wb") as file:
            file.write(response.content)
    #用户自定义歌曲模块
    def custom_current_music(self):
        cur_music = self.Local.currentItem().text()
        self.CurMusic.setText(cur_music)
        item = self.Local.currentRow()
        self.PlayList.setCurrentIndex(item)
        self.player.stop() #停止上一首歌
        self.player.play() #开始播放当前指定的歌曲

    #设置音乐播放模式模块
    def music_Mode(self):
        self.PlayList.setPlaybackMode(QMediaPlaylist.CurrentItemInLoop)#单曲循环
        self.PlayList.setPlaybackMode(QMediaPlaylist.Random)  # 随机播放
        self.PlayList.setPlaybackMode(QMediaPlaylist.Sequential)  # 顺序播放

    #重写窗口paintEvent函数
    def paintEvent(self,event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), QPixmap("image/background.jpg"))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    music = music_play()
    music.show()
    sys.exit(app.exec())