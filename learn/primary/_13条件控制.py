# !/usr/local/bin/python3.12
# Python3 条件控制
# Python 条件语句是通过一条或多条语句的执行结果（True 或者 False）来决定执行的代码块。
print("*******************************************【1】 if 语句 *******************************************")
# Python 中用 elif 代替了 else if，所以if语句的关键字为：if – elif – else。

# 1、每个条件后面要使用冒号 :，表示接下来是满足条件后要执行的语句块。
# 2、使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。
# 3、在 Python 中没有 switch...case 语句，但在 Python3.10 版本添加了 match...case，功能也类似
# 以下是一个简单的 if 实例：
var1 = 100
if var1:
    print("1 - if 表达式条件为 true")
    print(var1)

var2 = 0
if var2:
    print("2 - if 表达式条件为 true")
    print(var2)
print("Good bye!")
# 从结果可以看到由于变量 var2 为 0，所以对应的 if 内的语句没有执行。

# 以下实例演示了狗的年龄计算判断：
age = int(input("请输入你家狗狗的年龄: "))
print("")
if age <= 0:
    print("你是在逗我吧!")
elif age == 1:
    print("相当于 14 岁的人。")
elif age == 2:
    print("相当于 22 岁的人。")
elif age > 2:
    human = 22 + (age - 2) * 5
    print("对应人类年龄: ", human)

### 退出提示
input("点击 enter 键退出")

# 以下为if中常用的操作运算符:
# 操作符	        描述
# <	            小于
# <=	        小于或等于
# >	            大于
# >=	        大于或等于
# ==	        等于，比较两个值是否相等
# !=	        不等于

# 程序演示了 == 操作符
# 使用数字
print(5 == 6)
# 使用变量
x = 5
y = 8
print(x == y)

# 该实例演示了数字猜谜游戏
number = 7
guess = -1
print("数字猜谜游戏!")
while guess != number:
    guess = int(input("请输入你猜的数字："))

    if guess == number:
        print("恭喜，你猜对了！")
    elif guess < number:
        print("猜的数字小了...")
    elif guess > number:
        print("猜的数字大了...")

print("*******************************************【2】 if 嵌套 *******************************************")
# 在嵌套 if 语句中，可以把 if...elif...else 结构放在另外一个 if...elif...else 结构中。

num = int(input("输入一个数字："))
if num % 2 == 0:
    if num % 3 == 0:
        print("你输入的数字可以整除 2 和 3")
    else:
        print("你输入的数字可以整除 2，但不能整除 3")
else:
    if num % 3 == 0:
        print("你输入的数字可以整除 3，但不能整除 2")
    else:
        print("你输入的数字不能整除 2 和 3")

print("*******************************************【3】 match...case *******************************************")


# Python 3.10 增加了 match...case 的条件判断，不需要再使用一连串的 if-else 来判断了。
# match 后的对象会依次与 case 后的内容进行匹配，如果匹配成功，则执行匹配到的表达式，否则直接跳过，_ 可以匹配一切
# case _: 类似于 C 和 Java 中的 default:，当其他 case 都无法匹配时，匹配这条，保证永远会匹配成功。
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"


mystatus = 400
print(http_error(400))

# 一个 case 也可以设置多个匹配条件，条件使用 ｜ 隔开，例如：
# ...
#     case 401|403|404:
#     return "Not allowed"