# !/usr/local/bin/python3.12
# Python3 列表
# 序列是 Python 中最基本的数据结构。
# 序列中的每个值都有对应的位置值，称之为索引，第一个索引是 0，第二个索引是 1，依此类推。
# Python 有 6 个序列的内置类型，但最常见的是列表和元组。
# 列表都可以进行的操作包括索引，切片，加，乘，检查成员。
# 此外，Python 已经内置确定序列的长度以及确定最大和最小的元素的方法。
# 列表是最常用的 Python 数据类型，它可以作为一个方括号内的逗号分隔值出现。
# 列表的数据项不需要具有相同的类型
# 创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可。如下所示：
list1 = ['Google', 'Runoob', 1997, 2000]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]
list4 = ['red', 'green', 'blue', 'yellow', 'white', 'black']

print("【1】访问列表中的值 *******************************************")
# 与字符串的索引一样，列表索引从 0 开始，第二个索引是 1，依此类推。
# 通过索引列表可以进行截取、组合等操作。
list = ['red', 'green', 'blue', 'yellow', 'white', 'black']
print(list[0])
print(list[1])
print(list[2])
# 索引也可以从尾部开始，最后一个元素的索引为 -1，往前一位为 -2，以此类推。
list = ['red', 'green', 'blue', 'yellow', 'white', 'black']
print(list[-1])
print(list[-2])
print(list[-3])
# 使用下标索引来访问列表中的值，同样你也可以使用方括号 [] 的形式截取字符，如下所示：
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(nums[0:4])
# 使用负数索引值截取：
list = ['Google', 'Runoob', "Zhihu", "Taobao", "Wiki"]

# 读取第二位
print("list[1]: ", list[1])
# 从第二位开始（包含）截取到倒数第二位（不包含）
print("list[1:-2]: ", list[1:-2])

print("【2】更新列表 *******************************************")
# 你可以对列表的数据项进行修改或更新，你也可以使用 append() 方法来添加列表项，如下所示：
list = ['Google', 'Runoob', 1997, 2000]

print("第三个元素为 : ", list[2])
list[2] = 2001
print("更新后的第三个元素为 : ", list[2])

list1 = ['Google', 'Runoob', 'Taobao']
list1.append('Baidu')
print("更新后的列表 : ", list1)

print("【3】删除列表元素 *******************************************")
# 可以使用 del 语句来删除列表中的元素，如下实例：
list = ['Google', 'Runoob', 1997, 2000]

print("原始列表 : ", list)
del list[2]
print("删除第三个元素 : ", list)

print("【4】Python列表脚本操作符 *******************************************")
# 列表对 + 和 * 的操作符与字符串相似。+ 号用于组合列表，* 号用于重复列表。
# 如下所示：
# Python 表达式	                            结果	                                描述
# len([1, 2, 3])	                        3	                                    长度
# [1, 2, 3] + [4, 5, 6]	                    [1, 2, 3, 4, 5, 6]	                    组合
# ['Hi!'] * 4	                            ['Hi!', 'Hi!', 'Hi!', 'Hi!']	        重复
# 3 in [1, 2, 3]	                        True	                                元素是否存在于列表中
# for x in [1, 2, 3]: print(x, end=" ") 	1 2 3	                                迭代

print("【5】Python 列表截取与拼接 *******************************************")
# Python 的列表截取与字符串操作类似，如下所示：
L = ['Google', 'Runoob', 'Taobao']
# Python 表达式	        结果	                    描述
# L[2]	                'Taobao'	                读取第三个元素
# L[-2]                 'Runoob'	                从右侧开始读取倒数第二个元素: count from the right
# L[1:]	                ['Runoob', 'Taobao']	    输出从第二个元素开始后的所有元素
L = ['Google', 'Runoob', 'Taobao']
print(L[2])
print(L[-2])
print(L[1:])
# 列表还支持拼接操作：
squares = [1, 4, 9, 16, 25]
squares += [36, 49, 64, 81, 100]
print(squares)

print("【6】嵌套列表 *******************************************")
# 使用嵌套列表即在列表里创建其它列表，例如：
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[0][1])

print("【7】列表比较 *******************************************")
# 列表比较需要引入 operator 模块的 eq 方法
# 导入 operator 模块
import operator

a = [1, 2]
b = [2, 3]
c = [2, 3]
print("operator.eq(a,b): ", operator.eq(a, b))
print("operator.eq(c,b): ", operator.eq(c, b))

print("【8】Python列表函数&方法 *******************************************")
# Python包含以下函数:
# 方法                                       说明
# len(list)                                 列表元素个数
# max(list)                                 返回列表元素最大值
# min(list)                                 返回列表元素最小值
# ist(seq)                                  将元组转换为列表

# list.append(obj)                          在列表末尾添加新的对象
# list.count(obj)                           统计某个元素在列表中出现的次数
# list.extend(seq)                          在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
# list.index(obj)                           从列表中找出某个值第一个匹配项的索引位置
# list.insert(index, obj)                   将对象插入列表
# list.pop([index=-1])                      移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
# list.remove(obj)                          移除列表中某个值的第一个匹配项
# list.reverse()                            反向列表中元素
# list.sort( key=None, reverse=False)       对原列表进行排序
# list.clear()                              清空列表
# list.copy()                               复制列表

print("【9】笔记 *******************************************")
# python 创建二维列表，将需要的参数写入 cols 和 rows 即可
# list_2d = [[0 for col in range(cols)] for row in range(rows)]
list_2d = [[0 for i in range(5)] for i in range(5)]
list_2d[0].append(3)
list_2d[0].append(5)
list_2d[2].append(7)
print(list_2d)

# 列表的复制
# >>> a = [1, 2, 3]
# >>> b = a
# >>> c = []
# >>> c = a
# >>> d = a[:]
# >>> a, b, c, d
# ([1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3])
# >>> b[0] = 'b'
# >>> a, b, c, d
# (['b', 2, 3], ['b', 2, 3], ['b', 2, 3], [1, 2, 3])
# >>> id(a), id(b), id(c), id(d)
# (140180778120200, 140180778120200, 140180778120200, 140180778122696)
# >>> c[0] = 'c'
# >>> a, b, c, d
# (['c', 2, 3], ['c', 2, 3], ['c', 2, 3], [1, 2, 3])
# >>> id(a), id(b), id(c), id(d)
# (140180778120200, 140180778120200, 140180778120200, 140180778122696)
# >>> d[0] = 'd'
# >>> a, b, c, d
# (['c', 2, 3], ['c', 2, 3], ['c', 2, 3], ['d', 2, 3])
# >>> id(a), id(b), id(c), id(d)
# (140180778120200, 140180778120200, 140180778120200, 140180778122696)

# 可以看到a b c 三个是同一id值，当改变当中任一列表元素的值后，三者会同步改变。
# 但d的元素值不会变，改变d的元素值其它三个变量内的元素值也不会变。
# 从a b c d 的id值来看，a b c 地址全一样，唯有d分配了新地址。
# 所以一般情况下想复制得到一个新列表并改变新列表内元素而不影响原列表，可以采用d的赋值方式。
# 这只是针对这种比较单一的普通列表。

# 分享一个例子，刚学，错了别喷:

l = [i for i in range(0, 15)]
print(l[::2])
# 我们可以看到l后面跟了两个冒号，还有个 2 ，效果：

l = [i for i in range(0, 15)]
print(l[::2])

# 我理解为:
# l[start:end:span]
# 遍历 [start,end)，间隔为 span，当 span>0 时顺序遍历, 当 span<0 时，逆着遍历。
# start 不输入则默认为 0，end 不输入默认为长度。
