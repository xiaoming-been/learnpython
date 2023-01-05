# 构造一个1, 3, 5, 7, ..., 99的列表，可以通过循环实现
'''
L = []
n = 1
while n <=99:
	L.append(n)
	n = n + 2
print(L)
'''
# 切片
'''
L = ['Michael','Sarah','Tracy','Bob','Jack']
r = []
n = 3
for i in range(n):
	r.append(L[i])
print(r)

# L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素
print(L[0:3])

# 如果第一个索引是0，还可以省略
print(L[:3])

# 也可以从索引1开始，取出2个元素出来
print(L[1:3])

# 倒数第一个元素的索引是-1
print(L[-2:])
'''
'''
# 创建一个0-99的数列
L = list(range(100))
print(L)

# 前十个数
print(L[:10])

# 后十个数
print(L[-10:])

# 前十一到二十个数
print(L[10:20])

# 前10个数，每两个取一个
print(L[:10:2])

# 所有数，每5个取一个
print(L[::5])

# 原样复制一个list
print(L[:])

# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple
print((0,1,2,3,4,5)[:3])

# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串
print(('abcdefg')[:3])
print(('abcdefg')[::2])
'''

# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法
def trim(s):
	if len(s) == 0:
		return ''
	if s[0] ==' ' or s[0] == '	':
		# 若字符串首尾有空格就递归调用trim函数本身
		s = trim(s[1:])
	elif s[-1] == ' ' or s[-1] == '	':
		s = trim(s[:-1])
	return(s)
	
print(trim('hello '))
# 测试
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')