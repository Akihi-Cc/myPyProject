# !/usr/local/bin/python3.12
# Python 关键字是指在 Python 解释器中已经有特定含义和用途的词语。Python 语言规定有 35 （python 3.12.2）个关键字，这些关键字应该全部采用小写字母表示，不允许用作变量名、函数名、类名等。
import keyword
import asyncio
# Python 3.7+
import datetime
print("*******************************************【1】keyword.kwlist *******************************************")
# 查看python解释器中的所有关键字：

# 打印所有关键字
print(len(keyword.kwlist), ':', keyword.kwlist)

# 1. 控制流程关键字
# 名称	                    描述
# if/elif/else	            条件判断
# for/while/else	        循环判断
# break/continue	        跳出循环、跳出本次循环
# try/except/else/finally	异常处理
# assert	                条件测试的语句

print("*******************************************【2】 if / elif / else *******************************************")
# if / elif / else
# 如果给定的条件为True，则执行相应的代码块。如果条件为False，则可以选择执行一个else代码块（如果提供了的话）。

x, y = 10, 5
if x > 5:
    print('x > 5')

if x > y:
    print('x > y')
else:
    print('x < y')

if x > 5:
    print('x > 5')
elif x > y:
    print('x > y')
else:
    print('x < 5 and x < y')

print("*******************************************【3】 for / while / else *******************************************")
# for / while / else
# 只要条件满足，循环就会一直执行，直到条件变为False为止。如果条件一开始就不满足，那么循环体一次都不会执行。（else块通常不是必需的）

# for循环用于遍历可迭代对象（如列表、元组、字典、字符串等）中的元素。
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

# for循环遍历numbers列表。如果找到了数字3，则通过break语句提前终止循环。由于3确实在列表中，所以循环会在找到3之后终止，并且不会执行else子句中的代码。
i = 0
for number in range(1, 6):
    if number == 3:
        i += 1
        print("找到了3 退出循环 循环了%d次" % i)
        break  # 当number等于3时，使用break语句退出循环
    i += 1
    print(number)
else:
    print("循环完成而未找到 3")

# while只要条件满足，循环就会一直执行，直到条件变为False为止。如果条件一开始就不满足，那么循环体一次都不会执行。
count = 0
while True:  # 无限循环
    print(count)
    count += 1
    if count >= 5:
        break  # 当count达到5时，使用break语句退出循环
else:
    print("这将不会被打印")

print("*******************************************【4】 break / continue *******************************************")
# break / continue（必须用在循环内部）
# continue语句用于在循环中跳过当前迭代的剩余部分，并开始下一个迭代。当continue语句被执行时，循环会立即跳过当前迭代中continue之后的所有代码，并检查循环条件以决定是否继续执行下一个迭代。

for number in range(1, 11):
    if number % 2 == 0:  # 如果数字是偶数
        continue  # 跳过当前迭代
    print(number)  # 只打印奇数

# break语句用于提前终止循环（无论是for循环还是while循环）。当break语句被执行时，循环将立即停止，并且程序流程将继续在循环结构之后的第一条语句。
count = 0
while count < 10:
    count += 1
    if count == 5:  # 当count等于5时
        print('count等于5时，跳出循环。')
        break  # 跳出循环
    print(count)

print("*******************************************【5】 try/ except / else / finally *******************************************")
# try/ except / finally / else结构用于异常处理。这种结构允许你指定在程序执行过程中可能出现的错误（异常），并定义当这些错误发生时应该如何响应。

# 这里是这些关键字的基本用法和说明：

# try块中的代码是程序尝试执行的代码。如果这段代码运行期间没有发生异常，那么try块之后的else块（如果有的话）将被执行。如果try块中的代码引发了异常，那么except块将被执行。
# except块用于捕获try块中引发的异常。你可以指定要捕获的异常类型，以及当该异常被触发时要执行的代码。你可以有多个except块来捕获不同类型的异常。
# else块是可选的，它会在try块成功执行（即没有引发异常）之后执行。如果try块中引发了异常，则else块将不会被执行。
# finally块中的代码无论是否发生异常都会被执行。这通常用于清理资源，如关闭文件或网络连接。
try:
    # 尝试执行可能会引发异常的代码
    result = 10 / 0
except ZeroDivisionError:
    # 捕获ZeroDivisionError异常
    print("不能除以零!")
except TypeError as e:
    # 捕获其他类型的异常，并打印异常信息
    print(f"发生了类型错误: {e}")
else:
    # 如果没有异常发生，执行这里的代码
    print("计算成功，结果是:", result)
finally:
    # 无论是否发生异常，最后都会执行这里的代码
    print("清理资源或执行最后的操作。")

# else块通常不是必需的，并且它通常用于在try块成功完成后执行一些额外的操作，而不是用于异常处理。finally块则更常用于资源清理，确保无论程序是否成功，都会执行一些操作。

