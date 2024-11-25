# !/usr/local/bin/python3.12
import os
import os.path

# Python3 File(文件) 方法
# open() 方法
# Python open() 方法用于打开一个文件，并返回文件对象。
# 在对文件进行处理过程都需要使用到这个函数，如果该文件无法被打开，会抛出 OSError。
# 注意：使用 open() 方法一定要保证关闭文件对象，即调用 close() 方法。
# open() 函数常用形式是接收两个参数：文件名(file)和模式(mode)。
# open(file, mode='r')
# 完整的语法格式为：
# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
# 参数说明:
# file: 必需，文件路径（相对或者绝对路径）。
# mode: 可选，文件打开模式
# buffering: 设置缓冲
# encoding: 一般使用utf8
# errors: 报错级别
# newline: 区分换行符
# closefd: 传入的file参数类型
# opener: 设置自定义开启器，开启器的返回值必须是一个打开的文件描述符。
# mode 参数有

# 模式	        描述
# 常见模式
# r: 读取模式（默认）。如果文件不存在，会引发 FileNotFoundError。
# w: 写入模式。如果文件已存在，会被截断为零长度；如果文件不存在，会创建新文件。
# a: 追加模式。如果文件已存在，写入的内容会被添加到文件末尾；如果文件不存在，会创建新文件。
# x: 独占创建模式。如果文件已存在，会引发 FileExistsError；如果文件不存在，会创建新文件。
# b: 二进制模式。与上述模式结合使用，例如 'rb' 表示以二进制模式读取文件。
# t: 文本模式（默认）。与上述模式结合使用，例如 'rt' 表示以文本模式读取文件。
# +: 更新模式。与上述模式结合使用，表示同时支持读写操作，例如 'r+' 表示读写模式，文件指针位于文件开头。
# 组合模式
# r+: 读写模式，文件指针位于文件开头。
# w+: 读写模式，如果文件已存在，会被截断为零长度；如果文件不存在，会创建新文件。
# a+: 读写模式，如果文件已存在，写入的内容会被添加到文件末尾；如果文件不存在，会创建新文件。

# 默认为文本模式，如果要以二进制模式打开，加上 b 。

print("*******************************************【1】 file 对象 *******************************************")
# ile 对象使用 open 函数来创建，下表列出了 file 对象常用的函数：
# 方法                                    描述
# file.close()                          关闭文件。关闭后文件不能再进行读写操作。
# file.flush()                          刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入。
# file.fileno()                         返回一个整型的文件描述符(file descriptor FD 整型), 可以用在如os模块的read方法等一些底层操作上。
# file.isatty()                         如果文件连接到一个终端设备返回 True，否则返回 False。
# file.next()                           Python 3 中的 File 对象不支持 next() 方法。返回文件下一行。
# file.read([size])                     从文件读取指定的字节数，如果未给定或为负则读取所有。
# file.readlines([sizeint])             读取所有行并返回列表，若给定sizeint>0，返回总和大约为sizeint字节的行, 实际读取值可能比 sizeint 较大, 因为需要填充缓冲区。
# file.seek(offset[, whence])           移动文件读取指针到指定位置
# file.tell()                           返回文件当前位置。
# file.truncate([size])                 从文件的首行首字符开始截断，截断文件为 size 个字符，无 size 表示从当前位置截断；截断之后后面的所有字符被删除，其中 windows 系统下的换行代表2个字符大小。
# file.write(str)                       将字符串写入文件，返回的是写入的字符长度。
# file.writelines(sequence)             向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。


print("*******************************************【2】 笔记 *******************************************")
# 检索指定路径下后缀是 py 的所有文件：

path = '/Users/liuchao/Desktop'
ls = []


def getAppointFile(path, ls):
    fileList = os.listdir(path)
    try:
        for tmp in fileList:
            pathTmp = os.path.join(path, tmp)
            if True == os.path.isdir(pathTmp):
                getAppointFile(pathTmp, ls)
            elif pathTmp[pathTmp.rfind('.') + 1:].upper() == 'PY':
                ls.append(pathTmp)
    except PermissionError:
        pass


def main():
    while True:
        path = input('请输入路径:').strip()
        if os.path.isdir(path) == True:
            break

    getAppointFile(path, ls)
    print("py文件数量:",len(ls))
    print(ls)


main()
