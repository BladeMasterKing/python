# if语句
# cars = ['bmw', 'audi', 'subaru', 'toyota']
# for car in cars:
	# if car == 'bmw':
		# print(car.upper())
	# else:
		# print(car.title())

## 检查是否相等
# car = 'bmw'
# print(car == 'bmw')
# print(car != 'bmw')

## 区分大小写
# car = 'audi'
# print(car == 'Audi')
# print(car.title() == 'Audi')

## 比较数字
# age = 18
# print(age == 18)
# print(age != 18)
# print(age > 10)
# print(age < 20)
# print(age >= 18)
# print(age <= 20)


## 多条件
### and
# age_0 = 22
# age_1 = 18
# print(age_0 >= 21 and age_1 >= 21)

### or
# print(age_0 >= 21 or age_1 >= 21)

## 检查元素是否在列表中 in / not in
# cars = ['bmw', 'audi', 'subaru', 'toyota']
# print('audi' in cars)
# print('skoda' not in cars)

## 布尔表达式 True False
# game_active = True
# can_edit = False

# if语句语法
# if condition_test:
	# do something

# if-else

# if-elif-else
# age = 19
# if age>60:
	# print("退休啦")
# elif age<18 :
	# print("未成年")
# else:
	# print("加油干吧")

# requested_toppings = ['mushroom', 'green peppers', 'extra cheese']
# for requested_topping in requested_toppings:
	# if requested_topping == 'green peppers':
		# print("sorry, we are out of green peppers right now")
	# else:
		# print("adding: "+requested_topping)

## 检查列表不为空
# requested_toppings = []
# if requested_toppings:
	# for x in requested_toppings:
		# print("adding "+x)
# else:
	# print("列表为空")


avaliable = ['洋葱', '大蒜', '香菜', '大葱', '韭菜花']
request = ['大葱', '香菜']
for x in avaliable:
	if x in request:
		print("添加 "+x)
	else :
		print(x+"没有了")