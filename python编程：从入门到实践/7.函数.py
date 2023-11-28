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
### 通过切片创建副本，将副本作为参数传递
# move(a[:], b[:])
# print(a)
# print(b)


## 传递任意数量的参数
# def make_pizza(*toppings):
# 	print(toppings)
# make_pizza('pepperoni')
# make_pizza('mushroom','pepperoni')
### *toppongs 创建空元组，调用函数将参数封装到元组中


## 任意数量的关键字实参
### 形参`**user_info`创建一个名为user_info的空字典，并将收到的键值对封装到字典中
# def build_profile(first, last, **user_info):
# 	profile = {}
# 	profile['first'] = first
# 	profile['last'] = last
# 	for key,value in user_info.items():
# 		profile[key] = value
# 	return profile

# user_profile = build_profile('albert', 'einstein',
# 	localtion='princeton', field='physics')
# print(user_profile)



## 导入整个模块
### 模块是`.py`文件
# import pizza
# pizza.make_pizza(16, 'pepperoni')

## 导入特定函数
### 语法 `from module_name import function_0, function_1, function_2`
# from pizza import make_pizza
# make_pizza(18, 'mushroom')

### 使用`as`给函数指定别名
#### 函数指定别名 `from module_name import function_name as fn`
#### 模块指定别名 `import module_name as mn`
# from pizza import make_pizza as mp
# mp(18, 'mushroom')

### 导入模块所有函数
#### `from pizza import *`

## 给形参指定默认值时，等号两边不要有空格：
## def function_name(parameter_0, parameter_1='default value')