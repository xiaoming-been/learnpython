# while循环，只要条件满足，就不断循环，条件不满足时退出循环。
# 计算100以内所有奇数之和
sum = 0
n = 99
while n >0:
	sum = sum + n
	n = n - 2
print(sum)


sum = 0
n = 0
while(n<100):
	n = n + 1
	if(n%2==1):
		sum = sum + n
print(sum)

# 在循环中，break语句可以提前退出循环
n = 1
while n <=100:
	if n > 10: # 当n = 11时，条件满足，执行break语句
		break # break语句会结束当前循环
	print(n)
	n = n + 1
print('END')

# 在循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环。
n = 0
while n < 10:
	n = n + 1
	if(n%2==0): # 如果n是偶数，执行continue语句
		continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
	print(n)