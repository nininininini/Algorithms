# *_* coding:utf-8 *_*

import numpy as np
import matplotlib.pyplot as plt

def loadDataSet():
    dataMat = []
    labelMat = []
    fr = open('data/testSet.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0,float(lineArr[0]),float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat,labelMat

def sigmoid(inX):
    return 1.0/(1+np.exp(-inX))

def gradAscent(dataMatIn,classLabels):
    dataMatrix = np.mat(dataMatIn)     # dataset 100*3
    labelMat = np.mat(classLabels).transpose()  # labels 1*100   .transpose 100*1
    m,n = np.shape(dataMatrix)    # m:100   n:3
    alpha = 0.001
    maxCycles = 500               # 500次迭代
    weights = np.ones((n,1))      # 权重：3项权重
    for k in range(maxCycles):
        h = sigmoid(dataMatrix*weights)     # w^*  为  w，b 合并向量    x为[X,1]合并向量
        error = (labelMat-h)                # 运算误差值  （符号问题 求导过程因子）
        weights = weights+alpha*dataMatrix.transpose()*error # 权重更新 步长*w的梯度 损失函数为交叉熵损失函数
    return weights

def plotBestFit(wei):
    weights = wei
    try:
        weights = wei.getA()
    except:
        pass

    dataMat,labelMat = loadDataSet()
    dataArr = np.array(dataMat)
    n = np.shape(dataArr)[0]
    xcord1 = []; ycord1 = []
    xcord2 = []; ycord2 = []
    for i in range(n):
        if int(labelMat[i]) == 1:
            xcord1.append(dataArr[i,1])
            ycord1.append(dataArr[i,2])
        else:
            xcord2.append(dataArr[i,1])
            ycord2.append(dataArr[i,2])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1,ycord1,s=30,c='red',marker='s')
    ax.scatter(xcord2,ycord2,s=30,c='green')
    x1 = np.arange(-3.0,3.0,0.1)
    x2 = (-weights[0]-weights[1]*x1)/weights[2]  #分界处 0 = w1*x1 + w2*x2 +w0*x0   x0=1
    ax.plot(x1,x2)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.show()

#  单实例随机梯度下降算法
def stocGradAscent0(dataMatrix,classLabels,numIter=50):
    dataMatrix = np.array(dataMatrix)
    m,n = np.shape(dataMatrix)
    # alpha = 0.01
    weights = np.ones(n)
    for j in range(numIter):
        dataIndex = range(m)
        for i in range(m):
            alpha = 4/(1.0+j+i) + 0.01
            randIndex = int(np.random.uniform(0,len(dataIndex)))
            h = sigmoid(np.sum(dataMatrix[randIndex]*weights))
            error = classLabels[i] - h
            weights = weights + alpha*error*dataMatrix[randIndex]
    return weights

if __name__ == "__main__":
    data,labels = loadDataSet()
    # print(gradAscent(data,labels))
    print(np.mat(data).shape)
    print(np.mat(labels).shape)

    # 梯度提升算法   梯度下降 反个符号
    weights = gradAscent(data,labels)
    plotBestFit(weights)

    # 随机梯度提升
    weights = stocGradAscent0(data,labels,500)
    plotBestFit(weights)