# 定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:
# 然后，在缩进块中编写函数体，函数的返回值用return语句返回。
# def my_abs(x):
#	if(x>=0):
#		return x
#	else:
#		return -x
# print(my_abs(-99))

# 如果你已经把my_abs()的函数定义保存为abstest.py文件了，
# 那么，可以在该文件的当前目录下启动Python解释器，
# 用from abstest import my_abs来导入my_abs()函数，注意abstest是文件名（不含.py扩展名）：
from abstest import my_abs
print(my_abs(-9))

# 函数可以返回多个值
# 比如在游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的坐标
import math
# import math语句表示导入math包，并允许后续代码引用math包里的sin、cos等函数。
def move(x,y,step,angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx,ny

x, y = move(100, 100, 60, math.pi / 6)
print(x,y)

# 定义函数时，需要确定函数名和参数个数
# 如果有必要，可以先对参数的数据类型做检查；
# 函数体内部可以用return随时返回函数结果；
# 函数执行完毕也没有return语句时，自动return None。
# 函数可以同时返回多个值，但其实就是一个tuple。

# 定义一个函数quadratic(a, b, c)，接收3个参数，
# 返回一元二次方程 ax^2+bx+c=0的两个解。
# 计算平方根可以调用math.sqrt()函数
import math
def quadratic(a,b,c):
	d=b*b-4*a*c
	if a==0:
		return("这不是二元一次方程")
	elif d<0:
		return("方程无解")
	else:
		x1=(-b+math.sqrt(d))/(2*a)
		x2=(-b+math.sqrt(d))/(2*a)
		return x1,x2
	a=int(input("请输入a的值："))
	b=int(input("请输入b的值："))
	c=int(input("请输入c的值："))
	x=quadratic(a,b,c)
	print(x)
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))