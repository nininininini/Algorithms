# *_* coding:utf-8 *_*

import numpy as np
import re

def loadDataSet():
    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0,1,0,1,0,1]    #1 is abusive, 0 not   1代表侮辱性文字 0代表正常
    return postingList , classVec

def createVocabList(datasert):
    vocabSet = set([])
    for document in datasert:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)

# 词集模型
def setOfWords2Vec(vocablist,inputSet):
    returnVec = [0]*len(vocablist)
    for word in inputSet:
        if word in vocablist:
            returnVec[vocablist.index(word)] = 1
        else:
            print("the word:%s is not in my Vocabulary!" %word)
    return returnVec

# 词袋模型
def bagOfWords2Vec(vocablist,inputSet):
    returnVec = [0]*len(vocablist)
    for word in inputSet:
        if word in vocablist:
            returnVec[vocablist.index(word)] += 1
        else:
            print("the word:%s is not in my Vocabulary" %word)
    return returnVec

# 朴素贝叶斯 核心计算代码  计算概率
def trainNB0(trainMatrix,trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCategory)/float(numTrainDocs)
    p0Num = np.ones(numWords)    # 防止概率为0 导致计算结果为0  初始化为1  为每个取值添加一个频数
    p1Num = np.ones(numWords)
    p0Denmo = 2.0
    p1Denmo = 2.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denmo += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denmo += sum(trainMatrix[i])
    p0Vect = np.log(p0Num/p0Denmo)
    p1Vect = np.log(p1Num/p1Denmo)
    return p0Vect,p1Vect,pAbusive

def classifyNB(vec2Classify,p0Vec,p1Vec,pClass1):
    p1 = sum(vec2Classify*p1Vec) + np.log(pClass1)    # 通过对数运算 把乘法运算 转换成了加法运算
    p0 = sum(vec2Classify*p0Vec) + np.log(1.0-pClass1)
    if p1>p0:
        return 1
    else:
        return 0

def testingNB():
    listOPosts,listClasses = loadDataSet()
    myVocabList = createVocabList(listOPosts)
    trainMat = []
    for postinDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocabList,postinDoc))
    p0V,p1V,pAb = trainNB0(trainMat,listClasses)
    testEntry = ['love','my','dalmation']
    thisDoc = np.array(setOfWords2Vec(myVocabList,testEntry))
    print("testEntry, classified as :",classifyNB(thisDoc,p0V,p1V,pAb))

def textParse(bigString):
    listofTokens = re.split(r'\W+',bigString)
    return [tok.lower() for tok in listofTokens if len(tok) >2]

def spamTest():
    docList = []
    classList = []
    fullTest = []
    for i in range(1,26):
        wordList = textParse(open('data/email/spam/%d.txt'%i,encoding='ISO-8859-1').read())
        docList.append(wordList)
        fullTest.extend(wordList)
        classList.append(1)

        wordList = textParse(open('data/email/ham/%d.txt'%i,encoding='ISO-8859-1').read())
        docList.append(wordList)
        fullTest.extend(wordList)
        classList.append(0)

    vocabList = createVocabList(docList)
    trainingSet = [i for i in range(50)]     # trainingSet index
    testSet = []
    for i in range(10):
        randIndex = int(np.random.uniform(0,len(trainingSet)))   # 随机选取10条数据  用作测试集
        testSet.append(trainingSet[randIndex])
        del(trainingSet[randIndex])             # 训练集中删除测试集内的数据
    trainMat = []
    trainClasses =[]
    for docIndex in trainingSet:
        trainMat.append(setOfWords2Vec(vocabList,docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V,p1V,Pspam = trainNB0(np.array(trainMat),np.array(trainClasses))
    errorCount = 0
    for docIndex in testSet:
        wordVector = setOfWords2Vec(vocabList,docList[docIndex])
        if classifyNB(np.array(wordVector),p0V,p1V,Pspam) != classList[docIndex]:
            errorCount += 1
            # print(docList[docIndex])    误判断的邮件
    print("the error rate is :", float(errorCount)/len(testSet))

if __name__ == "__main__":
    # postingList,classVec = loadDataSet()
    # print(postingList)
    # myVocabList = createVocabList(postingList)
    # print(myVocabList)
    #
    # print(setOfWords2Vec(myVocabList,postingList[0]))
    #
    # trainMat = []
    # for postinDoc in postingList:
    #     trainMat.append(setOfWords2Vec(myVocabList,postinDoc))
    #
    # p0V,p1V,pAb = trainNB0(trainMat,classVec)
    # print(p0V)
    # print(p1V)
    #
    # testingNB()
    #
    # mysent = 'bayes is a famous scientist !'
    # print(mysent.split())
    #
    # regEx = re.compile("\\W+")
    # print(re.split(regEx,mysent))

    spamTest()