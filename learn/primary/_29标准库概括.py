# !/usr/local/bin/python3.12
# Python3 标准库概览
# Python 标准库非常庞大，所提供的组件涉及范围十分广泛，使用标准库我们可以让您轻松地完成各种任务。
# 以下是一些 Python3 标准库中的模块：
# os 模块：os 模块提供了许多与操作系统交互的函数，例如创建、移动和删除文件和目录，以及访问环境变量等。
# sys 模块：sys 模块提供了与 Python 解释器和系统相关的功能，例如解释器的版本和路径，以及与 stdin、stdout 和 stderr 相关的信息。
# time 模块：time 模块提供了处理时间的函数，例如获取当前时间、格式化日期和时间、计时等。
# datetime 模块：datetime 模块提供了更高级的日期和时间处理函数，例如处理时区、计算时间差、计算日期差等。
# random 模块：random 模块提供了生成随机数的函数，例如生成随机整数、浮点数、序列等。
# math 模块：math 模块提供了数学函数，例如三角函数、对数函数、指数函数、常数等。
# re 模块：re 模块提供了正则表达式处理函数，可以用于文本搜索、替换、分割等。
# json 模块：json 模块提供了 JSON 编码和解码函数，可以将 Python 对象转换为 JSON 格式，并从 JSON 格式中解析出 Python 对象。
# urllib 模块：urllib 模块提供了访问网页和处理 URL 的功能，包括下载文件、发送 POST 请求、处理 cookies 等。

print("【1】 操作系统接口 *******************************************")
# os 模块提供了不少与操作系统相关联的函数，例如文件和目录的操作。
import os

# 获取当前工作目录
current_dir = os.getcwd()
print("当前工作目录:", current_dir)

# 列出目录下的文件
files = os.listdir(current_dir)
print("目录下的文件:", files)

# 建议使用 import os 风格而非 from os import *，这样可以保证随操作系统不同而有所变化的 os.open() 不会覆盖内置函数 open()。
# 在使用 os 这样的大型模块时内置的 dir() 和 help() 函数非常有用:
import os

dir(os)
help(os)

# 针对日常的文件和目录管理任务，:mod:shutil 模块提供了一个易于使用的高级接口:
import shutil

shutil.copyfile('data.db', 'archive.db')
shutil.move('/build/executables', 'installdir')

print("【2】 文件通配符 *******************************************")
# glob 模块提供了一个函数用于从目录通配符搜索中生成文件列表:
import glob

print(glob.glob('*.py'))

print("【3】 命令行参数 *******************************************")
# 通用工具脚本经常调用命令行参数。这些命令行参数以链表形式存储于 sys 模块的 argv 变量。例如在命令行中执行 "python demo.py one two three" 后可以得到以下输出结果:
import sys

print(sys.argv)

print("【4】 错误输出重定向和程序终止 *******************************************")
# sys 还有 stdin，stdout 和 stderr 属性，即使在 stdout 被重定向时，后者也可以用于显示警告和错误信息。
sys.stderr.write('Warning, log file not found starting a new one\n')
# 大多脚本的定向终止都使用 sys.exit()。

print("【5】 字符串正则匹配 *******************************************")
# re 模块为高级字符串处理提供了正则表达式工具。对于复杂的匹配和处理，正则表达式提供了简洁、优化的解决方案:
import re

print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))
# 如果只需要简单的功能，应该首先考虑字符串方法，因为它们非常简单，易于阅读和调试:
print('tea for too'.replace('too', 'two'))

print("【6】 数学 *******************************************")
# math 模块为浮点运算提供了对底层 C 函数库的访问:
import math

print(math.cos(math.pi / 4))
print(math.log(1024, 2))

# random 提供了生成随机数的工具。
import random

print(random.choice(['apple', 'pear', 'banana']))
print(random.sample(range(100), 10))  # sampling without replacement
print(random.random())  # random float
print(random.randrange(6))  # random integer chosen from range(6)

print("【7】 访问 互联网 *******************************************")
# 有几个模块用于访问互联网以及处理网络通信协议。其中最简单的两个是用于处理从 urls 接收的数据的 urllib.request 以及用于发送电子邮件的 smtplib:
from urllib.request import urlopen

for line in urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
    line = line.decode('utf-8')  # Decoding the binary data to text.
if 'EST' in line or 'EDT' in line:  # look for Eastern Time
    print(line)

import smtplib

server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
                """To: jcaesar@example.org
               ... From: soothsayer@example.org
               ...
               ... Beware the Ides of March.
               ... """)
server.quit()
# 注意第二个例子需要本地有一个在运行的邮件服务器。

