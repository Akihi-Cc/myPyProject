# !/usr/local/bin/python3.12
import requests

# Python3 面向对象
# Python从设计之初就已经是一门面向对象的语言，正因为如此，在Python中创建一个类和对象是很容易的。本章节我们将详细介绍Python的面向对象编程。
# 如果你以前没有接触过面向对象的编程语言，那你可能需要先了解一些面向对象语言的一些基本特征，在头脑里头形成一个基本的面向对象的概念，这样有助于你更容易的学习Python的面向对象编程。
# 接下来我们先来简单的了解下面向对象的一些基本特征。
print("*******************************************【1】 面向对象技术简介 *******************************************")
# 类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
# 方法：类中定义的函数。
# 类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
# 数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。
# 方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
# 局部变量：定义在方法中的变量，只作用于当前实例的类。
# 实例变量：在类的声明中，属性是用变量来表示的，这种变量就称为实例变量，实例变量就是一个用 self 修饰的变量。
# 继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
# 实例化：创建一个类的实例，类的具体对象。
# 对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。
# 和其它编程语言相比，Python 在尽可能不增加新的语法和语义的情况下加入了类机制。
# Python中的类提供了面向对象编程的所有基本功能：类的继承机制允许多个基类，派生类可以覆盖基类中的任何方法，方法中可以调用基类中的同名方法。
# 对象可以包含任意数量和类型的数据。
print("*******************************************【2】 类定义 *******************************************")
# 语法格式如下：
# class ClassName:
#     <statement-1>
#     .
#     .
#     <statement-N>
# 类实例化后，可以使用其属性，实际上，创建一个类之后，可以通过类名访问其属性。
print("*******************************************【3】 类对象 *******************************************")


# 类对象支持两种操作：属性引用和实例化。
# 属性引用使用和 Python 中所有的属性引用一样的标准语法：obj.name。
# 类对象创建后，类命名空间中所有的命名都是有效属性名。所以如果类定义是这样:

class MyClass:
    """一个简单的类实例"""
    i = 12345

    def f(self):
        return 'hello world'


# 实例化类
x = MyClass()

# 访问类的属性和方法
print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的方法 f 输出为：", x.f())


# 以上创建了一个新的类实例并将该对象赋给局部变量 x，x 为空的对象。
# 类有一个名为 __init__() 的特殊方法（构造方法），该方法在类实例化时会自动调用，像下面这样：
# def __init__(self):
#     self.data = []
# 类定义了 __init__() 方法，类的实例化操作会自动调用 __init__() 方法。如下实例化类 MyClass，对应的 __init__() 方法就会被调用:
# x = MyClass()
# 当然， __init__() 方法可以有参数，参数通过 __init__() 传递到类的实例化操作上。例如:

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = Complex(3.0, -4.5)
print(x.r, x.i)  # 输出结果：3.0 -4.5


# self 代表类的实例，而非类
# 类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。
class Test:
    def prt(self):
        print(self)
        print(self.__class__)


t = Test()
t.prt()


# 从执行结果可以很明显的看出，self 代表的是类的实例，代表当前对象的地址，而 self.class 则指向类。
# self 不是 python 关键字，我们把他换成 runoob 也是可以正常执行的:
class Test:
    def prt(runoob):
        print(runoob)
        print(runoob.__class__)


t = Test()
t.prt()


# 在 Python中，self 是一个惯用的名称，用于表示类的实例（对象）自身。它是一个指向实例的引用，使得类的方法能够访问和操作实例的属性。
# 当你定义一个类，并在类中定义方法时，第一个参数通常被命名为 self，尽管你可以使用其他名称，但强烈建议使用 self，以保持代码的一致性和可读性。
class MyClass:
    def __init__(self, value):
        self.value = value

    def display_value(self):
        print(self.value)


# 创建一个类的实例
obj = MyClass(42)

# 调用实例的方法
obj.display_value()  # 输出 42
# 在上面的例子中，self 是一个指向类实例的引用，它在 __init__ 构造函数中用于初始化实例的属性，也在 display_value 方法中用于访问实例的属性。通过使用 self，你可以在类的方法中访问和操作实例的属性，从而实现类的行为。

print("*******************************************【4】 类的方法 *******************************************")


# 在类的内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self, 且为第一个参数，self 代表的是类的实例。
# 类属性：在整个类的所有实例之间共享，通过类名或实例访问。
# 实例属性：每个实例都有自己独立的属性，通过实例访问。
# 私有属性：以双下划线 __ 开头，只能通过类中的方法访问和修改。
# 动态属性：可以在类的实例上动态添加属性。
# 类定义
class People:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


# 实例化类
p = People('runoob', 10, 30)
p.speak()

print("*******************************************【5】 继承 *******************************************")


# Python 同样支持类的继承，如果一种语言不支持继承，类就没有什么意义。派生类的定义如下所示:
# class DerivedClassName(BaseClassName):
#     <statement-1>
#     .
#     .
#     <statement-N>
# 子类（派生类 DerivedClassName）会继承父类（基类 BaseClassName）的属性和方法。
# BaseClassName（实例中的基类名）必须与派生类定义在一个作用域内。除了类，还可以用表达式，基类定义在另一个模块中时这一点非常有用:
# class DerivedClassName(modname.BaseClassName):
# 类定义
class People:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


# 单继承示例
class Student(People):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构函
        People.__init__(self, n, a, w)
        self.grade = g

    # 覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


s = Student('ken', 10, 60, 3)
s.speak()

print("【6】 多继承 *******************************************")


