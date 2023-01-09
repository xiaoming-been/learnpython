# 只要把一个列表生成式的[]改成()，就创建了一个generator
# L = [x * x for x in range(10)]
# print(L)

# 生成器
# generator也是可迭代对象
# g = (x * x for x in range(10))
# for n in g:
# 	print(n)
# print(g)

'''
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
'''

# 斐波拉契数列
# 除第一个和第二个数外，任意一个数都可由前两个数相加得到
# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
def fib(max):
	n,a,b=0,0,1
	while n < max:
		print(b)
		a,b=b,a+b
		n=n+1
	# 使用return 'done'语句结尾生成done，不使用则生成None
	return 'done'
print(fib(4))

