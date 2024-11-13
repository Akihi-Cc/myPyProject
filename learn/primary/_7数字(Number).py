# !/usr/local/bin/python3.12
# Python3 数字(Number)
# Python 数字数据类型用于存储数值。
# 数据类型是不允许改变的，这就意味着如果改变数字数据类型的值，将重新分配内存空间。
# 以下实例在变量赋值时 Number 对象将被创建：
import cmath

var1 = 1
var2 = 10
# 您也可以使用del语句删除一些数字对象的引用。
# del语句的语法是：
# del var1[,var2[,var3[....,varN]]]
# 您可以通过使用del语句删除单个或多个对象的引用，例如：

# del var
# del var_a, var_b
# Python 支持三种不同的数值类型：
# 整型(int) - 通常被称为是整型或整数，是正或负整数，不带小数点。Python3 整型是没有限制大小的，可以当作 Long 类型使用，所以 Python3 没有 Python2 的 Long 类型。布尔(bool)是整型的子类型。
# 浮点型(float) - 浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示（2.5e2 = 2.5 x 102 = 250）
# 复数( (complex)) - 复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型。

# 2 进制是以 0b 开头的: 例如: 0b11 则表示十进制的 3
# 8 进制是以 0o 开头的: 例如: 0o11 则表示十进制的 9
# 16 进制是以 0x 开头的: 例如: 0x11 则表示十进制的 17

# 我们可以使用十六进制和八进制来代表整数：
number = 0xA0F  # 十六进制
print(number)
number = 0o70  # 八进制
print(number)

# 数值类型实例
# int	    float	    complex
# 10	    0.0	        3.14j
# 100	    15.20	    45.j
# -786	    -21.9	    9.322e-36j
# 080	    32.3e+18	.876j
# -0490	    -90.	    -.6545+0J
# -0x260	-32.54e100	3e+26J
# 0x69	    70.2E-12	4.53e-7j
# Python 还支持复数，复数由实数部分和虚数部分构成，可以用 a + bj，或者 complex(a,b) 表示， 复数的实部 a 和虚部 b 都是浮点型。
print("*******************************************【1】 Python 数字类型转换 *******************************************")
# 有时候，我们需要对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可。
# int(x) 将x转换为一个整数。
# float(x) 将x转换到一个浮点数。
# complex(x) 将x转换到一个复数，实数部分为 x，虚数部分为 0。
# complex(x, y) 将 x 和 y 转换到一个复数，实数部分为 x，虚数部分为 y。x 和 y 是数字表达式。
# 以下实例将浮点数变量 a 转换为整数：
a = 1.0
print(int(a))

