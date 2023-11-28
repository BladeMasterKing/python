# 7.函数

## 定义函数
# def greet_user():
# 	print("hello")
# greet_user()

## 函数传参
# def greet_user(username):
# 	print("hello "+ username.title())
# greet_user('alice')

### 函数定义的参数为形参，调用函数的参数为实参

### 关键字实参，在调用函数时传递键值对
# def describe_pet(animal_type, animal_name):
# 	print("my animal type is "+animal_type+", it's name is "+animal_name)
# describe_pet(animal_type='hamster',animal_name='harry')

### 形参指定默认值
# def describe_pet(animal_type, animal_name='dog'):
# 	print("my animal type is "+animal_type+", it's name is "+animal_name)
# describe_pet(animal_type='harry')


## 函数返回值, 没有返回值为 None

## 列表作为参数
# def greet_users(names):
# 	for name in names:
# 		print("hello, "+name.title())
# names = ['alice', 'bob', 'david']
# greet_users(names)

## 函数修改列表
a = ['1', '2', '3']
b = []
def move(a , b):
	while a:
		item = a.pop()
		b.append(item)
# move(a, b)
# print(a)
# print(b)

## 禁止函数修改列表
### 通过切片创建副本
move(a[:], b[:])
print(a)
print(b)


## 传递任意数量的参数
def make_pizza(*toppings):
	print(toppings)
make_pizza('pepperoni')
make_pizza('mushroom','pepperoni')
### *toppongs 创建空元组，调用函数将参数封装到元组中

## 任意数量的关键字形参