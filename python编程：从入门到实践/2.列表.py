# 列表

bicycles = ['redline', 'trek', 'cannondale', 'specilized']
print(bicycles)

## 访问元素
print(bicycles[0])
print(bicycles[0].title())

## 添加修改元素

### 修改
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
# motorcycles[0] = 'ducati'
# print(motorcycles)

### 添加
#### 1.末位添加
# motorcycles.append('ducati')
# print(motorcycles)

#### 2.列表中插入
motorcycles.insert(1 , 'ducati')
print(motorcycles)

### 删除
#### 1.指定位置删除
# del motorcycles[0]
# print(motorcycles)

### 2.删除第一个
# pop_motors = motorcycles.pop()
# print(pop_motors)

### 3.删除指定位置
# motorcycles.pop(2)
# print(motorcycles)

### 4.根据值删除
motorcycles.remove('ducati');
print(motorcycles)
## remove函数只能删除第一个

### 排序
#### 1.永久性排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort();
# print(cars)
# cars.sort(reverse = True)
# print(cars)

#### 2.临时排序
# print(sorted(cars))
# print(cars)
# print(sorted(cars, reverse=True))

#### 3.倒序
cars.reverse()
print(cars)

#### 4.列表长度
print(len(cars))