print("【8】 日期和时间 *******************************************")
# datetime 模块为日期和时间处理同时提供了简单和复杂的方法。
# 支持日期和时间算法的同时，实现的重点放在更有效的处理和格式化输出。
import datetime

# 获取当前日期和时间
current_datetime = datetime.datetime.now()
print(current_datetime)

# 获取当前日期
current_date = datetime.date.today()
print(current_date)

# 格式化日期
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_datetime)  # 输出：2023-07-17 15:30:45

# 该模块还支持时区处理:
# 导入了 datetime 模块中的 date 类
from datetime import date

now = date.today()  # 当前日期
print(now)
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))

# 创建了一个表示生日的日期对象
birthday = date(1964, 7, 31)
age = now - birthday  # 计算两个日期之间的时间差
print(age.days)  # 变量age的days属性，表示时间差的天数

print("【9】 数据压缩 *******************************************")
# 以下模块直接支持通用的数据打包和压缩格式：zlib，gzip，bz2，zipfile，以及 tarfile。
import zlib

s = b'witch which has which witches wrist watch'
print(len(s))
t = zlib.compress(s)
print(len(t))
print(zlib.decompress(t))
print(zlib.crc32(s))

print("【10】 性能度量 *******************************************")
# 有些用户对了解解决同一问题的不同方法之间的性能差异很感兴趣。Python 提供了一个度量工具，为这些问题提供了直接答案。
# 例如，使用元组封装和拆封来交换元素看起来要比使用传统的方法要诱人的多,timeit 证明了现代的方法更快一些。
from timeit import Timer

print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
print(Timer('a,b = b,a', 'a=1; b=2').timeit())

print("【11】 测试模块 *******************************************")


# 开发高质量软件的方法之一是为每一个函数开发测试代码，并且在开发过程中经常进行测试
# doctest模块提供了一个工具，扫描模块并根据程序中内嵌的文档字符串执行测试。
# 测试构造如同简单的将它的输出结果剪切并粘贴到文档字符串中。
# 通过用户提供的例子，它强化了文档，允许 doctest 模块确认代码的结果是否与文档一致:
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)


import doctest

doctest.testmod()  # 自动验证嵌入测试

# unittest模块不像 doctest模块那么容易使用，不过它可以在一个独立的文件里提供一个更全面的测试集:
import unittest


class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        self.assertRaises(ZeroDivisionError, average, [])
        self.assertRaises(TypeError, average, 20, 30, 70)


unittest.main()  # Calling from the command line invokes all tests

# 以上我们看到的只是 Python3 标准库中的一部分模块，还有很多其他模块可以在官方文档中查看完整的标准库文档：https://docs.python.org/zh-cn/3/library/index.html

print("【12】 笔记 *******************************************")
# 关于urlopen的补充

# 处理get请求，不传data，则为get请求

import urllib
from urllib.request import urlopen
from urllib.parse import urlencode

url = 'http://www.xxx.com/login'
data = {"username": "admin", "password": 123456}
req_data = urlencode(data)  # 将字典类型的请求数据转变为url编码
res = urlopen(url + '?' + req_data)  # 通过urlopen方法访问拼接好的url
res = res.read().decode()  # read()方法是读取返回数据内容，decode是转换返回数据的bytes格式为str

print(res)
# 处理post请求,如果传了data，则为post请求

import urllib
from urllib.request import Request
from urllib.parse import urlencode

url = 'http://www.xxx.com/login'
data = {"username": "admin", "password": 123456}
data = urlencode(data)  # 将字典类型的请求数据转变为url编码
data = data.encode('ascii')  # 将url编码类型的请求数据转变为bytes类型
req_data = Request(url, data)  # 将url和请求数据处理为一个Request对象，供urlopen调用
with urlopen(req_data) as res:
    res = res.read().decode()  # read()方法是读取返回数据内容，decode是转换返回数据的bytes格式为str

print(res)

# 时间和日期补充
# 常用时间处理方法

# 今天                    today = datetime.date.today()
# 昨天                     yesterday = today - datetime.timedelta(days=1)
# 上个月                   last_month = today.month - 1 if today.month - 1 else 12
# 当前时间戳                time_stamp = time.time()
# 时间戳转datetime          datetime.datetime.fromtimestamp(time_stamp)
# datetime转时间戳          int(time.mktime(today.timetuple()))
# datetime转字符串          today_str = today.strftime("%Y-%m-%d")
# 字符串转datetime          today = datetime.datetime.strptime(today_str, "%Y-%m-%d")
# 补时差                   today + datetime.timedelta(hours=8)
