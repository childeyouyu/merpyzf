import json

import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLineEdit,
                             QPushButton, QTextEdit, QLabel, QFormLayout, QRadioButton)


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.type = None
        self.paper_book_button = None
        self.ebook_button = None
        self.setWindowTitle('笔记导入')

        layout = QFormLayout()
        self.ipLabel = QLabel('请输入 ip 地址(必填):', self)
        self.ipEdit = QLineEdit()
        layout.addRow(self.ipLabel, self.ipEdit)

        self.titleLabel = QLabel('请输入书名(必填):', self)
        self.titleEdit = QLineEdit()
        layout.addRow(self.titleLabel, self.titleEdit)

        self.authorLabel = QLabel('请输入作者:', self)
        self.authorEdit = QLineEdit()
        layout.addRow(self.authorLabel, self.authorEdit)

        self.translatorLabel = QLabel('请输入译者:', self)
        self.translatorEdit = QLineEdit()
        layout.addRow(self.translatorLabel, self.translatorEdit)

        self.textLabel = QLabel('在这里写原文:', self)
        self.textEdit = QTextEdit()
        layout.addRow(self.textLabel, self.textEdit)

        self.noteLabel = QLabel('在这里写想法:', self)
        self.noteEdit = QTextEdit()
        layout.addRow(self.noteLabel, self.noteEdit)

        self.publisherLabel = QLabel('请输入出版社:', self)
        self.publisherEdit = QLineEdit()
        layout.addRow(self.publisherLabel, self.publisherEdit)

        self.isbnLabel = QLabel("请输入图书ISBN:", self)
        self.isbnEdit = QLineEdit()
        layout.addRow(self.isbnLabel, self.isbnEdit)

        # combo_box = QComboBox(self)
        # combo_box.addItem('纸质书')
        # combo_box.addItem('电子书')
        # combo_box.move(50, 160)
        # layout.addRow(combo_box)

        self.init_ui(layout)

        self.submitBtn = QPushButton('提交')
        self.submitBtn.clicked.connect(self.submit_note)
        layout.addWidget(self.submitBtn)

        self.setLayout(layout)

    def init_ui(self, layout):
        """ 书籍类型 """
        self.paper_book_button = QRadioButton('纸质书')
        self.ebook_button = QRadioButton('电子书')

        layout.addWidget(self.paper_book_button)
        layout.addWidget(self.ebook_button)

        self.setLayout(layout)
        self.setWindowTitle('单选框')

    def clear(self):
        for widget in reversed(self.ui.widgets):
            if isinstance(widget, (QLineEdit, QTextEdit)):
                widget.clear()

    def on_radio_button_clicked(self):

        # 检查单选按钮的被选中状态
        if self.paper_book_button.isChecked():
            self.type = 0
        elif self.ebook_button.isChecked():
            self.type = 1
        # 连接单选按钮的 clicked() 信号
        self.paper_book_button.clicked.connect(self.on_radio_button_clicked)
        self.ebook_button.clicked.connect(self.on_radio_button_clicked)

    def submit_note(self):
        title = self.titleEdit.text()
        author = self.authorEdit.text()
        translator = self.translatorEdit.text()
        publisher = self.publisherEdit.text()
        isbn = self.isbnEdit.text()
        book_type = self.type

        text = self.textEdit.toPlainText()
        note = self.noteEdit.toPlainText()

        data = {
            "title": title,
            "author": author,
            # "cover": "https://img2.doubanio.com/view/subject/l/public/s29707472.jpg",
            "translator": translator,
            "publisher": publisher,
            "publishDate": 1519833600,
            "isbn": isbn,
            "type": book_type,
            "locationUnit": 2,
            "entries": [{
                "page": 100,  # 书籍页码\位置\进度，选填
                "text": "与其苦苦追寻失去的东西，还不如好好珍惜自己眼前拥有的东西。",  # 原文摘录，选填
                "note": note,  # 想法，选填
                # "chapter": "春",  # 章节，选填
                # "time": 1652544669  # 笔记创建日期时间，选填

            }]
        }

        url = 'http://' + self.ipEdit.text() + ':8080/send'

        headers = {'Content-Type': 'application/json'}

        # 在submitNote方法中

        response = requests.post(url, data=json.dumps(data), headers=headers)

        if response.status_code == 200:
            print('保存成功!')
            # self.titleEdit.clear()
            # self.authorEdit.clear()
            self.noteEdit.clear()
        else:
            print('保存失败,请重试')


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