print("*******************************************【6】 assert *******************************************")
# assert
# assert 是一个用于进行条件测试的语句。如果条件为True，则assert 语句不会有任何效果，程序将继续执行。但是，如果条件为 False，则assert 语句会触发一个AssertionError异常。

condition = True
assert condition, "error message"


# 其中，condition是要测试的条件，而"error message"是在条件为False时引发的异常的消息。这个消息是可选的，但提供它可以使得在调试时更容易理解为什么断言失败了。

# 在函数中使用断言来验证输入
def divide(numerator, denominator):
    assert denominator != 0, "Denominator cannot be zero"
    return numerator / denominator


print(divide(10, 1))

# 使用断言来验证程序状态
x = [1, 2, 3]
assert len(x) > 0, "List should not be empty"


# assert 语句主要用于调试和开发过程中，而不是用于生产环境的错误处理。在生产环境中，你可能希望使用更复杂的错误处理和日志记录机制来处理错误情况。此外，通过优化
# Python 解释器的命令行选项（如 - O 或 - OO），可以禁用所有的 assert 语句，这使得它们不适合用于生产环境的必要检查。

# 2.定义变量或常量关键字
# 名称            描述
# def	        定义函数     循环使用，保存了名字，通过名字就可以重复引用函数功能
# class	        定义类
# lambda	    定义匿名函数（或lambda 表达式）  一次性使用，随时随时定义
# import	    导入模块
# from…import…	获取模块中指定
# yield	        定义一个生成器     yield就是 return 返回一个值，并且记住这个返回的位置，下次迭代就从这个位置后(下一行)开始。

print("*******************************************【7】 def *******************************************")
# def用于定义函数。函数是一段可重复使用的代码块，它执行特定的任务，并可能接收输入（称为参数）和返回输出（称为返回值）。
# 比如函数中有一个yield赋值，a = yield 5，第一次迭代到这里会返回5，a还没有赋值。第二次迭代时，使用.send(10)，那么，就是强行修改yield 5表达式的值为10，本来是5的，那么a=10

def greet(name):
    """这是一个简单的问候函数，接收一个名字作为参数，并打印出问候信息。"""
    print(f'你好，{name}!')
    return "hahaha"


# 调用函数，传递参数"Alice"
print(greet("Alice"))


# 在这个例子中，def后面紧跟着函数名greet，然后是一组括号，里面可以放置函数的参数（在这个例子中是name）。接下来是一个冒号:，表示函数体的开始。函数体是缩进的代码块，它包含了函数执行时要运行的代码。
# 函数的文档字符串（docstring）是一个可选的多行字符串，紧跟在函数定义之后，用于解释函数的目的和行为。它不是必需的，但通常用于提供关于函数如何工作和使用方法的说明。
# 要调用（执行）这个函数，你只需在函数名后面加上括号，并传入所需的参数（如果有的话）。在这个例子中，我们调用了greet函数，并传递了字符串"Alice"作为参数。
# 函数可以有任意数量的参数，也可以没有参数。此外，函数可以返回一个值（使用return关键字），也可以不返回任何值（在这种情况下，函数的返回值是None）。

print("*******************************************【8】 class *******************************************")
# class类是创建对象的模板或蓝图，它描述了具有相同属性和方法的对象的集合。通过类，你可以创建类的实例（即对象），每个实例都有自己的状态（即属性）和行为（即方法）。

# 定义一个名为Person的类
class Person:
    # 这是一个特殊的方法，称为构造方法或初始化方法
    # 当创建类的新实例时，它会自动被调用
    def __init__(self, name, age):
        # self是对实例自身的引用，它总是类方法的第一个参数
        self.name = name  # 为实例设置一个属性name
        self.age = age  # 为实例设置一个属性age

    # 这是一个实例方法，它可以通过类的实例来调用
    def greet(self):
        print(f"你好，我叫{self.name}，我{self.age}岁了。")


# 创建Person类的一个实例
person1 = Person("Alice", 30)
# 调用实例的方法
person1.greet()  # 输出：你好，我叫Alice，我30岁了。

# 访问实例的属性
print(person1.name)  # 输出：Alice
print(person1.age)  # 输出：30
# 在这个例子中，Person类有两个属性（name和age）和一个方法（greet）。__init__方法是一个特殊的方法，它在创建类的新实例时被调用，用于初始化实例的属性。greet方法是一个实例方法，它可以通过类的实例来调用，
# 并且可以访问该实例的属性。
# 类还可以包含其他类型的方法，如类方法（使用 @ classmethod装饰器）、静态方法（使用 @ staticmethod装饰器）和属性（使用 @ property装饰器）。类还可以继承其他类，从而创建更复杂的类和对象层次结构。
# 此外，Python还支持一些高级特性，如抽象基类、混入（mixins）、多重继承等，这些都可以用来创建更加灵活和强大的类结构。

