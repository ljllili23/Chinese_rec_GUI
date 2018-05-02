# -*- coding: utf-8 -*-
"""
Created on 2018/4/20

@author: LeeJiangLee
"""
from PyQt5.QtWidgets import (QMainWindow, QLineEdit, QAction, QFileDialog, QApplication, QPushButton, QHBoxLayout, QVBoxLayout, QLabel,QWidget,QMessageBox,QFrame)
from PyQt5.QtGui import QIcon, QPixmap, QFont, QPalette, QBrush, QColor
from PyQt5.QtCore import Qt
import sys
import chinese_rec
import pickle

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.ansPredict_1 = 100
        self.ansPredict_2 = 0
        self.ansPredict_3 = 0
        self.myFileStr = '../data/test/00999/223400.png'  # 这是inference的输入
        self.ans = '帆'  # 这是inference的结果
        self.LineEdit = QLineEdit(self.myFileStr)
        self.okButton = QPushButton("OK")
        self.okButton.clicked.connect(self.showAns)
        self.openButton = QPushButton("...")
        self.openButton.clicked.connect(self.showDialog)
        self.openButton.setFixedSize(23,23)
        pixmap = QPixmap(self.myFileStr,'wr')
        self.graphLabel = QLabel()
        self.graphLabel.setPixmap(pixmap)
        self.graphLabel.setScaledContents(True)
        self.graphLabel.setFixedSize(268,268)
        self.graphLabel.setAlignment(Qt.AlignCenter)
        self.graphText = QLabel()
        self.graphText.setText('原始图片：')
        self.graphText.setFont(QFont("ZhongSong", 20, QFont.Bold))

        self.ansLabel_1 = QLabel(self.ans)
        self.ansLabel_1.setFont(QFont("ZhongSong", 100, QFont.Bold))
        # palette = QPalette()
        # palette.setBrush(self.backgroundRole(),QBrush(pixmap))
        # self.ansLabel_1.setPalette(palette)
        #self.ansLabel_1.setStyleSheet("border:2px")
        # palette_1 = QPalette()
        # palette_1.setColor(self.backgroundRole(), QColor(0, 0, 0))
        # self.setPalette(palette_1)
        #self.ansLabel_1.setScaledContents(True)
        self.ansLabel_1.setFixedSize(268,268)
        self.ansLabel_1.setAlignment(Qt.AlignCenter)
        # palette_2 = QPalette()
        # palette_2.setColor(self.backgroundRole(),QColor(255,255,255))
        # self.ansLabel_1.setPalette(palette_2)
        self.ansLabel_1.setStyleSheet('QLabel{border-image:url(background.jpg);}')

        self.ansText_11 = QLabel()
        self.ansText_11.setText("识别结果1：")
        self.ansText_11.setFont(QFont("ZhongSong", 20, QFont.Bold))
        self.ansText_12 = QLabel()
        self.ansText_12.setText("可能性：{0}%".format(self.ansPredict_1))
        self.ansText_12.setFont(QFont("ZhongSong", 20, QFont.Bold))
        self.vbox_1 = QVBoxLayout()
        self.vbox_1.addWidget(self.ansText_11)
        self.vbox_1.addWidget(self.ansText_12)

        self.ansLabel_2 = QLabel()
        self.ansLabel_2.setFixedSize(268, 268)
        # self.ansLabel_2.setScaledContents(True)
        self.ansLabel_2.setAlignment(Qt.AlignCenter)
        self.ansLabel_2.setStyleSheet('border-image:url(background.jpg)')

        self.ansText_21 = QLabel()
        self.ansText_21.setText("识别结果2：")
        self.ansText_21.setFont(QFont("ZhongSong", 20, QFont.Bold))
        self.ansText_22 = QLabel()
        self.ansPredict_1 = 100
        self.ansText_22.setText("可能性：{0}%".format(self.ansPredict_2))
        self.ansText_22.setFont(QFont("ZhongSong", 20, QFont.Bold))
        self.vbox_2 = QVBoxLayout()
        self.vbox_2.addWidget(self.ansText_21)
        self.vbox_2.addWidget(self.ansText_22)

        self.ansLabel_3 = QLabel()
        #self.ansLabel_3.setFont(QFont("ZhongSong", 100, QFont.Bold))
        self.ansLabel_3.setFixedSize(268, 268)
        self.ansLabel_3.setAlignment(Qt.AlignCenter)
        self.ansLabel_3.setStyleSheet("QLabel{background-image:url(background.jpg)}")

        self.ansText_31 = QLabel()
        self.ansText_31.setText("识别结果3：")
        self.ansText_31.setFont(QFont("ZhongSong", 20, QFont.Bold))
        self.ansText_32 = QLabel()
        self.ansPredict_1 = 100
        self.ansText_32.setText("可能性：{0}%".format(self.ansPredict_3))
        self.ansText_32.setFont(QFont("ZhongSong", 20, QFont.Bold))
        self.vbox_3 = QVBoxLayout()
        self.vbox_3.addWidget(self.ansText_31)
        self.vbox_3.addWidget(self.ansText_32)

        hbox_1 = QHBoxLayout()
        hbox_1.addWidget(self.LineEdit)
        hbox_1.addWidget(self.openButton)
        # hbox_1.addStretch(1)
        hbox_1.addWidget(self.okButton)

        hbox_2 = QHBoxLayout()
        hbox_2.addWidget(self.graphText)
        #hbox_2.addSpacing(30)
        hbox_2.addWidget(self.graphLabel)
        #hbox_2.addSpacing(30)

        hbox_3 = QHBoxLayout()
        hbox_3.addLayout(self.vbox_1)
        hbox_3.addWidget(self.ansLabel_1)
        # hbox_2.addStretch(1)
        #hbox_2.addWidget(self.ansLabel)

        hbox_4 = QHBoxLayout()
        hbox_4.addLayout(self.vbox_2)
        hbox_4.addWidget(self.ansLabel_2)

        hbox_5 = QHBoxLayout()
        hbox_5.addLayout(self.vbox_3)
        hbox_5.addWidget(self.ansLabel_3)
        vbox = QVBoxLayout()
        vbox.addLayout(hbox_1)
        vbox.addSpacing(30)
        vbox.addLayout(hbox_2)
        #vbox.addSpacing(30)
        vbox.addLayout(hbox_3)
        vbox.addLayout(hbox_4)
        vbox.addLayout(hbox_5)

        self.setLayout(vbox)

        self.setGeometry(200,200,294,1100)
        self.setWindowTitle("手写汉字识别")
        self.setWindowIcon(QIcon('feather-pencil-512.png'))
        self.show()

    def showDialog(self):

        fname = QFileDialog.getOpenFileName(self, 'Open file', '../data/test/')

        if fname[0]:
            # print(fname)
            f = open(fname[0], 'r')
            self.myFileStr = fname[0]
            self.LineEdit.setText(fname[0])
            pixmap = QPixmap(self.myFileStr)
            self.graphLabel.setPixmap(pixmap)
            print(self.myFileStr)

    def showAns(self):
        # QApplication.processEvents()
        final_predict_val, final_predict_index = chinese_rec.inference(self.myFileStr)
        # logger.info('the result info label {0} predict index {1} predict_val {2}'.format(190, final_predict_index,final_predict_val))
        # print(final_predict_index)
        # print(final_predict_index[0][0])
        ansIndex_1=final_predict_index[0][0]
        ansIndex_2=final_predict_index[0][1]
        ansIndex_3=final_predict_index[0][2]
        #print(final_predict_val)
        self.ansPredict_1 = final_predict_val[0][0]*100
        self.ansPredict_2 = final_predict_val[0][1]*100
        self.ansPredict_3 = final_predict_val[0][2]*100
        f = open('D:\TFRECORD\data\char_dict','rb')
        charDict = pickle.load(f)
        # print(charDict)
        f.close()
        self.ans_1 = list(charDict.keys())[list(charDict.values()).index(ansIndex_1)]
        self.ans_2 = list(charDict.keys())[list(charDict.values()).index(ansIndex_2)]
        self.ans_3 = list(charDict.keys())[list(charDict.values()).index(ansIndex_3)]
        self.ansLabel_1.setText(self.ans_1)
        self.ansLabel_1.setFont(QFont("ZhongSong", 100, QFont.Bold))
        # self.ansLabel_1.setFrameShape(QFrame.Panel)
        # self.ansLabel_1.setFrameShadow(QFrame.Sunken)
        # self.ansLabel_1.setLineWidth(3)
        self.ansLabel_2.setText(self.ans_2)
        self.ansLabel_2.setFont(QFont("ZhongSong", 100, QFont.Bold))
        self.ansLabel_3.setText(self.ans_3)
        self.ansLabel_3.setFont(QFont("ZhongSong", 100, QFont.Bold))

        self.ansText_12.setText("可能性：{:.2f}%".format(self.ansPredict_1))
        self.ansText_22.setText("可能性：{:.2f}%".format(self.ansPredict_2))
        self.ansText_32.setText("可能性：{:.2f}%".format(self.ansPredict_3))


        #return self.ans
        # for key, value in charDict.items():
        #     print(key)
        #     if value == final_predict_index[0]:
        #
        #         self.ans= key
        #         self.ansLabel.setText(self.ans)


# class ansWindow(QWidget):
#     def __init__(self,ans):
#         super().__init__()
#         self.resize(200,200)
#         self.ans=ans
#     def handle_click(self):
#         self.ansLabel = QLabel(self.ans)
#         self.ansLabel.setScaledContents(True)
#         self.ansLabel.setFont(QFont("ZhongSong", 100, QFont.Bold))
#         self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MyWindow()
    #ans = mainWindow.showAns()
    #popWindow = ansWindow(ans)
    #mainWindow.okButton.clicked.connect(popWindow.handle_click)
    # mainWindow.show()
    sys.exit(app.exec_())