# Python同样有限的支持多继承形式。多继承的类定义形如下例:
# class DerivedClassName(Base1, Base2, Base3):
#     <statement-1>
#     .
#     .
#     <statement-N>
# 需要注意圆括号中父类的顺序，若是父类中有相同的方法名，而在子类使用时未指定，python从左至右搜索 即方法在子类中未找到时，从左到右查找父类中是否包含方法。
# 类定义
class People:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


# 单继承示例
class Student(People):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构函
        People.__init__(self, n, a, w)
        self.grade = g

    # 覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


# 另一个类，多继承之前的准备
class Speaker:
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))


# 多继承
class Sample(Speaker, Student):
    a = ''

    def __init__(self, n, a, w, g, t):
        Student.__init__(self, n, a, w, g)
        Speaker.__init__(self, n, t)


test = Sample("Tim", 25, 80, 4, "Python")
test.speak()  # 方法名同，默认调用的是在括号中参数位置排前父类的方法

print("*******************************************【7】 方法重写 *******************************************")


# 如果你的父类方法的功能不能满足你的需求，你可以在子类重写你父类的方法，实例如下：
class Parent:  # 定义父类
    def myMethod(self):
        print('调用父类方法')


class Child(Parent):  # 定义子类
    def myMethod(self):
        print('调用子类方法')


c = Child()  # 子类实例
c.myMethod()  # 子类调用重写方法
super(Child, c).myMethod()  # 用子类对象调用父类已被覆盖的方法
# super() 函数是用于调用父类(超类)的一个方法。

print("*******************************************【8】 类属性与方法 *******************************************")


# 类的私有属性
# __private_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。
# 类的方法
# 在类的内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self，且为第一个参数，self 代表的是类的实例。
# self 的名字并不是规定死的，也可以使用 this，但是最好还是按照约定使用 self。
# 类的私有方法
# __private_method：两个下划线开头，声明该方法为私有方法，只能在类的内部调用 ，不能在类的外部调用。self.__private_methods。
# 类的私有属性实例如下：
class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0  # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)


counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)


# print(counter.__secretCount)  # 报错，实例不能访问私有变量


# 类的私有方法实例如下：
class Site:
    def __init__(self, name, url):
        self.name = name  # public
        self.__url = url  # private

    def who(self):
        print('name  : ', self.name)
        print('url : ', self.__url)

    def __foo(self):  # 私有方法
        print('这是私有方法')

    def foo(self):  # 公共方法
        print('这是公共方法')
        self.__foo()


x = Site('菜鸟教程', 'www.runoob.com')
x.who()  # 正常输出
x.foo()  # 正常输出
# x.__foo()  # 报错

# 类的专有方法：
# __init__ : 构造函数，在生成对象时调用
# __del__ : 析构函数，释放对象时使用
# __repr__ : 打印，转换
# __setitem__ : 按照索引赋值
# __getitem__: 按照索引获取值
# __len__: 获得长度
# __cmp__: 比较运算
# __call__: 函数调用
# __add__: 加运算
# __sub__: 减运算
# __mul__: 乘运算
# __truediv__: 除运算
# __mod__: 求余运算
# __pow__: 乘方

print("*******************************************【9】 运算符重载 *******************************************")


# Python同样支持运算符重载，我们可以对类的专有方法进行重载，实例如下：
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)

print("*******************************************【10】 笔记 *******************************************")


# 针对 __str__ 方法给出一个比较直观的例子：

class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '这个人的名字是%s,已经有%d岁了！' % (self.name, self.age)


a = People('孙悟空', 999)
print(a)


# Python3 中类的静态方法、普通方法、类方法

# 静态方法:
# 定义：静态方法使用 @staticmethod 装饰器定义，不需要 self 或 cls 参数。
# 调用：可以通过类或类的实例调用。
# 用途：用于定义与类或实例无关的工具方法，通常用于辅助功能。

# 普通方法:
# 定义：普通方法是默认的方法类型，它必须有一个 self 参数，表示类的实例。
# 调用：只能通过类的实例调用。
# 用途：用于操作实例属性，完成实例相关的功能。

# 类方法:
# 定义：类方法使用 @classmethod 装饰器定义，必须有一个 cls 参数，表示类本身。
# 调用：可以通过类或类的实例调用。
# 用途：用于操作类属性，完成类相关的功能。

class Classname:
    @staticmethod
    def fun():
        print('静态方法')

    @classmethod
    def a(cls):
        print('类方法')

    # 普通方法
    def b(self):
        print('普通方法')


Classname.fun()
Classname.a()

C = Classname()
C.fun()
C.a()
C.b()


# 关于 __name__
# 比如所示的一段代码里面（这个脚本命名为 pcRequests.py），我只设了一个函数，但是并没有地方运行它，所以当 run 了这一段代码之后我们有会发现这个函数并没有被调用。
# 但是当我们在运行这个代码时这个代码的 __name__ 的值为 __main__ （一段程序作为主线运行程序时其内置名称就是 __main__）。

# 首先需要了解 __name__ 是属于 python 中的内置类属性，就是它会天生就存在于一个 python 程序中，代表对应程序名称。
class Requests(object):
    def __init__(self, url):
        self.url = url
        self.result = self.getHTMLText(self.url)

    def getHTMLText(url):
        try:
            r = Requests.get(url, timeout=30)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            return r.text
        except:
            return "This is a error."


print(__name__)

# 结果：
# __main__
# Process finished with exit code 0
# 当这个 pcRequests.py 作为模块被调用时，则它的 __name__ 就是它自己的名字：
# import pcRequestspcRequestsc=pcRequestsc.__name__
# 结果：
# 'pcRequests'

# 看到这里应该能明白，自己的 __name__ 在自己用时就是 main，当自己作为模块被调用时就是自己的名字，就相当于：我管自己叫我自己，但是在朋友眼里我就是小仙女一样。
