import os
import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal, QDateTime, QUrl
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer, QMediaPlaylist
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QApplication
import time
import sys
import pymysql
import json
from urllib.request import urlretrieve


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


class search_song(QThread):
    song = pyqtSignal(object)   #str表示要返回的每个参数的类型

    def __init__(self,music_name,musician_name):
        super(search_song,self).__init__()
        self.music_name = music_name
        self.musician_name = musician_name

    def run(self):
        self.SaveData = db()
        music_data = self.SaveData.get_data(self.musician_name, self.music_name)
        self.SaveData.close_DB()
        self.song.emit(music_data)

class download_song(QThread):
    song = pyqtSignal()   #str表示要返回的每个参数的类型,可以有多个

    def __init__(self,music_name,music_author,music_url):
        super(download_song,self).__init__()
        self.music_name = music_name
        self.music_author = music_author
        self.music_url = music_url

    def run(self):
        urlretrieve(self.music_url,'E:/MusicMedia/MusicMedia/music/{} - {}.mp3'.format(self.music_name,self.music_author))
        # self.song.emit()    #由于不需要数据的传输，因此可以不用发送信号

class download_song2(QThread):
    song = pyqtSignal(object)   #str表示要返回的每个参数的类型,可以有多个

    def __init__(self,name,author):
        super(download_song2,self).__init__()
        self.name = name
        self.author = author

    def run(self):
        url = 'https://daga.cc/yue/'
        header = {'origin': 'https://daga.cc',
                  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
                  'x-requested-with': 'XMLHttpRequest', }
        postData = {'input': self.name,
                    'filter': 'name',
                    'type': 'netease',
                    'page': '1', }
        response = requests.post(url, data=postData, headers=header)
        response = response.json()
        list = response['data']
        # 只需要获取其中一条信息即可
        for item in list:
            if item['author'] == self.author:
                music_title = item['title']
                music_author = item['author']
                music_url = item['url']
                music_data = {'title': music_title, 'author': music_author, 'url': music_url}
                self.song.emit(music_data)


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1005, 599)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30, 80, 111, 28))
        self.pushButton.setObjectName("pushButton")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(30, 150, 441, 321))
        self.listWidget.setObjectName("listWidget")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(840, 80, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.listWidget_2 = QtWidgets.QListWidget(Form)
        self.listWidget_2.setGeometry(QtCore.QRect(480, 150, 471, 311))
        self.listWidget_2.setObjectName("listWidget_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(530, 80, 113, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(710, 80, 113, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(480, 84, 41, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(660, 80, 41, 21))
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(350, 80, 111, 28))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton_2.clicked.connect(Form.search)
        self.pushButton.clicked.connect(Form.load_Local)
        self.listWidget.clicked.connect(Form.custom_current_music)  # 当用户自己点击的时候触发,播放歌曲
        self.pushButton_3.clicked.connect(Form.delete_song) #将解码器不支持的歌曲从列表中删除

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "导入本地歌曲"))
        self.pushButton_2.setText(_translate("Form", "在线歌曲"))
        self.label.setText(_translate("Form", "音乐:"))
        self.label_2.setText(_translate("Form", "歌手:"))
        self.pushButton_3.setText(_translate("Form", "删除歌曲"))

class play(QMainWindow,Ui_Form):
    def __init__(self):
        super(play,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("VIP音乐播放器")
        self.m_filepath = 'E:/MusicMedia/MusicMedia/music/'
        # self.m_filepath = 'E:/ProgramData/PyUI/music'
        self.player = QMediaPlayer()
        self.PlayList = QMediaPlaylist()
        self.player.setPlaylist(self.PlayList)
        self.count = 0  #做一个计数器

    def search(self):
        self.listWidget_2.clear()
        music = self.lineEdit.text()  #地心
        author = self.lineEdit_2.text() #汪峰
        self.music = search_song(music, author)
        self.music.song.connect(self.get_music)
        # 启动线程
        self.music.start()

    def get_music(self,data):
        if data != None:
            music = self.lineEdit.text()  # 地心
            self.listWidget_2.addItem("{} - {}".format(data[0],data[1]))
            #启动下载歌曲的线程
            self.dowm = download_song(music,data[1],data[2])
            # self.music.song.connect(self.music_dowm)   #没有信号的发送这里也可以不用定义槽函数
            self.dowm.start()
        else:
            music = self.lineEdit.text()  # 地心
            author = self.lineEdit_2.text()  # 汪峰
            # 启动下载歌曲的线程
            self.Intel = download_song2(music,author)
            self.Intel.song.connect(self.Intelnet_song)
            self.Intel.start()
    def Intelnet_song(self,data):
        self.listWidget_2.addItem("{} - {}".format(data['title'], data['author']))
        # 启动下载歌曲的线程
        self.dowm = download_song(data['title'], data['author'], data['url'])
        self.dowm.start()

    def load_Local(self):
        if self.count == 0:
            self.PlayList.clear()  # 便于网络歌曲加入
            self.listWidget.clear()  # 刷新播放列表
            list = os.listdir(self.m_filepath)
            for cur_music in list:
                self.listWidget.addItem(cur_music[:-4])
                self.PlayList.addMedia(QMediaContent(QUrl.fromLocalFile(self.m_filepath + cur_music)))
            self.count += 1
        else:
            cur_music = self.listWidget_2.currentItem().text()
            row = self.listWidget.currentRow()
            self.listWidget.insertItem(row,cur_music)
            self.listWidget_2.clear()  # 清空在线的列表，造成一种从左边移动到右边的视觉
            self.PlayList.addMedia(QMediaContent(QUrl.fromLocalFile(self.m_filepath + cur_music+'.mp3')))
    def custom_current_music(self):
        cur_music = self.listWidget.currentItem().text() #获取当前播放的歌曲的名字
        item = self.listWidget.currentRow()
        self.PlayList.setCurrentIndex(item)
        self.player.play()  # 开始播放当前指定的歌曲
    def delete_song(self):
        cur_music = self.listWidget.currentItem().text()
        os.remove(self.m_filepath+cur_music+'.mp3')  #从磁盘上删除
        row = self.listWidget.currentRow() #获取当前鼠标所选行
        self.listWidget.takeItem(row) #从列表上删除该行
        self.PlayList.next() #歌曲列表顺势往下
        self.player.play() #播放

    # 重写窗口paintEvent函数
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), QPixmap("image/back.jpg"))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = play()
    example.show()
    sys.exit(app.exec())