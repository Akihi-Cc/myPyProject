# !/usr/local/bin/python3.12
# Python3 集合
# 集合（set）是一个无序的不重复元素序列。
# 集合中的元素不会重复，并且可以进行交集、并集、差集等常见的集合操作。
# 可以使用大括号 { } 创建集合，元素之间用逗号 , 分隔， 或者也可以使用 set() 函数创建集合。
# 创建格式：
# parame = {value01,value02,...}
# 或者
# set(value)
# 以下是一个简单实例：
set1 = {1, 2, 3, 4}  # 直接使用大括号创建集合
print(set1)
set2 = set([4, 5, 6, 7])  # 使用 set() 函数从列表创建集合
print(set2)
# 注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

# 更多实例演示：
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  # 这里演示的是去重功能
print('orange' in basket)  # 快速判断元素是否在集合内
print('crabgrass' in basket)

# 下面展示两个集合间的运算.
a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
print(a - b)  # 集合a中包含而集合b中不包含的元素
{'r', 'd', 'b'}
print(a | b)  # 集合a或b中包含的所有元素
print(a & b)  # 集合a和b中都包含了的元素
print(a ^ b)  # 不同时包含于a和b的元素

# 类似列表推导式，同样集合支持集合推导式(Set comprehension):
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

print("【1】 集合的基本操作 *******************************************")
# 1、添加元素
# 语法格式如下：
# s.add(x)
# 将元素 x 添加到集合 s 中，如果元素已存在，则不进行任何操作。
thisset = set(("Google", "Runoob", "Taobao"))
thisset.add("Facebook")
print(thisset)
# 还有一个方法，也可以添加元素，且参数可以是列表，元组，字典等，语法格式如下：
# s.update( x )
# x 可以有多个，用逗号分开。
thisset = set(("Google", "Runoob", "Taobao"))
thisset.update({1, 3})
print(thisset)
thisset.update([1, 4], [5, 6])
print(thisset)

# 2、移除元素
# 语法格式如下：
# s.remove( x )
# 将元素 x 从集合 s 中移除，如果元素不存在，则会发生错误。
thisset = set(("Google", "Runoob", "Taobao"))
thisset.remove("Taobao")
print(thisset)
# thisset.remove("Facebook")  # 不存在会发生错误 异常 KeyError: 'Facebook'

# 此外还有一个方法也是移除集合中的元素，且如果元素不存在，不会发生错误。格式如下所示：
# s.discard( x )
thisset = set(("Google", "Runoob", "Taobao"))
thisset.discard("Facebook")  # 不存在不会发生错误
print(thisset)

# 我们也可以设置随机删除集合中的一个元素，语法格式如下：
# s.pop()
thisset = set(("Google", "Runoob", "Taobao", "Facebook"))
x = thisset.pop()
print(x)
# 多次执行测试结果都不一样。
# set 集合的 pop 方法会对集合进行无序的排列，然后将这个无序排列集合的左面第一个元素进行删除。

# 3、计算集合元素个数
# 语法格式如下：
# len(s)
# 计算集合 s 元素个数。
thisset = set(("Google", "Runoob", "Taobao"))
print(len(thisset))

# 4、清空集合
# 语法格式如下：
# s.clear()
# 清空集合 s。
thisset = set(("Google", "Runoob", "Taobao"))
thisset.clear()
print(thisset)
set()

# 5、判断元素是否在集合中存在
# 语法格式如下：
# x in s
# 判断元素 x 是否在集合 s 中，存在返回 True，不存在返回 False。
thisset = set(("Google", "Runoob", "Taobao"))
print("Runoob" in thisset)
print("Facebook" in thisset)

# 集合内置方法完整列表
# 方法	                            描述
# add()	                            为集合添加元素
# clear()	                        移除集合中的所有元素
# copy()	                        拷贝一个集合
# difference()	                    返回多个集合的差集
# difference_update()	            移除集合中的元素，该元素在指定的集合也存在。
# discard()	                        删除集合中指定的元素
# intersection()	                返回集合的交集
# intersection_update()	            返回集合的交集。
# isdisjoint()	                    判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
# issubset()	                    判断指定集合是否为该方法参数集合的子集。
# issuperset()	                    判断该方法的参数集合是否为指定集合的子集
# pop()	                            随机移除元素
# remove()	                        移除指定元素
# symmetric_difference()	        返回两个集合中不重复的元素集合。
# symmetric_difference_update()	    移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
# union()	                        返回两个集合的并集
# update()	                        给集合添加元素
# len()	                            计算集合元素个数

print("【2】 笔记 *******************************************")
# s.update( "字符串" ) 与 s.update( {"字符串"} ) 含义不同:
# s.update( {"字符串"} ) 将字符串添加到集合中，有重复的会忽略。
# s.update( "字符串" ) 将字符串拆分单个字符后，然后再一个个添加到集合中，有重复的会忽略。
thisset = set(("Google", "Runoob", "Taobao"))
print(thisset)
thisset.update({"Facebook"})
print(thisset)
thisset.update("Yahoo")
print(thisset)

# set() 中参数注意事项
# 1.创建一个含有一个元素的集合
my_set = set(('apple',))
print(my_set)

# 2.创建一个含有多个元素的集合
my_set = set(('apple', 'pear', 'banana'))
print(my_set)

# 3.如无必要，不要写成如下形式
my_set = set('apple')
print(my_set)
my_set1 = set(('apple'))
print(my_set1)
