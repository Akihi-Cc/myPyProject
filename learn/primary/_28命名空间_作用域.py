# !/usr/local/bin/python3.12
import builtins
# Python3 命名空间和作用域
print("*******************************************【1】 命名空间 *******************************************")
# 先看看官方文档的一段话：
# A namespace is a mapping from names to objects.Most namespaces are currently implemented as Python dictionaries。
# 命名空间(Namespace)是从名称到对象的映射，大部分的命名空间都是通过 Python 字典来实现的。
# 命名空间提供了在项目中避免名字冲突的一种方法。各个命名空间是独立的，没有任何关系的，所以一个命名空间中不能有重名，但不同的命名空间是可以重名而没有任何影响。
# 我们举一个计算机系统中的例子，一个文件夹(目录)中可以包含多个文件夹，每个文件夹中不能有相同的文件名，但不同文件夹中的文件可以重名。

# 命名空间的类型

# 内置命名空间（Built-in Namespace）
# 包含 Python 语言内置的名称，如函数名 abs、len 和异常名称 BaseException、Exception 等。
# 这些名称在 Python 解释器启动时就已经存在，始终可用。

# 全局命名空间（Global Namespace）
# 模块中定义的名称，记录了模块的变量，包括函数、类、其它导入的模块、模块级的变量和常量。
# 全局命名空间在模块加载时创建，在模块执行完毕后销毁。

# 局部命名空间（Local Namespace）
# 函数中定义的名称，记录了函数的变量，包括函数的参数和局部定义的变量。
# 类中定义的名称也属于局部命名空间。
# 局部命名空间在函数调用时创建，在函数返回时销毁。

# 命名空间的生命周期
# 内置命名空间：始终存在，从 Python 解释器启动到关闭。
# 全局命名空间：在模块加载时创建，在模块执行完毕后销毁。
# 局部命名空间：在函数调用时创建，在函数返回时销毁。

# 命名空间的查找顺序
# 当 Python 解释器查找一个名称时，它会按照以下顺序进行查找：
# 局部命名空间（Local）：函数内部的变量。
# 嵌套的局部命名空间（Enclosing）：包含非局部也非全局的变量，例如嵌套函数。
# 全局命名空间（Global）：模块级别的变量。
# 内置命名空间（Built-in）：Python 内置的名称。

# var1 是全局名称
var1 = 5


def some_func():
    # var2 是局部名称
    var2 = 6

    def some_inner_func():
        # var3 是内嵌的局部名称
        var3 = 7


# 相同的对象名称可以存在于多个命名空间中。

# 查看内置命名空间中的所有名称
print(dir(builtins))

print("*******************************************【2】 作用域 *******************************************")
# A scope is a textual region of a Python program where a namespace is directly accessible. "Directly accessible" here means that an unqualified reference to a name attempts to find the name in the namespace.
# 作用域就是一个 Python 程序可以直接访问命名空间的正文区域。
# 在一个 python 程序中，直接访问一个变量，会从内到外依次访问所有的作用域直到找到，否则会报未定义的错误。
# Python 中，程序的变量并不是在哪个位置都可以访问的，访问权限决定于这个变量是在哪里赋值的。
# 变量的作用域决定了在哪一部分程序可以访问哪个特定的变量名称。Python 的作用域一共有4种，分别是：

# 有四种作用域：
# L（Local）：最内层，包含局部变量，比如一个函数/方法内部。
# E（Enclosing）：包含了非局部(non-local)也非全局(non-global)的变量。比如两个嵌套函数，一个函数（或类） A 里面又包含了一个函数 B ，那么对于 B 中的名称来说 A 中的作用域就为 nonlocal。
# G（Global）：当前脚本的最外层，比如当前模块的全局变量。
# B（Built-in）： 包含了内建的变量/关键字等，最后被搜索。
# 规则顺序： L –> E –> G –> B。

# 在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内置中找。
g_count = 0  # 全局作用域


def outer():
    o_count = 1  # 闭包函数外的函数中

    def inner():
        i_count = 2  # 局部作用域


# 内置作用域是通过一个名为 builtin 的标准模块来实现的，但是这个变量名自身并没有放入内置作用域内，所以必须导入这个文件才能够使用它。在Python3.0中，可以使用以下的代码来查看到底预定义了哪些变量:

print(dir(builtins))
# Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，也就是说这些语句内定义的变量，外部也可以访问，如下代码：
if True:
    msg = 'I am from Runoob'
print(msg)


# 实例中 msg 变量定义在 if 语句块中，但外部还是可以访问的。
# 如果将 msg 定义在函数中，则它就是局部变量，外部不能访问：
def test():
    msg_inner = 'I am from Runoob'


# print(msg_inner) # 异常 NameError: name 'msg_inner' is not defined
# 从报错的信息上看，说明了 msg_inner 未定义，无法使用，因为它是局部变量，只有在函数内可以使用。

