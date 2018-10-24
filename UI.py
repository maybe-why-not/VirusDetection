# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
import os


class filedialogdemo(QWidget):

    def __init__(self, parent=None):
        super(filedialogdemo, self).__init__(parent)
        layout = QVBoxLayout()

        self.myButton = QtWidgets.QPushButton(self)
        self.myButton.setObjectName("myButton")
        self.myButton.setText("选择exe文件")
        self.myButton.clicked.connect(self.load_text)
        layout.addWidget(self.myButton)
		
		# self.label = QLabel()
		# layout.addWidget(self.label)
        self.content = QTextEdit()
        layout.addWidget(self.content)
		
        self.setWindowTitle("恶意代码检测")

        self.setLayout(layout)

# 这个函数是打开文本选择器，加载文本的函数
    def load_text(self):
        print("load--text")
        fileName, filetype = QFileDialog.getOpenFileName(self,
                                    "选取文件",
                                    "/",
                                    "All Files(*)")   #设置文件扩展名过滤,用双分号间隔

        command = 'python3 D:\\004实训资料\\实验\\VirusDetection-2.0.py -f' + fileName + ' -v' #可以直接在命令行中执行的命令
        r = os.popen(command) #执行该命令
        info = r.read()  #读取命令行的输出到一个list	
        data = ''.join(info)  #list转化为str
		
        self.content.clear()  #刷新
        if '1' in info.split('\t')[-1]:
            print(fileName)
            print(fileName.replace('/', '\\\\'))
            #os.remove(fileName.replace('/', '\\\\'))
            self.content.setText(data+'恶意代码文件 '+fileName+' 已被删除！') #载入str
        else:
            self.content.setText(data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    fileload =  filedialogdemo()
    fileload.show()
    sys.exit(app.exec_())