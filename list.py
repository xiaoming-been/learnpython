# -*- coding: utf-8 -*-

# list(列表)是一种有序的集合，可以随时添加和删除其中的元素
classmates = ['Michael','Bob','Tracy']

# 用len()函数可以获取list元素的个数
print('列表classmates的元素个数：',len(classmates))

# 往list中追加元素到末尾
classmates.append('Adam')
print(classmates)

# 把元素插入到索引为1的位置
classmates.insert(1,'Jack')
print(classmates)

# 删除list末尾的元素，用pop()函数
classmates.pop()
print(classmates)

# 删除指定位置的元素，用pop(i)，其中i是索引位置
classmates.pop(1)
print(classmates)

# 把某个元素替换成别的元素，可以直接赋值给对应的索引位置
classmates[1] = 'Sarah'
print(classmates)

# list里面的元素的数据类型也可以不同，比如
L = ['Apple', 123, True]
print(L)

# list元素也可以是另一个list，比如
# s = ['python', 'java', ['asp', 'php'], 'scheme']
# print(len(s))
# print(s)

p = ['asp', 'php']
s = ['python', 'java', p, 'scheme']
print(s)

# 如果一个list中一个元素也没有，就是一个空的list，它的长度为0
L = []
print('列表L的长度为：',len(L))