# 使用isinstance()判断一个对象是否是Iterable对象(可迭代)
from collections.abc import Iterator

print(isinstance([],Iterator))
print(isinstance({},Iterator))
print(isinstance('abc',Iterator))
print(isinstance((x for x in range(10)),Iterator))
print(isinstance(100,Iterator))

for x in [1,2,3,4,5]:
	print(x)

# 获取Iterator对象：
it = iter([1,2,3,4,5])
print(it)
# 循环：
while True:
	try:
		# 获取下一个值：
		x = next(it)
		print(x)
	except StopIteration:
		# 遇到StopIteration就退出循环
		break



