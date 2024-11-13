# !/usr/local/bin/python3.12
# Python3 字典
# 字典是另一种可变容器模型，且可存储任意类型对象。
# 字典的每个键值 key=>value 对用冒号 : 分割，每个对之间用逗号(,)分割，整个字典包括在花括号 {} 中 ,格式如下所示：
# d = {key1 : value1, key2 : value2, key3 : value3 }
# 注意：dict 作为 Python 的关键字和内置函数，变量名不建议命名为 dict。
# 键必须是唯一的，但值则不必。
# 值可以取任何数据类型，但键必须是不可变的，如字符串，数字。
# 一个简单的字典实例：
tinydict = {'name': 'runoob', 'likes': 123, 'url': 'www.runoob.com'}
print(tinydict)
# 也可如此创建字典：
tinydict1 = {'abc': 456}
tinydict2 = {'abc': 123, 98.6: 37}
print(tinydict1)
print(tinydict2)

print("*******************************************【1】 创建空字典 *******************************************")
# 使用大括号 { } 创建空字典：
# 使用大括号 {} 来创建空字典
emptyDict = {}
# 打印字典
print(emptyDict)
# 查看字典的数量
print("Length:", len(emptyDict))
# 查看类型
print(type(emptyDict))

# 使用内建函数 dict() 创建字典：
emptyDict = dict()
# 打印字典
print(emptyDict)
# 查看字典的数量
print("Length:", len(emptyDict))
# 查看类型
print(type(emptyDict))

print("*******************************************【2】 访问字典里的值 *******************************************")
# 把相应的键放入到方括号中，如下实例:
tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print("tinydict['Name']: ", tinydict['Name'])
print("tinydict['Age']: ", tinydict['Age'])
# 如果用字典里没有的键访问数据，会输出错误如下：
tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# print("tinydict['Alice']: ", tinydict['Alice'])  #异常 KeyError: 'Alice'

print("*******************************************【3】 修改字典 *******************************************")
# 向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对如下实例:
tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
tinydict['Age'] = 8  # 更新 Age
tinydict['School'] = "菜鸟教程"  # 添加信息
print("tinydict['Age']: ", tinydict['Age'])
print("tinydict['School']: ", tinydict['School'])

print("*******************************************【4】 删除字典元素 *******************************************")
# 能删单一的元素也能清空字典，清空只需一项操作。
# 显式删除一个字典用del命令，如下实例：
tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
del tinydict['Name']  # 删除键 'Name'
tinydict.clear()  # 清空字典
del tinydict  # 删除字典
# print("tinydict['Age']: ", tinydict['Age'])  # 异常 NameError: name 'tinydict' is not defined
# print("tinydict['School']: ", tinydict['School']) # 异常 NameError: name 'tinydict' is not defined. Did you mean: 'tinydict1'?
# 但这会引发一个异常，因为用执行 del 操作后字典不再存在：

print("*******************************************【5】 字典键的特性 *******************************************")
# 字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行。
# 两个重要的点需要记住：
# 1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，如下实例：
tinydict = {'Name': 'Runoob', 'Age': 7, 'Name': '小菜鸟'}
print("tinydict['Name']: ", tinydict['Name'])
# 2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行，如下实例：
# tinydict = {['Name']: 'Runoob', 'Age': 7}  # 异常 TypeError: unhashable type: 'list'
print("tinydict['Name']: ", tinydict['Name'])

print("*******************************************【6】 字典内置函数&方法 *******************************************")
# Python字典包含了以下内置函数：
# 函数                                       描述
# len(dict)                                 计算字典元素个数，即键的总数。
# str(dict)                                 输出字典，可以打印的字符串表示。
# type(variable)                            返回输入的变量类型，如果变量是字典就返回字典类型。

# dict.clear()                              删除字典内所有元素
# dict.copy()                               返回一个字典的浅复制
# dict.fromkeys()                           创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
# key in dict                               如果键在字典dict里返回true，否则返回false
# dict.items()                              以列表返回一个视图对象
# dict.keys()                               返回一个视图对象
# dict.setdefault(key, default=None)        和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
# dict.update(dict2)                        把字典dict2的键/值对更新到dict里
# dict.values()                             返回一个视图对象
# pop(key[,default])                        删除字典 key（键）所对应的值，返回被删除的值。
# popitem()                                 返回并删除字典中的最后一对键和值。