print("*******************************************【9】 lambda *******************************************")
# lambda是一个关键字，用于定义匿名函数（也叫作lambda函数或lambda表达式）。匿名函数是一种小型、简洁的函数，通常用于需要一个函数作为参数传递给另一个函数，或者用于简单的、一次性的函数操作。
# Lambda函数可以接受任意数量的参数，但只能有一个表达式，并且这个表达式的结果就是该函数的返回值。Lambda函数没有函数名，也不能使用return关键字。

# 定义一个lambda函数，它接受两个参数x和y，并返回它们的和
add = lambda x, y: x + y
# 使用这个lambda函数
result = add(3, 4)
print(result)  # 输出：7
# 在这个例子中，lambda x, y: x + y定义了一个匿名函数，该函数接受两个参数x和y，并返回它们的和。然后，这个匿名函数被赋值给了变量add，之后可以像调用普通函数一样使用它。

print("*******************************************【10】 import *******************************************")
# import用于导入一个模块或库，以便你可以在当前的程序中使用它提供的函数、类、变量等。模块是一个包含Python代码的文件，通常包含定义函数、类和变量的代码，以及可以被其他模块使用的代码。
# 当你使用import关键字导入一个模块时，Python会查找该模块并在内存中加载它。然后，你就可以通过模块名来访问该模块中定义的函数、类和变量。

import math

# 使用模块中的函数
print(math.sqrt(16))  # 输出：4.0

# 导入模块有助于组织代码，使其更加模块化和可重用。通过导入模块，你可以将代码分解为多个独立的文件，每个文件包含一组相关的函数和类，这样可以提高代码的可读性和可维护性。

print("*******************************************【11】 from ... import... *******************************************")
# from ... import...语句用于从一个模块中导入特定的部分（函数、类、变量等），而不是导入整个模块。

from math import sqrt, pi

# 直接使用 sqrt 和 pi 函数，不需要 math. 作为前缀
print(sqrt(16))  # 输出：4.0
print(pi)  # 输出：3.141592653589793
# 使用from ... import...语句可以使代码更加简洁，因为你不需要每次都写出完整的模块名。然而，这也可能导致命名空间的冲突，特别是当你从不同的模块导入同名的函数或变量时。在这种情况下，建议使用别名导入来避免冲突。

print("*******************************************【12】 yield *******************************************")
# yield关键字用于定义一个生成器（generator）。生成器是一种特殊的迭代器，它允许你逐个地产生（或“yield”）一系列的值，而不是一次性地生成所有值。这样做的好处是可以节省内存，因为生成器只在需要时才产生下一个值，
# 而不是一次性地在内存中存储所有值。
# yield语句只能在定义生成器函数时使用，这样的函数看起来就像一个普通的函数，但是包含了yield语句。当你调用这样的函数时，它不会执行，而是返回一个迭代器。然后，每次你从迭代器请求一个值时（例如，通过next()
# 函数或在for循环中），生成器函数会执行到下一个yield语句，并返回该语句的值。然后函数的状态被保存，直到下一次请求值。

def generator():
    yield 1, 2
    yield 3, 4


# 创建生成器对象
f = generator()
# 使用next()函数获取生成器产生的值
print(next(f))  # (1, 2)
print(next(f))  # (3, 4)
# 此时的f已经迭代到StopIteration，如果再次执行next(f)就会抛出StopIteration异常。
# 如果再次尝试获取值，生成器已经耗尽，将抛出StopIteration异常
# print(next(f))  # 将抛出 StopIteration

#  for循环可以处理StopIteration异常
for x in generator():
    print(x)

# 生成器在处理大数据集或无限序列时特别有用，因为它们允许你逐个处理元素，而不是一次性加载整个数据集到内存中。

# 3.常量关键字
# 名称                 描述
# True / False        布尔类型，逻辑值
# None                空对象

print("*******************************************【13】 True和False *******************************************")
# True和False是布尔（Boolean）类型的两个值，用于表示逻辑条件的结果。布尔类型只有两个值：True和False，它们通常用于条件语句（如 if 语句）和循环语句（如while 循环）中，以决定程序的执行流程。
# 使用逻辑运算符组合条件
a = True
b = False
if a and b:  # a和b都是True时，结果为True
    print("Both a and b are True")
else:
    print("At least one of a or b is False")  # 这个语句会执行，因为a或b至少有一个是False

# 使用not运算符取反
if not a:  # not True 结果是 False
    print("a is False")
else:
    print("a is True")  # 这个语句会执行，因为a是True

