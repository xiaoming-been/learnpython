def my_abs(x):
	if not isinstance(x,(int,float)):
		# isinstance()是Python中的一个内建函数。是用来判断一个对象的变量类型。
		raise TypeError('bad operand type')
	if(x>=0):
		return x
	else:
		return -x
