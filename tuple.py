# tuple有序列表：元组

# tuple和list非常类似，但是tuple一旦初始化就不能修改,比如
classmates = ('Michael', 'Bob', 'Tracy')

# classmates这个tuple不能改变，没有append(),insert()这样的方法，也不能赋值成另外的元素

# 不可变的tuple有什么意思？
# 因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple

# tuple的陷阱
# 当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来，比如
t = (1, 2)
print(t)

# 如果要定义一个空的tuple，可以写成()
t = ()
print(t)

# 定义一个只有1个元素的tuple
# Python在显示只有一个元素的tuple时，也会加一个逗号，以免你误解成数学计算意义上的括号
t = (1,)
print(t)

# “可变的”tuple
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)

# 表面上看，tuple的元素确实变了，但其实变得不是tuple的元素，而是list的元素
# tuple一开始指向的list并没有改变成别的list
# tuple所谓的“不变”是说tuple的每个元素指向永远不变
# 指向一个list，就不能指向其他对象，但指向的这个list本身是可变的

# L列表
L = [
	['Apple', 'Google', 'Microsoft'],
	['Java', 'Python', 'PHP'],
	['Adam', 'Bart', 'Lisa']
]

print('打印Apple：',L[0][0])
print('打印Python：',L[1][1])
print('打印Lisa：',L[2][2])
