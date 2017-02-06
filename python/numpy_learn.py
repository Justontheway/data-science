#-*- coding:utf-8 -*-

import numpy as np


# $1. 数组创建
## 可以通过array函数对python的序列对象创建数组
## 如果传递的是多层嵌套的序列,则创建多维数组
### 一维数组
sa = np.array([1,2,3,4,5])
sb = np.array((1,2,3,4,5))
### 多维数组
ma = np.array([[1,2,3,4], [2,2,3,4]])

# $2. 数组大小
## 可以通过shape属性获取数组的大小
## 通过x.shape = m,n 可以改变数组的维度
## 当m或n为-1时,可以自动计算该维的长度
print sa.shape
print sb.shape
print ma.shape

# $3. reshape创建新数组
## 通过reshape((m,n))可以创建一个改变了尺寸的新数组,原有数组的shape保持不变
## 两数组共享数据存储区域,只是属性不同
print sa.reshape(5, 1)
print sa.reshape(5, -1)

# $4. dtype元素类型
## 通过dtype属性获取数组的元素类型
## 也可以在创建的时候用np.array([1,2,3], dtype=np.float)等制定元素类型

# $5. 常用函数
## np.arange类似range
## linspace通过指定开始值/终止值/元素个数创建一维数组
## logspace通过指定开始值/终止值/元素个数创建一维指数数组
## frombuffer/fromstring/fromfile可以从`字节序列`创建数组
## fromfunction根据传入的函数创建数组

# $6. 元素存取
## 数组元素的存取方法和python的标准方法相同
## s:t s: :t :-1 s:t:l
## 但是通过这种方式获得的数组同reshape一样和原数组共享存储区域
## 使用x[xb]布尔数组下标可以取出下标为true的元素,数据和原数组不共享存储
## 对于多维数组的存取,使用tuple来实现,各维度用逗号分隔开

# $7. 创建结构数组,类似C中的struct
## 定义类型np.dtype({'names':['name', 'age'], 'formats':['S32', 'i']})
## np.array创建数组
