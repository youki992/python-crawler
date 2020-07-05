from tkinter import *
from urllib.request import urlopen  # 注意这里的写法urllib不能直接写为import urllib要加上它的对象request
from bs4 import BeautifulSoup
import re
import time
import urllib.request


def input1():
    url = str(inp1.get())
    html = urllib.request.urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    # 是指定Beautiful的解析器为“html.parser”还有BeautifulSoup(markup,“lxml”)BeautifulSoup(markup, “lxml-xml”) BeautifulSoup(markup,“xml”)等等很多种
    # 用Beautiful Soup结合正则表达式来提取包含所有图片链接（img标签中，class=**，以.png结尾的链接）的语句
    # find()查找第一个匹配结果出现的地方，find_all()找到所有匹配结果出现的地方
    # re模块中包含一个重要函数是compile(pattern [, flags]) ，该函数根据包含的正则表达式的字符串创建模式对象。可以实现更有效率的匹配。
    links = soup.find_all('img', "", src=re.compile('.*(.jpg|.png|.jpeg)$'))

    # 设置保存图片的路径，否则会保存到程序当前路径
    path = r'C:/Users/ASUS/desktop/images/'  # 路径前的r是保持字符串原始值的意思，就是说不对其中的符号进行转义
    for link in links:  # 使用attrs 获取标签属性
        # 保存链接并命名，time.time()返回当前时间戳防止命名冲突
        # urlretrieve()方法直接将远程数据下载到本地
        # urlretrieve(url, filename=None, reporthook=None, data=None)
        urllib.request.urlretrieve(link.attrs['src'],
                                   path + '\%s.png' % time.time())  # 使用request.urlretrieve直接将所有远程链接数据下载到本地
        txt.insert(END, '已爬取 ' + link.attrs['src'] + '\n')
        txt.update()
    txt.insert(END, '\n' + '\n')  # 文本最后插入
    txt.insert(END, '保存成功！保存路径：' + path)
    inp1.delete(0, END)


root = Tk()
root.geometry('460x240')
root.title('爬取图片界面')

lb1 = Label(root, text='请输入需要爬取的网页')
lb1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)
inp1 = Entry(root)
inp1.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.1)


# 方法
btn1 = Button(root, text='开始爬取', command=input1)
btn1.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.2)

# 在窗体垂直自上而下位置60%处起，布局相对窗体高度40%高的文本框
txt = Text(root)
txt.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.4)
root.mainloop()
