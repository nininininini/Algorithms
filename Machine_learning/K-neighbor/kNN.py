# *_* coding:utf-8 *_*

from numpy import *
import operator
from os import listdir
import matplotlib
import matplotlib.pyplot as plt



def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels

def classify0(inx,dataSet,labels,k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inx,(dataSetSize,1)) - dataSet
    sqdiffMat = diffMat**2
    sqDistance = sqdiffMat.sum(axis=1)
    distances = sqDistance**0.5
    sortedDistIndicies = distances.argsort()

    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)
    returnMat = zeros((numberOfLines,3))
    classLabelVector = []
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index+= 1
    return returnMat,classLabelVector

def autoNorm(dataSet):           # 对数据进行归一化处理
    minVals = dataSet.min(0)     # 获取列的最小值
    maxVals = dataSet.max(0)
    ranges = maxVals-minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals,(m,1))
    normDataSet = normDataSet/tile(ranges,(m,1))
    return normDataSet,ranges,minVals

def datingClassTest():
    hoRatio = 0.10
    datingDataMat,datingLabels = file2matrix('data/datingTestSet2.txt')
    normMat,ranges,minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
        print("the classifier came back with: %d, the real answer is: %d" %(classifierResult,datingLabels[i]))

        if (classifierResult != datingLabels[i]):
            errorCount+= 1.0
    print("the total error rate is %f" %(errorCount/float(numTestVecs)))

def classifyPerson():
    resultList = ['not at all','in small doses','in large doses']
    percentRats = float(input("percentage of time spent playing video games?"))
    ffMiles = float(input("frequent flier miles earned per year?"))
    iceCream = float(input("liters of ice cream consumed per year?"))
    datingDataMat, datingLabels = file2matrix('data/datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    inArr = array([ffMiles,percentRats,iceCream])

    classifierResult = classify0((inArr-minVals)/ranges,normMat,datingLabels,3)
    print("you will probably like this person: ",resultList[classifierResult-1])


if __name__ == "__main__":
    # group,labels = createDataSet()
    # result = classify0([0,0],group,labels,3)
    # print(result)

    datingDataMat,datingLabels = file2matrix('data/datingTestSet2.txt')
    print(datingDataMat)
    print(datingLabels[0:20])
    #
    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    # ax.scatter(datingDataMat[:,1],datingDataMat[:,2],15.0*array(datingLabels),15.0*array(datingLabels))
    # plt.show()
    normMat,ranges,minVals = autoNorm(datingDataMat)
    print(normMat,ranges,minVals)
    datingClassTest()

    classifyPerson()