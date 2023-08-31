import json  # 导入json模块
import requests  # 导入requests模块
import customtkinter as ctk  # 导入customtkinter模块

ctk.set_appearance_mode("Light")  # 设置外观为Light模式


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # 设置窗口标题
        self.title("笔记导入")  # 设置窗口标题

        # 设置窗口大小
        self.minsize(500, 400)
        self.geometry("500 + 500 + 100 + 10")

        # 创建组件
        self.ip_label = ctk.CTkLabel(master=self, text="请输入ip地址(必填):")  # 创建ip标签
        self.ip_entry = ctk.CTkEntry(master=self)  # 创建ip输入框

        self.title_label = ctk.CTkLabel(master=self, text="请输入书名(必填):")  # 创建书名标签
        self.title_entry = ctk.CTkEntry(master=self)  # 创建书名输入框

        self.author_label = ctk.CTkLabel(master=self, text="请输入作者:")  # 创建作者标签
        self.author_entry = ctk.CTkEntry(master=self)  # 创建作者输入框

        self.translator_label = ctk.CTkLabel(master=self, text="请输入译者:")  # 创建译者标签
        self.translator_entry = ctk.CTkEntry(master=self)  # 创建译者输入框

        self.text_label = ctk.CTkLabel(master=self, text="在这里写原文:")  # 创建原文标签
        self.text_text = ctk.CTkTextbox(master=self)  # 创建原文文本框

        self.note_label = ctk.CTkLabel(master=self, text="在这里写想法:")  # 创建笔记标签
        self.note_text = ctk.CTkTextbox(master=self)  # 创建笔记文本框

        self.publisher_label = ctk.CTkLabel(master=self, text="请输入出版社:")  # 创建出版社标签
        self.publisher_entry = ctk.CTkEntry(master=self)  # 创建出版社输入框

        self.isbn_label = ctk.CTkLabel(master=self, text="请输入图书ISBN:")  # 创建ISBN标签
        self.isbn_entry = ctk.CTkEntry(master=self)  # 创建ISBN输入框

        self.submit_btn = ctk.CTkButton(master=self, text="提交", command=self.submit_note)  # 创建提交按钮并绑定事件

        # 设置布局
        self.grid_columnconfigure(1, weight=1)  # 设置列 1 扩张 比例为 1

        self.ip_label.grid(row=0, column=0, pady=10, padx=10)  # 布局ip标签
        self.ip_entry.grid(row=0, column=1, pady=10, padx=10, sticky="ew")  # 布局ip输入框

        self.title_label.grid(row=1, column=0, pady=10, padx=10)  # 布局书名标签
        self.title_entry.grid(row=1, column=1, pady=10, padx=10, sticky="ew")  # 布局书名输入框

        self.author_label.grid(row=2, column=0, pady=10, padx=10)  # 布局作者标签
        self.author_entry.grid(row=2, column=1, pady=10, padx=10, sticky="ew")  # 布局作者输入框

        self.translator_label.grid(row=3, column=0, pady=10, padx=10)  # 布局译者标签
        self.translator_entry.grid(row=3, column=1, pady=10, padx=10, sticky="ew")  # 布局译者输入框

        self.text_label.grid(row=4, column=0, pady=10, padx=10)  # 布局原文标签
        self.text_text.grid(row=4, column=1, pady=10, padx=10, sticky="ew")  # 布局原文文本框

        self.note_label.grid(row=5, column=0, pady=10, padx=10)  # 布局笔记标签
        self.note_text.grid(row=5, column=1, pady=10, padx=10, sticky="ew")  # 布局笔记文本框

        self.publisher_label.grid(row=6, column=0, pady=10, padx=10)  # 布局出版社标签
        self.publisher_entry.grid(row=6, column=1, pady=10, padx=10, sticky="ew")  # 布局出版社输入框

        self.isbn_label.grid(row=7, column=0, pady=10, padx=10)  # 布局ISBN标签
        self.isbn_entry.grid(row=7, column=1, pady=10, padx=10, sticky="ew")  # 布局ISBN输入框

        self.submit_btn.grid(row=8, column=1, pady=10, padx=10, sticky="e")  # 布局提交按钮

    def submit_note(self):
        # 获取输入
        ip = self.ip_entry.get()  # 获取ip输入
        title = self.title_entry.get()  # 获取书名输入
        author = self.author_entry.get()  # 获取作者输入
        translator = self.translator_entry.get()  # 获取译者输入
        publisher = self.publisher_entry.get()  # 获取出版社输入
        isbn = self.isbn_entry.get()  # 获取ISBN输入
        text = self.text_text.get("1.0", "end")  # 获取原文输入
        note = self.note_text.get("1.0", "end")  # 获取笔记输入

        # 构造数据
        data = {
            "title": title,  # 书名：必填
            # "cover": "https:#img2.doubanio.com/view/subject/l/public/s29707472.jpg",  # 书籍封面：选填
            "author": author,  # 作者：选填
            "translator": translator,  # 译者：选填
            "publisher": publisher,  # 出版社：选填
            # "publishDate": 1519833600,  # 出版日期：单位秒，选填
            "isbn": isbn,  # ISBN：选填
            "type": 1,  # 书籍类型，必填。可取值：0：纸质书；1：电子书
            "locationUnit": 1,  # 书籍页码类型，必填。可取值：0：进度；1：位置；2：页码
            "entries": [{
                "text": text,
                "note": note
            }]
        }

        # 发送请求
        url = 'http://' + ip + ':8080/send'  # 构造请求URL
        # url = 'http://172.31.254.122:8080/send'  # 构造请求URL
        # url = 'http://192.168.124.45:8080/send'  # 公司内网地址
        url = 'http://192.168.1.113:8080/send'  # 公司内网地址

        headers = {'ContentType': 'application/json'}  # 设置请求头

        response = requests.post(url, data=json.dumps(data), headers=headers)  # 发送POST请求

        if response.status_code == 200:  # 判断返回状态码
            print("保存成功!")
            # self.note_text.delete("1.0", "end")  # 清空笔记文本框
        else:
            print("保存失败,请重试")


if __name__ == "__main__":
    app = App()
    app.mainloop()