# 在Python中，可以使用整数1和0来表示布尔值，其中1相当于True，而0相当于False。然而，这种做法并不推荐，因为它可能会导致混淆和误解。最佳实践是始终使用True和False来表示布尔值。
# Python还允许在条件语句中使用其它类型的值（如字符串、列表、字典等），这些值在条件判断时会被自动转换为布尔值。例如，空字符串""、空列表[]、空字典{}、数值0以及None都会被解释为False，而其他任何值都会被解释为True。

print("*******************************************【14】 None *******************************************")
# None用于表示一个空值或没有值。经常用于初始化变量，以表示该变量尚未被赋予一个有意义的值。None在Python中是一个非常重要的概念，用于区分空值和False，因为False在布尔上下文中是一个有效的值。

# 声明一个变量但没有给它赋值时，它的默认值是None。
x = None

# None和False在布尔上下文中是不同的。None本身在布尔上下文中被评估为False，但它们是两个不同的对象。这意味着可以用 is 或 is not 来区分它们：

if x is None:
    print("x is None")
if x is False:
    print("x is False")

# None在Python中是一个非常重要的概念，用于表示缺失值或空值，并且在处理可能为空的值时，应始终检查其是否为None，以避免产生意料之外的结果。

# 4.特殊用途关键字
# 名称                描述
# as                 指定别名
# global             声明全局变量
# nonlocal           声明外层变量

print("*******************************************【15】 as *******************************************")
# as关键字通常用于两个主要场景：import语句和with语句。

# a.import语句  在import语句中，as关键字用于为导入的模块或对象指定一个别名。在模块名称太长、模块名称与其它模块冲突、或者想要使用更简洁或更具描述性的名称时非常有用。
import math as m  # 将math模块重命名为m

# 现在可以使用m来访问math模块的函数和常量
print(m.sqrt(16))  # 输出 4.0

# b.with语句在with语句中，as关键字用于将上下文管理器返回的对象绑定到一个变量上，以便在with块内部使用。这通常用于文件操作、线程锁、事务处理等场景。
with open('/Users/liuchao/Desktop/123.py', 'r') as file:  # 打开文件，并将文件对象绑定到变量file上
    content = file.read()  # 使用file变量来读取文件内容
print(content)
# 当with块执行完毕后，文件会自动关闭，无需手动调用file.close()

# as关键字允许我们以更清晰、更简洁的方式编写代码，并避免名称冲突。
print("*******************************************【16】 global *******************************************")
# global关键字用于声明一个变量是全局的，这个变量是在函数外部定义的，并且可以在函数内部被访问和修改。通常，在函数内部定义的变量是局部变量，它们只在该函数内部有效，并且在函数外部是不可见的。
# 但是，通过使用global关键字，你可以在函数内部引用和修改全局变量。

# 定义一个全局变量
x = 10


def increment_x():
    # 声明我们要使用全局变量x
    global x
    # 修改全局变量x的值
    x += 1
    print(f"Inside function: x = {x}")


# 调用函数
increment_x()

# 打印全局变量x的值，检查它是否已被函数修改
print(f"Outside function: x = {x}")


# 在这个例子中，x是一个全局变量。increment_x函数使用global关键字来声明它要访问和修改的是全局变量x，而不是创建一个新的局部变量。因此，当函数执行后，全局变量x的值从10增加到了11，
# 并且在函数外部打印x的值时也显示了修改后的值。
# 过度使用全局变量可能会导致代码难以维护和理解，因为它们可以在程序的任何位置被修改。因此，通常建议尽可能使用局部变量，并通过函数的参数和返回值来传递数据。在确实需要访问和修改全局变量的情况下，再谨慎地使用global关键字。

print("*******************************************【17】 nonlocal *******************************************")
# nonlocal关键字用于指示一个变量引用的是嵌套作用域中的变量，而不是全局作用域中的变量。它通常用于嵌套函数（即在另一个函数内部定义的函数）中，以允许内部函数修改外部函数的变量。
# nonlocal关键字是在Python3中引入的，用于解决在嵌套函数中修改外部变量时的一个限制。在Python2中，要在嵌套函数中修改外部变量，通常需要使用可变对象（如列表或字典）作为“包装器”来间接修改其值。

def outer_function():
    x = 10

    def inner_function():
        # 声明我们要引用的是外部函数的变量x
        nonlocal x
        # 修改外部函数的变量x的值
        x += 1
        print(f"Inside inner_function: x = {x}")

    inner_function()
    print(f"Inside outer_function: x = {x}")


outer_function()
print(f"Outside all functions: x is not defined")

# 在这个例子中，outer_function定义了一个局部变量x，并定义了一个嵌套函数inner_function。在inner_function中，使用nonlocal关键字来声明我们要修改的是outer_function中的x变量，而不是创建一个新的局部变量。
# 因此，当inner_function执行时，它增加了x的值，并且这个修改在outer_function的作用域中也是可见的。
# 需要注意的是，nonlocal只能用于嵌套函数内部，并且它引用的变量必须是在当前嵌套作用域中定义的。如果尝试引用一个不存在于当前嵌套作用域中的变量，Python会抛出一个异常。此外，nonlocal不能用于全局作用域中，
# 因为全局变量应该使用global关键字来访问和修改。

