# !/usr/local/bin/python3.12
# Python3 基础语法

# 1、编码
# 默认情况下，Python 3 源码文件以 UTF-8 编码，所有字符串都是 unicode 字符串。 当然你也可以为源码文件指定不同的编码：
# -*- coding: cp-1252 -*-
# 上述定义允许在源文件中使用 Windows-1252 字符集中的字符编码，对应适合语言为保加利亚语、白俄罗斯语、马其顿语、俄语、塞尔维亚语。

# 2、标识符
# 第一个字符必须是字母表中字母或下划线 _ 。
# 标识符的其他的部分由字母、数字和下划线组成。
# 标识符对大小写敏感。
# 在 Python 3 中，可以用中文作为变量名，非 ASCII 标识符也是允许的了。

# 3、python保留字
# 保留字即关键字，我们不能把它们用作任何标识符名称。Python 的标准库提供了一个 keyword 模块，可以输出当前版本的所有关键字：
import keyword

print(keyword.kwlist)
print(len(keyword.kwlist))
# 35个关键字 只有 False、None、True  首字母大写 其余都是小写


# 4、注释
# Python中单行注释以 # 开头
# 第一个注释
print("Hello, Python!")  # 第二个注释
# 多行注释可以用多个 # 号，还有 ''' 和 """：
'''
第三注释
第四注释
'''

"""
第五注释
第六注释
"""
print("Hello, Python!")

# 5、行与缩进
# python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {} 。
# 缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数。实例如下：
if True:
    print("True")
else:
    print("False")
# 缩进不一致，执行后会出现类似以下错误：
# IndentationError: unindent does not match any outer indentation level

# 6、多行语句
# Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠 \ 来实现多行语句，例如：
total = 'item_one' + \
        'item_two' + \
        'item_three'
print(total)
# 在 [], {}, 或 () 中的多行语句，不需要使用反斜杠 \，例如：
total = ['item_one', 'item_two', 'item_three',
         'item_four', 'item_five']
print(total)

# 7、数字(Number)类型
# python中数字有四种类型：整数、布尔型、浮点数和复数。
# int (整数), 如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
# bool (布尔), 如 True。
# float (浮点数), 如 1.23、3E-2
# complex (复数) - 复数由实部和虚部组成，形式为 a + bj，其中 a 是实部，b 是虚部，j 表示虚数单位。如 1 + 2j、 1.1 + 2.2j
print(3E-2)
print(0.03)
print(3E-2 == 0.03)

print(1 + 2j)
print(1.1 + 2.2j)

# 8、字符串(String)类型
# Python 中单引号 ' 和双引号 " 使用完全相同。
# 使用三引号(''' 或 """)可以指定一个多行字符串。
# 转义符 \。
# 反斜杠可以用来转义，使用 r 可以让反斜杠不发生转义。 如 r"this is a line with \n" 则 \n 会显示，并不是换行。
# 按字面意义级联字符串，如 "this " "is " "string" 会被自动转换为 this is string。
# 字符串可以用 + 运算符连接在一起，用 * 运算符重复。
# Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
# Python 中的字符串不能改变。
# Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
# 字符串切片 str[start:end]，其中 start（包含）是切片开始的索引，end（不包含）是切片结束的索引。
# 字符串的切片可以加上步长参数 step，语法格式如下：str[start:end:step]
word = "字符串"
sentence = "这是一个句子"
paragraph = """这是一个段落，
可以换行。"""
str = "123456789"
print(str)  # 输出字符串
print(str[0:-1])  # 从第一个开始到倒数第二个元素前输出
print(str[::2])  # 输出字符串的偶数位置字符
print(str[1::2])  # 输出字符串的奇数位置字符
print(str[2:5])  # 输出从第三个开始到第五个的字符串
print(str[::-1])  # 输出字符串反向
print(str[2:])  # 输出从第三个开始后的字符串
print(str[:-2])  # 输出从第一个开始到倒数第二个的字符串
print(str[1:5:2])  # 输出从第二个开始到第五个，步长为2的字符串
print(str * 2)  # 输出字符串两次
print(str + "你好")  # 连接字符串
print("------------------------------")
print("hello\nworld")  # 换行符
print(r"hello\nworld")  # 不转义

# 9、空行
# 函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。
# 空行与代码缩进不同，空行并不是 Python 语法的一部分。书写时不插入空行，Python 解释器运行也不会出错。但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。
# 记住：空行也是程序代码的一部分。

# 10、等待用户输入
# 执行下面的程序在按回车键后就会等待用户输入：
input("\n\n按下enter 键后退出")
# 以上代码中 ，\n\n 在结果输出前会输出两个新的空行。一旦用户按下 enter 键时，程序将退出。

# 11、同一行显示多条语句
import sys;

x = 'runoob';
sys.stdout.write(x + '\n')

# 12、多个语句构成代码组
# 缩进相同的一组语句构成一个代码块，我们称之代码组。
# 像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。
# 我们将首行及后面的代码组称为一个子句(clause)。
# 如下实例
suite = print("退出")
if False:
    suite
