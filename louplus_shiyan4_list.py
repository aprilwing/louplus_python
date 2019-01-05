#!/usr/bin/env python3

# 1.以下是笔记内容
# '''列表、元组、集合、字典‘’‘
# ’‘’列表list
 list = ['', '', '']
# 以上是笔记内容

# 以下是列表list 的练习题代码：listtest.py：
#!/usr/bin/env python3

import sys

list = sys.argv[1:]

list1 = []
list2 = []

for i in list:
    if len(i) <= 3:
        list1.append(i)
    elif len(i) > 3:
        list2.append(i)

print(list1)
print(list2)
# 以上是练习题listtest.py的代码

# 2.以下是元组tuple的笔记：
‘’‘
tuple是个无序的
tuple创建后,tuple中的元素不能修改，但是其中包含的列表list里的内容可以修改
c_tuple = ('', '', '')
tip1:创建一个元素的tuple，要用('', )
‘’‘
# 以上是元组tuple的笔记

# 3.以下是集合set的笔记：
’‘’
set是一个无序不重复元素的
创建set：方法一：XXX = set()，方法二：xxx = set{}
set可以添加元素
‘’‘
# 以上是set的笔记

#以下是练习题settest.py的代码：
#!/usr/bin/env python3
import sys
set1 = set(sys.argv[1:])
print(set1)
# 以上是settest.py的代码

# 4.以下是字典dict的笔记：
‘’‘
字典是无序的
字典的key不可变，list不能作为key
dict创建：方法一：xxx = {'':''}, 方法二：xxx = dict((('',''), ('','')))
tip1:获取字典某个值，通过[]，[]中不是索引，是输入key，因为字典是无序的
tip2:获取字典所有元素：xxx.items(), 遍历每个元素：for key,value in xxx.items():print(key,value)
或者只获取key或value：xxx.keys()或xxx.values(), 也可遍历
’‘’
# 以上是字典dict的笔记

# 以下是练习题dicttest.py的代码和输出结果：
#!/usr/bin/env python3
import sys
for i in sys.argv[1:]:
    key_value = i.split(':')
    key = key_value[0]
    value = key_value[1]
    print('ID:{}'.format(key), 'Name:{}'.format(value))

shiyanlou:~/ $ python3 dicttest.py 100:shiyan 101:louplus 102:jack 103:lee
ID:100 Name:shiyan
ID:101 Name:louplus
ID:102 Name:jack
ID:103 Name:lee
# 以上是练习题dicttest.py

# 5.以下是‘数据类型转换’的笔记：
‘’‘
5.1. 转换成【列表】或【元组】：
>>> t = ('a', 'b', 'c')  # 将元组转换为列表
>>> list(t)或tuple(t)
['a', 'b', 'c']
>>> d = {'name': 'Tom', 'age': 11}
>>> list(d)  # 将字典的 key 值转换为字典    或tuple(d)
['name', 'age']
>>> list('hello shiyanlou')  # 将字符串中每个字符作为一个元素存入列表
['h', 'e', 'l', 'l', 'o', ' ', 's', 'h', 'i', 'y', 'a', 'n', 'l', 'o', 'u']

5.2.转换成【集合set】：
其他同上，
set(('python', 'louplus', 'python'))
{'python', 'louplus'}

5.3.转换成【dict】，dict转换方法参数必须是元组，元组中每个元素也必须为元组，相当于一对 key-value 键值对
>>> dict((('name', 'Tom'), ('age', 11)))
{'name': 'Tom', 'age': 11}
>>> d = {'name': 'Tom', 'age': 11}
>>> d1 = dict(**d)  # dict 方法也可以接收关键字参数，即把字典对象作为参数
>>> d1  # 这是一个新的字典
{'name': 'Tom', 'age': 11}
>>> d
{'name': 'Tom', 'age': 11}
>>> d1 == d  # 新字典与原字典值相同
True
>>> d1 is d  # 但它们不是同一个对象，在内存中各拥有一段空间，仅仅是值相同而已
False
’‘’
