# !/usr/local/bin/python3.12
# Python3 循环语句
# 本章节将为大家介绍 Python 循环语句的使用。
# Python 中的循环语句有 for 和 while。

print("*******************************************【1】 while 循环 *******************************************")
# 需要注意冒号和缩进。另外，在 Python 中没有 do..while 循环。
# 以下实例使用了 while 来计算 1 到 100 的总和：
n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
print("1 到 %d 之和为: %d" % (n, sum))

# while 循环使用 else 语句
# 如果 while 后面的条件语句为 false 时，则执行 else 的语句块。
count = 0
while count < 5:
    print(count, " 小于 5")
    count = count + 1
else:
    print(count, " 大于或等于 5")

print("*******************************************【2】 简单语句组 *******************************************")
# 简单语句组
# 类似 if 语句的语法，如果你的 while 循环体中只有一条语句，你可以将该语句与 while 写在同一行中， 如下所示：
flag = 1
while (flag == 1): print('欢迎访问菜鸟教程!'); flag += 1
print("Good bye!")

print("*******************************************【3】 for 语句 *******************************************")
# Python for 循环可以遍历任何可迭代对象，如一个列表或者一个字符串。
sites = ["Baidu", "Google", "Runoob", "Taobao"]
for site in sites:
    print(site)

# 整数范围值可以配合 range() 函数使用：
#  1 到 5 的所有数字：
for number in range(1, 6):
    print(number)

print("*******************************************【3】 for...else *******************************************")
# 在 Python 中，for...else 语句用于在循环结束后执行一段代码。
for x in range(6):
    print(x)
else:
    print("Finally finished!")

sites = ["Baidu", "Google", "Runoob", "Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")

print("*******************************************【4】 range() 函数 *******************************************")
# 如果你需要遍历数字序列，可以使用内置 range() 函数。它会生成数列，例如:
for i in range(5):
    print(i)

# 你也可以使用 range() 指定区间的值：
for i in range(5, 9):
    print(i)

# 也可以使 range() 以指定数字开始并指定不同的增量(甚至可以是负数，有时这也叫做'步长'):
for i in range(0, 10, 3):
    print(i)

# 负数：
for i in range(-10, -100, -30):
    print(i)

# 您可以结合 range() 和 len() 函数以遍历一个序列的索引,如下所示:
a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i, a[i])

# 还可以使用 range() 函数来创建一个列表：
print(list(range(5)))

# break 和 continue 语句及循环中的 else 子句
print("【4】 break 和 continue 语句及循环中的 else 子句 *******************************************")
# break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。
# continue 语句被用来告诉 Python 跳过当前循环块中的剩余语句，然后继续进行下一轮循环。
# while 中使用 break：
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('1循环结束。')

# while 中使用 continue：
n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('2循环结束。')

for letter in 'Runoob':  # 第一个实例
    if letter == 'b':
        break
    print('3当前字母为 :', letter)

var = 10  # 第二个实例
while var > 0:
    print('4当前变量值为 :', var)
    var = var - 1
    if var == 5:
        break

print("Good bye!")

# 以下实例循环字符串 Runoob，碰到字母 o 跳过输出
for letter in 'Runoob':  # 第一个实例
    if letter == 'o':  # 字母为 o 时跳过输出
        continue
    print('5当前字母 :', letter)

var = 10  # 第二个实例
while var > 0:
    var = var - 1
    if var == 5:  # 变量为 5 时跳过输出
        continue
    print('6当前变量值 :', var)
print("Good bye!")

# 循环语句可以有 else 子句，它在穷尽列表(以for循环)或条件变为 false (以while循环)导致循环终止时被执行，但循环被 break 终止时不执行。
# 如下实例用于查询质数的循环例子:
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n // x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')

print("*******************************************【5】 pass 语句 *******************************************")
# pass 语句
# Python pass是空语句，是为了保持程序结构的完整性。
# pass 不做任何事情，一般用做占位语句，如下实例
while True:
    pass  # 等待键盘中断 (Ctrl+C)


# 最小的类:
class MyEmptyClass:
    pass


# 以下实例在字母为 o 时 执行 pass 语句块:
for letter in 'Runoob':
    if letter == 'o':
        pass
        print('执行 pass 块')
    print('当前字母 :', letter)

print("Good bye!")

print("*******************************************【6】 笔记 *******************************************")
# 1-100 的和:
print(sum(range(101)))

# 使用内置 enumerate 函数进行遍历:
sequence = [12, 34, 34, 23, 45, 76, 89]
for i, j in enumerate(sequence):
    print(i, j)