elif False:
    suite
else:
    suite

# 13、print 输出
# print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：
x = "a"
y = "b"
# 换行输出
print(x)
print(y)

print('---------')
# 不换行输出
print(x, end=" ")
print(y, end=" ")
print()

# 14、import 与 from...import
# 在 python 用 import 或者 from...import 来导入相应的模块。
# 将整个模块(somemodule)导入，格式为： import somemodule
# 从某个模块中导入某个函数,格式为： from somemodule import somefunction
# 从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
# 将某个模块中的全部函数导入，格式为： from somemodule import *

# 导入 sys 模块
import sys

print('================Python import mode==========================')
print('命令行参数为:')
for i in sys.argv:
    print(i)
print('\n python 路径为', sys.path)
# 导入 sys 模块的 argv,path 成员
from sys import argv, path  # 导入特定的成员

print('================python from import===================================')
print('path:', path)  # 因为已经导入path成员，所以此处引用时不需要加sys.path

# 15、命令行参数
# 很多程序可以执行一些操作来查看一些基本信息，Python可以使用-h参数查看各参数帮助信息：
# $ python -h
# usage: python [option] ... [-c cmd | -m mod | file | -] [arg] ...
# Options and arguments (and corresponding environment variables):
# -c cmd : program passed in as string (terminates option list)
# -d     : debug output from parser (also PYTHONDEBUG=x)
# -E     : ignore environment variables (such as PYTHONPATH)
# -h     : print this help message and exit
#
# [ etc. ]

# 16、笔记
# !/usr/bin/python3
# 第一行注释标的是指向 python 的路径，告诉操作系统执行这个脚本的时候，调用 /usr/bin 下的 python 解释器。
# 此外还有以下形式（推荐写法）：
# !/usr/bin/env python3
# 这种用法先在 env（环境变量）设置里查找 python 的安装路径，再调用对应路径下的解释器程序完成操作。

# help() 函数
# 调用 python 的 help() 函数可以打印输出一个函数的文档字符串：
# 如下实例，查看 max 内置函数的参数列表和规范的文档
help(max)

# 在 print 打印的时候双引号与单引号都可以当做定界符使用，且可以嵌套。被嵌套的会被解释成为标点符号，反之一样。
print("Hello'World!")
help("print")

# 关于 import 的小结，以 time 模块为例：
# 1、将整个模块导入，例如：import time，在引用时格式为：time.sleep(1)。
# 2、将整个模块中全部函数导入，例如：from time import *，在引用时格式为：sleep(1)。
# 3、将模块中特定函数导入，例如：from time import sleep，在引用时格式为：sleep(1)。
# 4、将模块换个别名，例如：import time as abc，在引用时格式为：abc.sleep(1)。

# 在 Python 中，from somemodule import * 和 import somemodule 有一些重要的区别，主要体现在命名空间和可访问性上。
# import somemodule - 导入整个模块。
# 使用模块中的内容时，需要使用模块名作为前缀。例如，如果 somemodule 中有一个函数 foo，你需要这样调用它：somemodule.foo()。
# 优点是命名空间保持清晰，避免了与当前模块中的变量和函数名冲突。
import math

print(math.sqrt(16))  # 输出: 4.0

# from somemodule import * - 导入模块中的所有公开对象（函数、变量、类等）到当前命名空间。
# 使用模块中的内容时，不需要使用模块名作为前缀。例如，如果 somemodule 中有一个函数 foo，你可以直接调用它：foo()。
# 缺点是可能会引入命名冲突，因为当前命名空间中的变量和函数名可能与导入的模块中的某些名字冲突。
from math import *

print(sqrt(16))  # 输出: 4.0
# 总结来说，import somemodule 保持了命名空间的清晰性和安全性，减少了命名冲突的风险，而 from somemodule import * 虽然简洁，
# 但可能导致命名冲突和代码的可读性降低。通常建议使用 import somemodule 或者 from somemodule import specific_function 这种更明确的导入方式。

# 类似于 C/C++ 的 printf，Python 的 print 也能实现格式化输出，方法是使用 % 操作符，它会将左边的字符串当做格式字符串，将右边的参数代入格式字符串：
print("100 + 200 = %d" % 300)  # 左边的%d被替换成右边的300
print("A的小写是%s" % "a")  # 左边的%s被替换成右边的a
# 如果要带入多个参数，则需要用 () 包裹代入的多个参数，参数与参数之间用逗号隔开，参数的顺序应该对应格式字符串中的顺序
print("%d + %d = %d" % (100, 200, 300))
print("%s %s" % ("world", "hello"))
# 格式字符串中，不同占位符的含义：
# %s： 作为字符串
# %d： 作为有符号十进制整数
# %u： 作为无符号十进制整数
# %o： 作为无符号八进制整数
# %x： 作为无符号十六进制整数，a～f采用小写形式
# %X： 作为无符号十六进制整数，A～F采用大写形式
# %f： 作为浮点数
# %e，%E： 作为浮点数，使用科学计数法
# %g，%G： 作为浮点数，使用最低有效数位