# 5.逻辑运算符关键字
# 名称                描述
# not                布尔值进行取反                        对应java !
# and                测试两个或更多条件是否都为真            对应java &&
# or                 测试两个或更多条件是否至少有一个为真     对应java ||

print("*******************************************【18】 not *******************************************")
# not 是一个逻辑运算符，用于对布尔值进行取反。如果布尔值为True，not 将其转换为False；如果布尔值为False，not 将其转换为True。

# 使用 not 运算符在条件表达式中
result = not False  # result 将被赋值为 True
print(result)

# not 运算符在条件判断和逻辑运算中非常有用，特别是当你想检查某个条件是否不满足时。

print("*******************************************【19】 and *******************************************")
# and是一个逻辑运算符，用于测试两个或更多条件是否都为真（True）。如果所有条件都为真，则整个表达式的结果为True；否则，结果为False。

# 检查两个条件是否都为真
a = 5
b = 10
# Both a and b are positive.
if a > 0 and b > 0:
    print("Both a and b are positive.")
else:
    print("At least one of a or b is not positive.")

# 使用and运算符来组合多个条件
# a is positive, b is positive, and a is less than b.
if a > 0 and b > 0 and a < b:
    print("a is positive, b is positive, and a is less than b.")
else:
    print("One or more conditions are not met.")

# 短路行为：如果第一个条件为False，则整个表达式为False，不会评估后面的条件
x = False
y = True
# At least one of x or y is False.
if x and y:  # This will not evaluate 'y' because 'x' is False
    print("Both x and y are True.")
else:
    print("At least one of x or y is False.")

# and运算符在编程中非常有用，特别是当你需要确保多个条件同时满足时。它也可以用于连接多个布尔表达式，以创建更复杂的条件判断。

print("*******************************************【20】 or *******************************************")
# or 是一个逻辑运算符，用于测试两个或更多条件中是否至少有一个为真（True）。只要有一个条件为真，整个表达式的结果就是True；如果所有条件都为假，结果才是False。

# 使用 or 运算符来测试至少一个条件是否为真
a = 5
b = 10
# Both a and b are non-negative.
if a < 0 or b < 0:
    print("At least one of a or b is negative.")
else:
    print("Both a and b are non-negative.")

# 使用 or 运算符结合多个条件
# At least one of the conditions is true.
if a > 0 or b > 0 or a == b:
    print("At least one of the conditions is true.")
else:
    print("None of the conditions is true.")

# or 运算符的短路行为：如果第一个条件为真，则不会评估后面的条件
x = True
y = False
# x is True or y is True.
if x or y:
    print("x is True or y is True.")
else:
    print("Both x and y are False.")

# or 运算符用于变量，这些变量预期包含布尔值
flag1 = True
flag2 = False
# At least one of the flags is True.
if flag1 or flag2:
    print("At least one of the flags is True.")
else:
    print("Both flags are False.")

# or 运算符在编写条件语句时非常有用，特别是当你需要确保至少有一个条件满足时。它可以用于组合多个条件，以创建更复杂的逻辑判断。
# 逻辑运算符not、 and 和 or 的优先级从高到低分别是not > and > or 。这意味着在没有使用括号的情况下，not 会首先被评估，然后是 and，最后是 or。
# 当编写包含多个逻辑运算符的表达式时，使用括号来明确指定优先级是一个好习惯，这样可以提高代码的可读性并减少潜在的错误。

# 6.检查关键字
# 名称            描述
# in             判断一个成员是否属于一个序列
# is             检查两个变量是否引用内存中的同一个对象

print("*******************************************【21】 in *******************************************")
# in用于检查某个元素是否存在于一个序列（如列表、元组、字符串等）或集合中。如果元素存在于该序列或集合中，in表达式将返回True，否则返回False。

my_string = "Hello, World!"
if "World" in my_string:
    print("字符串中包含'World'")
else:
    print("字符串中不包含'World'")

my_dict = {'apple': 1, 'banana': 2, 'cherry': 3}
if 'banana' in my_dict:
    print("'banana'是字典的一个键")
else:
    print("'banana'不是字典的一个键")

# not in 是一个常用的组合运算符，用于检查某个元素是否不包含在特定的集合、列表、元组、字符串或其他可迭代对象中。如果元素不在指定的集合中，not in 将返回True，否则返回False。

# 检查一个值是否不在集合中
numbers = {1, 2, 3, 4, 5}
if 6 not in numbers:
    print("The number 6 is not in the set.")

