# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数：

# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖

# height = 1.75
# weight = 80.5
# BMI = weight/(height*height)
# if(BMI<18.5):
#	print('过轻')
# elif(BMI>=18.5 and BMI<=25):
#	print('正常')
# elif(BMI>=25 and BMI<=28):
#	print('过重')
# elif(BMI>=28 and BMI<=32):
#	print('肥胖')
# else:
#	print('严重肥胖')

print('欢迎您使用BMI体测仪器')

# []list列表 ()tuple元组

p = ('过轻','正常','过重','肥胖','严重肥胖')
height = float(input('请输入您的身高(m)：'))
weight = float(input('请输入您的体重(kg)：'))

BMI = weight/(height**2)
print('您的BMI指数为：',BMI)

if BMI<18.5:
	print('您的评估结果是：',p[0])
elif BMI>=18.5 and BMI<=25:
	print('您的评估结果是：',p[1])
elif BMI>=25 and BMI<=28:
	print('您的评估结果是：',p[2])
elif BMI>=28 and BMI<=32:
	print('您的评估结果是：',p[3])
elif BMI>32:
	print('您的评估结果是：',p[4])

print('欢迎您下次继续使用BMI体测仪器')
