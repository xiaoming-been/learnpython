# 定义一个计算x的平方的函数：
'''
def power(x):
	return x * x
print(power(5))
print(power(15))
'''

# 定义一个计算x的n次方的函数：
'''
def power(x, n=2):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s
print(power(5,2))
print(power(5,3))
'''
# 小学生注册函数
'''
def enroll(name, gender, age=6, city='Beijing'):
	print('name:',name)
	print('gender:',gender)
	print('age:', age)
	print('city:', city)

print(enroll('Sarach','F'))
'''

# 默认参数必须指向不变对象
'''
def add_end(L=None):
	if L is None:
		L = []
	L.append('END')
	return L
print(add_end())
print(add_end())
'''

# 给定一组数字a，b，c……，请计算a*a + b*b + c*c + ……
# Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum
# print(calc([1, 2, 3]))
print(calc(1,2,3))