print("*******************************************【2】 Python 数字运算 *******************************************")
# python 解释器可以作为一个简单的计算器，您可以在解释器里输入一个表达式，它将输出表达式的值。
# 表达式的语法很直白： +, -, * 和 /, 和其它语言（如Pascal或C）里一样。例如：
print(2 + 2)
print(50 - 5 * 6)
print((50 - 5 * 6) / 4)
print(8 / 5)  # 总是返回一个浮点数
# 注意：在不同的机器上浮点运算的结果可能会不一样。
# 在整数除法中，除法 / 总是返回一个浮点数，如果只想得到整数的结果，丢弃可能的分数部分，可以使用运算符 // ：
print(17 / 3)  # 整数除法返回浮点型
print(17 // 3)  # 整数除法返回向下取整后的结果
print(17 % 3)  # ％操作符返回除法的余数
print(5 * 3 + 2)
# 注意：// 得到的并不一定是整数类型的数，它与分母分子的数据类型有关系。
print(7 // 2)
print(7.0 // 2)
print(7 // 2.0)
# 等号 = 用于给变量赋值。赋值之后，除了下一个提示符，解释器不会显示任何结果。
width = 20
height = 5 * 9
print(width * height)
# Python 可以使用 ** 操作来进行幂运算：
print(5 ** 2)  # 5 的平方
print(2 ** 7)  # 2的7次方
# 变量在使用前必须先"定义"（即赋予变量一个值），否则会出现错误：
# >>> n   # 尝试访问一个未定义的变量
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# NameError: name 'n' is not defined

# 不同类型的数混合运算时会将整数转换为浮点数：
print(3 * 3.75 / 1.5)
print(7.0 / 2)
# 在交互模式中，最后被输出的表达式结果被赋值给变量 _ 。例如：
tax = 12.5 / 100
price = 100.50
print(price * tax)
# print(price + _)
# print(round(_, 2))
# 此处， _ 变量应被用户视为只读变量。

print("*******************************************【3】 数学函数 *******************************************")
# 函数	            返回值 ( 描述 )
# abs(x)	        返回数字的绝对值，                    如abs(-10) 返回 10
# fabs(x)	        以浮点数形式返回数字的绝对值，         如math.fabs(-10) 返回10.0
# ceil(x)	        返回数字的上入整数，                  如math.ceil(4.1) 返回 5
# floor(x)	        返回数字的下舍整数，                  如math.floor(4.9)返回 4
# round(x [,n])     返回浮点数 x 的四舍五入值，            如给出 n 值，则代表舍入到小数点后的位数。其实准确的说是保留值将保留到离上一位更近的一端。
# cmp(x, y)         如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。 Python 3 已废弃，使用 (x>y)-(x<y) 替换。
# log(x)	        如math.log(math.e)返回1.0,math.log(100,10)返回2.0
# log10(x)	        返回以10为基数的x的对数，              如math.log10(100)返回 2.0
# max(x1, x2,...)	返回给定参数的最大值，参数可以为序列。
# min(x1, x2,...)	返回给定参数的最小值，参数可以为序列。
# modf(x)	        返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
# pow(x, y)	        x**y    运算后的值。                 如math.pow(3, 2) 返回 9.0
# exp(x)	        返回e的x次幂(ex),                    如math.exp(1) 返回2.718281828459045
# sqrt(x)	        返回数字x的平方根。                   如math.sqrt(9)返回 3.0

print("*******************************************【4】 随机函数 *******************************************")
# 随机数可以用于数学，游戏，安全等领域中，还经常被嵌入到算法中，用以提高算法效率，并提高程序的安全性。
# Python包含以下常用随机数函数：
# 函数	            描述
# choice(seq)	    从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
# randrange         ([start,] stop [,step])	从指定范围内，按指定基数递增的集合中获取一个随机数，基数默认值为 1
# random()	        随机生成下一个实数，它在[0,1)范围内。
# seed([x])	        改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
# shuffle(lst)	    将序列的所有元素随机排序
# uniform(x, y)	    随机生成下一个实数，它在[x,y]范围内。

print("*******************************************【5】 三角函数 *******************************************")
# Python包括以下三角函数：
# 函数	            描述
# acos(x)	        返回x的反余弦弧度值。
# asin(x)	        返回x的反正弦弧度值。
# atan(x)	        返回x的反正切弧度值。
# atan2(y, x)	    返回给定的 X 及 Y 坐标值的反正切值。
# cos(x)	        返回x的弧度的余弦值。
# hypot(x, y)	    返回欧几里德范数 sqrt(x*x + y*y)。
# sin(x)	        返回的x弧度的正弦值。
# tan(x)	        返回x弧度的正切值。
# degrees(x)	    将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0
# radians(x)	    将角度转换为弧度

print("*******************************************【6】 数学常量 *******************************************")
# 常量	            描述
# pi	            数学常量 pi（圆周率，一般以π来表示）
# e	                数学常量 e，e即自然常数（自然常数）。

print("*******************************************【7】 笔记 *******************************************")
# “4舍6入5看齐,奇进偶不进”我觉得并不是因为浮点数在计算机表示的问题。计算机浮点数的表示是 ieee 定义的标准规则，如果 python 中存在，没道理其他语言中不存在。事实上是因为该取舍方法比过去的 "四舍五入" 方法在科学计算中更准确。而国家标准也已经规定使用 “4舍6入5看齐,奇进偶不进” 取代"四舍五入".
# 从统计学的角度上来讲,如果大量数据无脑的采用四舍五入会造成统计结果偏大。而"奇进偶舍"可以将舍入误差降到最低。
# 奇进偶舍是一种比较精确比较科学的计数保留法，是一种数字修约规则。
# 其具体要求如下（以保留两位小数为例）：
# （1）要求保留位数的后一位如果是4或者4以下的数字，则舍去， 例如 5.214保留两位小数为5.21。
# （2）如果保留位数的后一位如果是6或者6以上的数字，则进上去， 例如5.216保留两位小数为5.22。
# （3）如果保留位数是保留整数部分或保留一位小数，则要根据保留位来决定奇进偶舍：
# >>> round(5.215,2)#实际并没有进位
# 5.21
# >>> round(5.225,2)
# 5.22
# >>>
# >>> round(1.5)#此处进位
# 2
# >>> round(1.5)==round(2.5)#偶数舍去
# True
# >>> round(1.15,1)
# 1.1
# >>> round(1.25,1)
# 1.2
# >>> round(1.151,1)
# 1.2
# >>> round(1.251,1)
# 1.3
# (4) 如果保留位数的后一位如果是5，且该位数后有数字。则进上去，例如5.2152保留两位小数为5.22，5.2252保留两位小数为5.23，5.22500001保留两位小数为5.23。
# 从统计学的角度，“奇进偶舍”比“四舍五入”要科学，在大量运算时，它使舍入后的结果误差的均值趋于零，而不是像四舍五入那样逢五就入，导致结果偏向大数，使得误差产生积累进而产生系统误差，“奇进偶舍”使测量结果受到舍入误差的影响降到最低。