# *_* coding:utf-8 *_*

from numpy import *

array1 = random.rand(4,4)
print(array1)

# 构造一个4x4的随机数组

# Numpy数组与矩阵还是不同，虽然他们都可以处理行列表示的数据，调用mat()函数可以把数组转化成为矩阵。

randMat = mat(random.rand(4,4))
print(randMat.I)

invRandMat = randMat.I

# 除了对角线元素为1，其余元素都为0
print(invRandMat*randMat)

# 用eye命令创建单位矩阵
myeye = eye(4,4)
print(myeye)