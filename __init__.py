import requests
import json
from PyQt5.QtWidgets import (QApplication, QWidget, QLineEdit,
                             QPushButton, QTextEdit, QVBoxLayout)


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('笔记导入')

        self.titleEdit = QLineEdit()
        self.authorEdit = QLineEdit()
        self.noteEdit = QTextEdit()

        self.submitBtn = QPushButton('提交')
        self.submitBtn.clicked.connect(self.submitNote)

        layout = QVBoxLayout()
        layout.addWidget(self.titleEdit)
        layout.addWidget(self.authorEdit)
        layout.addWidget(self.noteEdit)
        layout.addWidget(self.submitBtn)

        self.setLayout(layout)

    def submitNote(self):
        title = self.titleEdit.text()
        author = self.authorEdit.text()
        note = self.noteEdit.toPlainText()

        data = {
            "title": title,
            "author": author,
            "type": 1,
            "locationUnit": 1,
            "entries": [{
                "note": note
            }]
        }

        url = 'http://192.168.124.39:8080/send'

        headers = {'Content-Type': 'application/json'}

        # 在submitNote方法中

        response = requests.post(url, data=json.dumps(data), headers=headers)

        if response.status_code == 200:
            print('保存成功!')
            self.titleEdit.clear()
            self.authorEdit.clear()
            self.noteEdit.clear()
        else:
            print('保存失败,请重试')


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
