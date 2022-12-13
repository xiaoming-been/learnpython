# dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度
# []list列表 ()tuple元组 {}dict字典
d = {'Michael':95,'Bob':75,'Tracy':85}
print(d['Michael'])

# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除
d.pop('Bob')
print(d)

# dict内部存放的顺序和key放入的顺序是没有关系的

# 和list比较，dict有以下几个特点：
# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。

# 而list相反：
# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。

# dict是用空间来换取时间的一种方法

# dict的key必须是不可变对象。
# 因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。
# 这个通过key计算位置的算法称为哈希算法（Hash）。
# 在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key
