# !/usr/local/bin/python3.12
# Python3 迭代器与生成器
print("【1】 迭代器 *******************************************")
# 迭代是 Python 最强大的功能之一，是访问集合元素的一种方式。
# 迭代器是一个可以记住遍历的位置的对象。
# 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
# 迭代器有两个基本的方法：iter() 和 next()。
# 字符串，列表或元组对象都可用于创建迭代器：
list = [1, 2, 3, 4]
it = iter(list)  # 创建迭代器对象
print(next(it))  # 输出迭代器的下一个元素
print(next(it))

# 迭代器对象可以使用常规for语句进行遍历：
list = [1, 2, 3, 4]
it = iter(list)  # 创建迭代器对象
for x in it:
    print(x, end=" ")

# 也可以使用 next() 函数：
import sys  # 引入 sys 模块

list = [1, 2, 3, 4]
it = iter(list)  # 创建迭代器对象

while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()

print("【2】 创建一个迭代器 *******************************************")


# 把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__() 。
# 如果你已经了解的面向对象编程，就知道类都有一个构造函数，Python 的构造函数为 __init__(), 它会在对象初始化的时候执行。
# 更多内容查阅：Python3 面向对象
# __iter__() 方法返回一个特殊的迭代器对象， 这个迭代器对象实现了 __next__() 方法并通过 StopIteration 异常标识迭代的完成。
# __next__() 方法（Python 2 里是 next()）会返回下一个迭代器对象。
# 创建一个返回数字的迭代器，初始值为 1，逐步递增 1：
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

print("【3】 StopIteration *******************************************")


# StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况，在 __next__() 方法中我们可以设置在完成指定循环次数后触发 StopIteration 异常来结束迭代。
# 在 20 次迭代后停止执行：
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)

print("【4】 生成器 *******************************************")


# 在 Python 中，使用了 yield 的函数被称为生成器（generator）。
# yield 是一个关键字，用于定义生成器函数，生成器函数是一种特殊的函数，可以在迭代过程中逐步产生值，而不是一次性返回所有结果。
# 跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
# 当在生成器函数中使用 yield 语句时，函数的执行将会暂停，并将 yield 后面的表达式作为当前迭代的值返回。
# 然后，每次调用生成器的 next() 方法或使用 for 循环进行迭代时，函数会从上次暂停的地方继续执行，直到再次遇到 yield 语句。这样，生成器函数可以逐步产生值，而不需要一次性计算并返回所有结果。
# 调用一个生成器函数，返回的是一个迭代器对象。
# 下面是一个简单的示例，展示了生成器函数的使用：
def countdown(n):
    while n > 0:
        yield n
        n -= 1


# 创建生成器对象
generator = countdown(5)

# 通过迭代生成器获取值
print(next(generator))  # 输出: 5
print(next(generator))  # 输出: 4
print(next(generator))  # 输出: 3

# 使用 for 循环迭代生成器
for value in generator:
    print(value)  # 输出: 2 1

# 以上实例中，countdown 函数是一个生成器函数。它使用 yield 语句逐步产生从 n 到 1 的倒数数字。在每次调用 yield 语句时，函数会返回当前的倒数值，并在下一次调用时从上次暂停的地方继续执行。
# 通过创建生成器对象并使用 next() 函数或 for 循环迭代生成器，我们可以逐步获取生成器函数产生的值。在这个例子中，我们首先使用 next() 函数获取前三个倒数值，然后通过 for 循环获取剩下的两个倒数值。
# 生成器函数的优势是它们可以按需生成值，避免一次性生成大量数据并占用大量内存。此外，生成器还可以与其他迭代工具（如for循环）无缝配合使用，提供简洁和高效的迭代方式。

# 以下实例使用 yield 实现斐波那契数列：
import sys


def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()

print("【5】 笔记 *******************************************")
# 来看一下有yield和没有yield的情况会对生成器了解多点：

# 第一种：使用 yield
import sys


def fibonacci(n, w=0):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        print('%d,%d' % (a, b))
        counter += 1


f = fibonacci(10, 0)  # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f), end=" ")
    except:
        sys.exit()
# 输出结果：
#
# 0 1,1
# 1 1,2
# 1 2,3
# 2 3,5
# 3 5,8
# 5 8,13
# 8 13,21
# 13 21,34
# 21 34,55
# 34 55,89
# 55 89,144

# 第二种：不使用 yield

import sys


def fibonacci(n, w=0):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        # yield a
        a, b = b, a + b
        print('%d,%d' % (a, b))
        counter += 1


f = fibonacci(10, 0)  # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f), end=" ")
    except:
        sys.exit()
    # 输出结果：
    #
    # 1,1
    # 1,2
    # 2,3
    # 3,5
    # 5,8
    # 8,13
    # 13,21
    # 21,34
    # 34,55
    # 55,89
    # 89,144

    # 第二种没有yield时，函数只是简单执行，没有返回迭代器f。这里的迭代器可以用生成l列表来理解一下：

l = [i for i in range(0, 15)]
print(l)
m = (i for i in range(0, 15))
print(m)
for g in m:
    print(g, end=', ')


# 这里的m就像上面的f一样，是迭代器。


# 什么情况下需要使用 yield？
# 一个函数 f，f 返回一个 list，这个 list 是动态计算出来的（不管是数学上的计算还是逻辑上的读取格式化），并且这个 list 会很大（无论是固定很大还是随着输入参数的增大而增大），这个时候，我们希望每次调用这个函数并使用迭代器进行循环的时候一个一个的得到每个 list 元素而不是直接得到一个完整的 list 来节省内存，这个时候 yield 就很有用。
# 具体怎么使用 yield 参考：Python yield 使用浅析
# 以斐波那契函数为例，我们一般希望从 n 返回一个 n 个数的 list：

def fab(max):
    n, a, b = 0, 0, 1
    L = []
    while n < max:
        L.append(b)
        a, b = b, a + b
        n = n + 1
    return L


# 上面那个 fab 函数从参数 max 返回一个有 max 个元素的 list，当这个 max 很大的时候，会非常的占用内存。
# 一般我们使用的时候都是这个样子的，比如：
f = iter(fab(1000))
while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()


# 这样我们实际上是先生成了一个 1000 个元素的 list:f，然后我们再去使用这个 f。
# 现在，我们换一个方法：
# 因为我们实际使用的是 list 的遍历，也就是 list 的迭代器。那么我们可以让这个函数 fab 每次只返回一个迭代器——一个计算结果，而不是一个完整的 list：

def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        # print b
        a, b = b, a + b
        n = n + 1


# 这样，我们每次调用fab函数，比如这样：
for x in fab(1000):
    print(x)


# 或者 next 函数之类的，实际上的运行方式是每次的调用都在 yield 处中断并返回一个结果，然后再次调用的时候再恢复中断继续运行。


# 对yield的测试结果：
# 打个比方的话，yield有点像断点。     加了yield的函数，每次执行到有yield的时候，会返回yield后面的值 并且函数会暂停，直到下次调用或迭代终止；
# yield后面可以加多个数值（可以是任意类型），但返回的值是元组类型的。
def get():
    m = 0
    n = 2
    l = ['s', 1, 3]
    k = {1: 1, 2: 2}
    p = ('2', 's', 't')
    while True:
        m += 1
        yield m
        yield m, n, l, k, p


it = get()
print(next(it))  # 1
print(next(it))  # (1, 2, ['s', 1, 3], {1: 1, 2: 2}, ('2', 's', 't'))

print(next(it))  # 2
print(type(next(it)))  # <class 'tuple'>
