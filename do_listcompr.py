# 生成列表
# L=list(range(1,11))
# print(L)

'''
# 生成[1x1, 2x2, 3x3, ..., 10x10]
L = []
for x in range(1,11):
	L.append(x*x)

print(L)
'''

# L = [x*x for x in range(1,11)]
# print(L)

# 筛选出仅偶数的平方
# L = [x*x for x in range(1,11) if x%2==0]
# print(L)

# 使用两层循环，可以生成全排列
# L = [m + n for m in 'ABC' for n in 'XYZ']
# print(L)

# 导入os模块
# import os

# os.listdir可以列出文件和目录
# L = [d for d in os.listdir('.')]
# print(L)

# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value
# d = {'x':'A','y':'B','z':'C'}
# for k,v in d.items():
#	print(k, '=', v)

# 列表生成式也可以使用两个变量来生成list(无序)
# L = [k + '=' + v for k,v in d.items()]
# print(L)

# 把一个list中所有的字符串变成小写
# L = ['Hello','World','IBM','Apple']
# L = [s.lower() for s in L]
# print(L)

# 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错
# L = ['Hello','World',18,'Aplle',None]
# L = [s.lower() for s in L]
# print(L)

# 使用内建的isinstance函数可以判断一个变量是不是字符串
# x = 'abc'
# y = 123
# print(isinstance(x,str))
# print(isinstance(y,str))

# 请修改列表生成式，通过添加if语句保证列表生成式能正确地执行
L1 = ['Hello','World',18,'Aplle',None]

# 筛选字符串并小写
L2 = [s.lower() for s in L1 if isinstance(s,str)]
print(L2)

# 筛选字符串小写并保留其他元素
L3 = [s.lower() if isinstance(s,str) else s for s in L1 ]
print(L3)


