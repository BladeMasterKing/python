# 1 遍历列表
# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
	# print(magician)

## 1.2 循环中执行多行
#> 通过缩进来确定循环中执行
# for magician in magicians:
	# print(magician.title()+',that was a great trick')
	# print("I cant't wait to see you next trick,"+magician.title())

## 1.3 数值列表
### range创建范围 起始数值~终止数值-1
# for value in range(1,5):
	# print(value)

### range指定步长
# for value in range(1,11,2):
	# print(value)

### 
# squares = []
# for value in range(1,11):
	# square = value ** 2
	# squares.append(square)
# print(squares)

## 1.4数值统计
# digits = [1,2,3,4,5,6,7,8,9,0]
# print(min(digits))
# print(max(digits))
# print(sum(digits))

## 1.5列表解
### 一行for循环创建列表
# squares = [value ** 2 for value in range(1,11)]
# print(squares)
# nums = [value**3 for value in range(1, 11)]
# print(nums)

# 2 切片

# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# [起始索引,元素个数]
# print(players[0:3]) 
## 没有指定索引，从第一个开始
# print(players[:4])
## 没有指定个数，到末位(包含指定索引)
# print(players[2:])
## 复数索引为距离末位距离的元素
# print(players[-2:])

## 2.2 遍历切片
# for player in players[-3:]:
	# print(player.title())

## 2.3 复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods[:]
# my_foods.append('cannoli')
# friend_foods.append('ice cream')
# print(my_foods)
# print(friend_foods)

# 直接赋值,两个列表指向同一指针，修改一个就全部修改
# friend_foods = my_foods
# print(my_foods)
# my_foods.append('cannoli')
# friend_foods.append('ice cream')
# print(my_foods)
# print(friend_foods)

# 3 元组
## 3.1定义元组
dimensions = (200, 50)
# print(dimensions[0])
# print(dimensions[1])
### 元组不允许修改
# dimensions[1] = 250

## 3.2遍历元组
# for dimension in dimensions:
	# print(dimension)

## 3.3修改元组变量
dimensions = (400, 100)
print(dimensions)
###元组数据结构更简单，需要整个生命周期的元组，定义元组