print("【3】 全局变量和局部变量 *******************************************")
# 定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。
# 局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。调用函数时，所有在函数内声明的变量名称都将被加入到作用域中。如下实例：
total = 0  # 这是一个全局变量


# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2  # total在这里是局部变量.
    print("函数内是局部变量 : ", total)
    return total


# 调用sum函数
sum(10, 20)
print("函数外是全局变量 : ", total)

print("【4】 global 和 nonlocal关键字 *******************************************")
# 当内部作用域想修改外部作用域的变量时，就要用到 global 和 nonlocal 关键字了。
# 以下实例修改全局变量 num：
num = 1


def fun1():
    global num  # 需要使用 global 关键字声明
    print(num)
    num = 123
    print(num)


fun1()
print(num)


# 如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了，如下实例：
def outer():
    num = 10

    def inner():
        nonlocal num  # nonlocal关键字声明
        num = 100
        print(num)

    inner()
    print(num)


outer()

# 另外有一种特殊情况，假设下面这段代码被运行：
a = 10


def test():
    a = a + 1
    print(a)
# test() # 错误信息为局部作用域引用错误，因为 test 函数中的 a 使用的是局部，未定义，无法修改。

# 修改 a 为全局变量：
a = 10


def test():
    global a
    a = a + 1
    print(a)


test()
# 也可以通过函数参数传递：
a = 10


def test(a):
    a = a + 1
    print(a)


test(a)

print("*******************************************【5】 笔记 *******************************************")
# 作为一个从 Java 过来的人来说，Python 的作用域有点奇葩，作为开发者，只需要关注全局作用域和局部作用域就好了，全局作用域就是说白了模块(单个 .py 文件中)直接声明的变量。
# 比如有个 demo.py 的文件，含有以下代码：

var_global = 'global_var'  # 这个var_global就是全局作用域


def globalFunc():
    var_local = 'local_var'  # 这个就是局部变量


class demo():
    class_demo_local_var = 'class member'  # 这里也是局部变量

    def localFunc(self):
        var_locals = 'local_func_var'  # 这里也是局部变量


# 以上只是说明了全局变量仅仅是在 .py 文件中直接声明的变量叫全局变量，还有在 .py 文件中直接写的逻辑代码块中，也是全局变量。也就是说在 if/elif/else/、try/except、for/while 等逻辑代码块中的变量。
# 这个教程中在介绍三种命令空间的时候，说查找变量的顺序为局部的命名空间去 -> 全局命名空间 -> 内置命名空间，但是我理解的变量查找顺序为：当前域 -> 外部域(如果有) -> 全局域 -> 内置域。
# 光说没有什么概念，我们来一段代码就清楚了。
# 我们以 demo1.py 为例子:
global_var = 'this  var  on  global space'
'''
申明global_var这个位置就是全局域，也就是教程中所说的全局作用域，
同时它也是直接声明在文件中的，而不是声明在函数中或者类中的变量
'''


class demo():
    class_demo_local_var = 'class member'
    '''
    虽然class_demo_local_var在这里是局部变量，这个局部变量的域相对于var_locals是外部域，
    所以可以直接被var_locals所在的更小的局部域访问
    '''

    def localFunc(self):
        var_locals = 'local_func_var'
        '''
        这里也是局部变量，但是相对于class_demo_local_var变量，却是更小的域，
        因此class_demo_local_var所在的哪个域无法访问到当前域来
        '''
        print(self.class_demo_local_var)  # 到这里会查找当前域中有没有class_demo_local_var这个变量，然后再到相对于当前域的外部域去查找变量


# 教程中写到 Python 中变量的查找顺序：“在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再去内置中找。可以看一个具体的例子。
# Python 的一个内建值 int，我们首先将其赋值为 0，然后定义一个函数 fun1()。

int = 0
def fun1():
    int = 1
    def fun2():
        int = 2
        print(int)
    fun2()
fun1()  # 输出 2
# 函数 fun1() 的作用就是调用函数 fun2() 来打印 int 的值。
# 输出结果为：2
# 因为 local 中的 int = 2，函数将其打印出来。
# 将函数 fun2() 中的 int = 2 删除：
int = 0
def fun1():
    int = 1
    def fun2():
        print(int)
    fun2()
fun1()  # 输出 1
# 调用函数 fun1() 输出结果为：1
# 因为 local 找不到 int 的值，就去上一层 non-local 寻找，发现 int = 1 并打印。
# 而进一步删除函数 fun1() 中的 int = 1：

int = 0
def fun1():
    def fun2():
        print(int)
    fun2()
fun1() # 输出 0
# 调用函数 fun1() 输出结果为：0
# 因为 local 和 non-local 都找不到 int 的值，便去 global 中寻找，发现 int = 0 并打印。
# 若删除 int = 0这一条件：

def fun1():
    def fun2():
        print(int)
    fun2()
fun1()
# 调用函数 fun1() 输出结果如下：
# <class 'int'>
# 因为 local、non-local、global 中都没有 int 的值，便去 built-in 中寻找 int 的值，即：
#
# >>> int
# <class 'int'>