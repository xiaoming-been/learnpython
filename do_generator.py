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
# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，
# 而是一个generator函数，调用一个generator函数将返回一个generator：
'''
def fib(max):
	n,a,b=0,0,1
	while n < max:
		# print(b)
		yield b 
		a,b=b,a+b
		n=n+1
	# 使用return 'done'语句结尾生成done，不使用则生成None
	return 'done'
# print(fib(4))
# for n in fib(6):
#	print(n)

# 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
g = fib(6)
while True:
	try:
		x = next(g)
		print('g:',x)
	except StopIteration as e:
		print('Generator return value:',e.value)
		break
'''

# 定义一个generator函数，依次返回数字1，3，5
'''
def odd():
	print('step 1')
	yield(1)
	print('step 2')
	yield(3)
	print('step 3')
	yield(5)

o = odd()
next(o)
next(o)
next(o)
'''

# 杨辉三角
'''
          1
         / \
        1   1
       / \ / \
      1   2   1
     / \ / \ / \
    1   3   3   1
   / \ / \ / \ / \
  1   4   6   4   1
 / \ / \ / \ / \ / \
1   5   10  10  5   1
'''
# 把每一行看做一个list，试写一个generator，不断输出下一行的list
def triangles():
	L = [1]
	while True:
		yield L # L列表生成器
		L = [sum(i) for i in zip([0]+L, L+[0])]

n = 0
results = []
for t in triangles():
	results.append(t)
	n = n + 1
	if n == 10:
		break

for t in results:
	print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')