# 字典dict迭代
d = {'a':1,'b':2,'c':3}
# dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样
# 默认情况下，dict迭代的是key。
'''
for key in d:
	print(key)
'''

# 如果要迭代value，可以用for value in d.values()
'''
for value in d.values():
	print(value)
'''

# 如果要同时迭代key和value，可以用for k, v in d.items()
'''
for k,v in d.items():
	print(k,':',v)
'''

# 字符串也是可迭代对象
'''
for ch in 'ABC':
	print(ch)
'''

# 如何判断一个对象是可迭代对象呢？方法是通过collections.abc模块的Iterable类型判断

'''
# 导入模块
from collections.abc import Iterable

# str是否可迭代
print(isinstance('abc',Iterable))

# list是否可迭代
print(isinstance([1,2,3],Iterable))

# 整数是否可迭代
print(isinstance(123,Iterable))
'''

# 在for循环中同时迭代索引和元素本身：
# Python内置的enumerate函数可以把一个list变成索引-元素对
for i,value in enumerate(['A','B','C']):
	print(i,value)