print("*******************************************【22】 is *******************************************")
# is 是一个身份运算符，用于比较两个对象的身份是否相同，也就是说，它检查两个变量是否引用内存中的同一个对象。如果两个变量引用的是同一个对象， is 运算符返回True，否则返回False。

# 比较两个变量是否引用同一个对象
a = [1, 2, 3]
b = a  # b 是 a 的另一个引用
c = [1, 2, 3]  # c 是一个新的列表，虽然内容与a相同，但不是同一个对象

print(a is b)  # 输出: True，因为b是a的引用
print(a is c)  # 输出: False，因为c是一个新的对象

# 与None的比较
x = None
print(x is None)  # 输出: True

# 与小整数对象的比较
# 在Python中，-5 到 256 之间的小整数是预先创建的单例对象
# 因此，对于这些小整数，使用 is 比较会得到 True
i1 = 100
i2 = 100
print(i1 is i2)  # 输出: True

# 对于超出这个范围的整数，is 比较会返回 False
i3 = 257
i4 = 257
print(i3 is i4)  # 输出: False

# 对于字符串，如果它们是通过相同的字面量创建的，那么它们可能是同一个对象
s1 = "hello"
s2 = "hello"
print(s1 is s2)  # 在CPython中，输出可能是: True，但这依赖于字符串的驻留机制

# 但如果你通过不同的方式创建字符串，那么它们就不是同一个对象
s3 = str("hello")
print(s1 is s3)  # 输出: False

# is与 == 运算符不同， == 运算符用于比较两个对象的值是否相等，而不是它们的身份。
# 需要注意的是， is 运算符的行为可能会因Python的实现（如CPython、Jython、IronPython等）而有所不同，特别是在处理小整数和字符串时。在CPython中，对于小的整数和通过相同字面量创建的字符串， is 可能会返回
# True，但这并不是Python语言规范的一部分，而是CPython的一个实现细节。因此，在编写可移植代码时，最好避免依赖这种行为。

# 7.异步关键字
# 名称            描述
# async          声明一个函数是异步的
# await          等待异步操作完成

print("*******************************************【23】 async *******************************************")
# async是一个关键字，用于声明一个函数是异步的。异步函数，也被称为协程（coroutine），是一种可以在执行过程中挂起（suspend）和恢复（resume）的函数。异步函数是异步编程的核心，它们允许你编写非阻塞的代码，这在处理I / O密集型任务（如网络请求或文件读写）时特别有用。
# 异步函数使用async def来定义，而不是常规的def。异步函数可以包含await表达式，用于挂起函数的执行，等待另一个异步操作完成。


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    formatted_time1 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print('started at', formatted_time1)

    await say_after(1, 'hello')
    await say_after(2, 'world')
    formatted_time12 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print('finished at',formatted_time12)

# 运行主协程
asyncio.run(main())

# 在这个例子中，say_after是一个异步函数，它使用await来等待asyncio.sleep(delay)完成。asyncio.sleep(delay)
# 是一个模拟异步等待的函数，它会“睡眠”指定的秒数。main函数也是异步的，并且它调用了两个say_after函数，每个函数都有一个不同的延迟。

# 当你运行这个程序时，它会首先打印开始时间，然后等待1秒钟后打印"hello"，再等待2秒钟后打印"world"，最后打印结束时间。尽管有两个延迟操作，但整个程序是异步的，因此它不会阻塞整个程序等待这些操作完成。
# 异步编程在Python中通常与asyncio模块一起使用，该模块提供了事件循环和许多用于异步I / O操作的工具。从Python3.7开始，可以使用asyncio.run(main())来运行主协程，这简化了异步程序的启动过程。
# 需要注意的是，不是所有的I / O操作都支持异步。然而，对于那些支持异步的I / O操作（如网络请求使用aiohttp或httpx库，文件读写使用aiofiles库等），使用异步编程可以显著提高程序的性能和响应能力。

print("*******************************************【24】 await *******************************************")
# await是一个用于在异步编程中等待异步操作完成的关键字。它只能在定义为async的异步函数（也称为协程）内部使用。当在异步函数内部遇到await时，Python会暂停该异步函数的执行，等待await后面的异步操作完成，然后继续执行异步函数。
# 异步编程通常用于I / O密集型任务，如网络请求或文件读写，以便在等待I / O操作完成时不会阻塞整个程序。通过使用async和await，你可以编写看起来像同步代码的异步代码，但实际上是非阻塞的。


async def fetch_data():
    # 模拟一个异步操作，如网络请求
    print("Fetching data...")
    await asyncio.sleep(1)  # 等待1秒，模拟异步I/O操作
    print("Data fetched!")
    return "Some data"


async def main():
    # 调用异步函数
    data = await fetch_data()
    print("Got data:", data)


# 运行主异步函数
asyncio.run(main())

