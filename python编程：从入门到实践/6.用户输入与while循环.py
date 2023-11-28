# 用户输入与while循环

# input()函数
# message = input("输入一个数")
# print("输入的是： " + message)

## int() 获取用户输入

# age = input("how old are you?")
# age = int(age)
# if age > 18:
	# print("你成年啦")
# else :
	# print("你未成年")

## 取模
# print(4%3)


# while循环
# current = 1
# while current <= 5:
	# print(current)
	# current += 1


## break退出循环
# while True:
	# city = input("input your city")
	# if city == 'quit':
		# break
	# else:
		# print("你的家乡是" + city)


## continue跳过循环
# current = 0
# while current < 10:
	# current += 1
	# if current % 2 == 0:
		# continue
	# print(current)

## 列表之间元素移动
# unconfirmed_users = ['alice', 'brian', 'candace']
# confirmed_users = []
# while unconfirmed_users:
# 	current_user = unconfirmed_users.pop()
# 	confirmed_users.append(current_user)

# print(unconfirmed_users)
# print(confirmed_users)

## 删除列表中指定元素
pets = ['dog', 'cat', 'dog', 'cat', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
	pets.remove('cat')
print(pets)


