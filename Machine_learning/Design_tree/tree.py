# *_* coding:utf-8 *_*

from math import log
import operator
import graphviz

''' 计算数据集的熵-经验熵  -- 体现数据的无序程度
    创建一个数据字典 他的键值为最后一列的数值  即为分类标签 每个键值记录当前类别出现的次数
    使用类标签发生的频率计算类别出现的概率
    再通过公式 计算信息 -log_2(p_(i))  再计算信息期望 得到信息熵'''
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob*log(prob,2)
    return  shannonEnt

def createDataSet():
    dataSet = [[1,1,'yes'],
               [1,1,'yes'],
               [1,0,'no'],
               [0,1,'no'],
               [0,1,'no']]
    labels = ['no surfacing','flippers']
    return dataSet,labels

"""划分数据集 计算条件熵"""
def splitDataSet(dataSet,axis,value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

"""计算信息增益 熵-条件熵  ID3算法"""
def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1

    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueValues = set(featList)    # 利用集合的不重复性质 对特征值去重
        newEntropy = 0.0
        for value in uniqueValues:
            subDataSet = splitDataSet(dataSet,i,value)    # 对每个特征的每个值进行熵运算  就算该特征的条件熵
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob*calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature

"""类似多数表决 """
def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] +=1
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

"""创建决策树"""
def createTree(dataSet,labels):
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]     # 复制标签列表  防止递归时对列表进行改变
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet,bestFeat,value),subLabels)
    return myTree

"""使用决策树的分类函数  使用决策树"""
def classify(inputTree,featlabels,testVec):
    firstStr = list(inputTree.keys())[0]
    secondDict = inputTree[firstStr]
    featIndex = featlabels.index(firstStr)
    for key in secondDict.keys():
        if testVec[featIndex] == key:
            if type(secondDict[key]).__name__ == 'dict':
                classLabel = classify(secondDict[key],featlabels,testVec)
            else:
                classLabel = secondDict[key]
    return classLabel


# 各个函数的测试
def demo():
    myData, labels = createDataSet()
    print(myData)
    entropy = calcShannonEnt(myData)
    print(entropy)
    retdata = splitDataSet(myData, 1, 0)
    print(retdata)
    print(chooseBestFeatureToSplit(myData))

    myData[0][-1] = 'maybe'
    print(myData)
    print(calcShannonEnt(myData))

    myTree = createTree(myData, labels)
    print(myTree)

    myData, labels = createDataSet()
    result = classify(myTree, labels, [1, 0])
    print(result)

# 实际数据算法效果展示
def lenseDemo():
    fr = open("data/lenses.txt")
    lenses = [inst.strip().split('\t') for inst in fr.readlines()]
    lenLabels = ['age','perscript','astigmatic','tearRate']
    lenTree = createTree(lenses,lenLabels)
    return lenTree
if __name__ == "__main__":
    demo()
    print(lenseDemo())