# 在这个例子中，fetch_data是一个异步函数，它使用await来等待asyncio.sleep(1)完成。asyncio.sleep(1)是一个模拟异步I / O操作的函数，它会“睡眠”1秒钟。在main异步函数中，我们调用fetch_data并使用await来等待它完成。

# 当你运行这个程序时，它会首先打印"Fetching data…"，然后等待1秒钟（在这个等待期间，其他任务可以并发执行），之后打印"Data fetched!“和"Got data: Some data”。
# 异步编程是Python3.5及更高版本中引入的新特性，它使得编写高性能的并发代码变得更加容易。

print("*******************************************【25】 del *******************************************")
# 8.其它
# 名称        描述
# del        删除对象的引用
# pass       空操作语句（占位符）
# raise      显式地引发（或重新引发）一个异常
# return     从函数中返回一个值
# with       上下文管理协议

# del是一个关键字，用于删除对象的引用。当使用del语句时，告诉Python垃圾回收器该对象不再需要，因此可以安全地释放其占用的内存。

x = 10
print(x)
del x  # 删除变量x的引用
# print(x)  # 输出: NameError: name 'x' is not defined

my_list = [1, 2, 3, 4, 5]
del my_list[1]  # 删除索引为1的元素（即数字2）
print(my_list)  # 输出: [1, 3, 4, 5]
del my_list[1:3]  # 删除索引1到2之间的元素（即数字3）
print(my_list)  # 输出: [1, 5]

del my_list  # 删除整个列表对象
# del my_module  # 如果my_module是一个模块名，则删除该模块
# del my_class  # 如果my_class是一个类名，则删除该类


# del可以用于删除变量的引用，从列表中删除元素，以及从字典中删除键值对。
# 需要注意的是，del关键字在删除列表或字典元素时不会引发错误，即使列表为空或字典中不存在指定的键。然而，如果尝试删除一个不存在的变量，将会引发NameError。
# del不能用于删除不可变类型（如元组或字符串）的元素，因为这些类型的元素不能被修改。
# del也用于删除整个对象，如删除模块或删除整个列表对象。
# 使用del时要小心，确保不会误删重要的变量或数据结构。在删除之前，最好先确认对象是否真的不再需要。

print("*******************************************【26】 pass *******************************************")
# pass是一个空操作语句，意味着当它被执行时，什么都不会发生。pass语句通常用作占位符，在语法上需要语句但程序不需要任何操作时使用。
def my_function():
    # 这个函数目前什么都不做
    pass


class MyClass:
    # 这个类目前什么都不做
    pass


if __name__ == "__main__":
    # 主程序入口，但目前还没有实现
    pass

# 在这个例子中，my_function函数、MyClass类以及if__name__ == "__main__": 块都包含了pass语句，这意味着它们目前不执行任何操作。
# 使用pass语句可以帮助你编写一个结构完整的代码框架，即使某些部分还没有完全实现。这对于在开发过程中逐步构建和测试代码非常有用。一旦你准备好了实现具体的功能，你可以简单地替换pass语句为实际的代码。

print("*******************************************【27】 raise *******************************************")
# raise语句用于显式地引发（或重新引发）一个异常。当raise语句被执行时，程序的正常流程会被中断，并跳转到最近的异常处理代码，通常是try块后面的except块。 相当于java 中 throw new Exception()。
# 引发一个新的异常：你可以使用raise关键字后跟一个异常类来引发一个新的异常。如果异常类需要一个字符串参数来描述异常，你可以将其作为raise语句的参数提供。
# raise ValueError("This is a value error")

# 重新引发当前的异常：在except块中，你可以使用raise语句不带任何参数来重新引发当前异常。这通常用于在捕获异常后执行一些清理操作，然后再将异常传递给上层调用者。

try:
    # 尝试执行一些可能会引发异常的代码
    pass
except ValueError as e:
    # 执行一些处理，但不立即重新引发异常
    pass

# 在后面的代码中重新引发异常
# raise ValueError("An error occurred") from e

# 在这个例子中，ValueError("An error occurred")是一个新的异常，但通过使用from e，原始异常e会被附加到新异常上，从而保留了异常的原始上下文。这有助于调试，因为它允许你查看引发异常的原始位置以及异常被重新引发的位置。
# raise语句是Python异常处理机制中不可或缺的一部分，它允许你明确地控制何时中断程序的正常流程，并传递有关错误情况的信息。

print("*******************************************【28】 return *******************************************")
# return语句用于从函数中返回一个值。当return语句被执行时，它会立即结束函数的执行，并将控制权返回给调用该函数的代码。如果return语句后面跟着一个值（或一组值），那么这个值（或这些值）将作为函数的返回值。
def get_details():
    name = "Alice"
    age = 30
    return name, age  # 返回两个值：name和age


# 调用函数并解包返回值
name, age = get_details()
print(name)  # 输出: Alice
print(age)  # 输出: 30


# 在函数的任何位置使用return语句来提前结束函数的执行。常常用于条件判断或错误处理。
def check_positive_number(number):
    if number < 0:
        return False  # 如果数字小于0，提前返回False
    else:
        return True  # 否则返回True


# 调用函数并打印返回值
print(check_positive_number(5))  # 输出: True
print(check_positive_number(-3))  # 输出: False

# 如果一个函数不包含return语句，或者return语句后面没有跟任何值，那么该函数将返回None。
# 在函数中使用return语句是一种很好的做法，因为它可以使代码更加清晰，并且允许函数在完成所需操作后立即返回结果，而不是继续执行后续的代码。这对于提高代码效率和可读性非常有帮助。

print("*******************************************【29】 with *******************************************")
# with语句是一种上下文管理协议（Context Management Protocol）的实现方式，它用于封装资源获取的初始化以及清理工作，例如打开文件、网络连接、线程锁等。with语句可以确保资源在使用后被正确地释放，
# 即使在处理资源时发生异常也是如此。
# 使用with语句可以简化资源管理代码，并使其更加清晰和安全。它会自动调用进入和退出代码块时的特定方法，通常是通过实现对象的__enter__()和__exit__()方法来实现的。
# 最常见的with语句用法是与文件操作一起使用，它可以自动打开文件，并在代码块执行完毕后自动关闭文件，无论是否发生异常。

with open('/Users/liuchao/Desktop/123.py', 'r') as file:
    content = file.read()
    # 在这个代码块中，文件是打开的，可以进行读写操作
    print(content)


# 当代码块执行完毕后，文件会被自动关闭，无需手动调用file.close()

# 在上面的例子中，open('example.txt', 'r')返回了一个文件对象，这个对象实现了上下文管理协议。当with语句的代码块执行时，会调用文件对象的__enter__()
# 方法（隐式地），并将结果（通常是文件对象本身）赋值给as关键字后面的变量（在这个例子中是file）。然后执行with语句块中的代码。当代码块执行完毕后，无论是否发生异常，都会调用文件对象的__exit__()方法来清理资源（即关闭文件）。
# with语句还可以与其他实现了上下文管理协议的对象一起使用，例如线程锁（threading.Lock）、数据库连接等。

class MyContext:
    def __enter__(self):
        print("Entering the block")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting the block")


with MyContext() as x:
    print("Inside the block")
# 输出:
# Entering the block
# Inside the block
# Exiting the block

# 在这个例子中，MyContext类实现了__enter__()和__exit__()方法。当进入with语句块时，__enter__()方法被调用，并打印一条消息。当离开with语句块时，__exit__()方法被调用，并打印另一条消息。注意，即使__exit__()
# 方法接收异常参数，它并不负责处理异常；它仅仅是作为资源清理的一部分被调用。异常处理仍然由with语句块外部的异常处理机制负责。

# 9.python关键字的注意事项
# Python关键字是Python语言中预定义的、具有特殊含义的单词。这些关键字在编程时具有特定的功能，不能用作变量名、函数名或其他标识符。以下是关于Python关键字的一些注意事项：

# 避免使用关键字作为标识符：Python关键字具有特定的语法含义，不能用作变量名、函数名、类名或其他标识符。如果尝试使用关键字作为标识符，Python解释器会抛出语法错误。
# 了解关键字的作用：熟悉每个关键字的作用和用法，以便在编程时能够正确地使用它们。例如，def关键字用于定义函数，if关键字用于条件判断，for和while关键字用于循环等。
# 注意大小写：Python是大小写敏感的，因此关键字的大小写必须正确。例如，and是一个有效的关键字，但And、AND或aNd都不是。
# 不要随意更改关键字：尽管可以通过特殊手段（如修改Python解释器的源代码）来更改关键字，但这通常是不建议的。关键字的存在是为了保持Python语言的一致性和可读性，随意更改可能会导致混淆和不可预见的问题。
# 使用IDE或代码编辑器：使用集成开发环境（IDE）或代码编辑器可以帮助避免使用关键字作为标识符。这些工具通常会高亮显示关键字，并在尝试使用关键字作为标识符时发出警告或错误。
# 了解保留字：除了关键字之外，Python还有一些保留字，它们在当前版本中并未作为关键字使用，但可能会在将来的版本中添加为关键字。为了避免潜在的兼容性问题，最好不要使用这些保留字作为标识符。
# 查阅官方文档：Python官方文档提供了关于关键字的完整列表和描述。在编程时，如果需要确认某个单词是否是关键字或保留字，可以查阅官方文档以获取准确的信息。
# 总之，了解并遵守Python关键字的规则和注意事项是编写高质量、可维护的Python代码的重要一步。
