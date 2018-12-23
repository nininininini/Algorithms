# *_* coding:utf-8*_*

import numpy as np

def loadDataSet(filename):
    dataMat = []
    fr = open(filename)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        dataMat.append(list(map(float,curLine)))
    return dataMat

def distEclud(vecA,vecB):
    return np.sqrt(np.sum(np.power(vecA-vecB,2)))

def randCent(dataSet,k):     # 随机中心点  在每个特征最大值与最小值之间选取随机数作为中心点
    n = np.shape(dataSet)[1]
    centroids = np.mat(np.zeros((k,n)))
    for j in range(n):
        minJ = min(dataSet[:, j])
        rangeJ = float( max(dataSet[:, j]) - minJ)
        centroids[:,j] = minJ + rangeJ * np.random.rand(k,1)
    return centroids


def kMeans(dataSet,k,distMeas=distEclud,createCent=randCent):
    m = np.shape(dataSet)[0]
    clusterAssment = np.mat(np.zeros((m,2)))    # 包含两列 第一列为簇的索引值  第二列存储误差值
    centroids = createCent(dataSet,k)
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):
            minDist = np.inf; minIndx = -1
            for j in range(k):
                distJI = distMeas(centroids[j,:],dataSet[i,:])
                if distJI < minDist:
                    minDist = distJI; minIndx = j
            if clusterAssment[i,0] != minIndx:
                clusterChanged = True
            clusterAssment[i,:] = minIndx,minDist**2
        print(centroids)

        for cent in range(k):
            ptsInClust = dataSet[np.nonzero(clusterAssment[:,0].A == cent)[0]]
            centroids[cent,:] = np.mean(ptsInClust,axis=0)
    return centroids,clusterAssment


def biKmeans(dataSet,k,distMeans=distEclud):
    m = np.shape(dataSet)[0]
    clusterAssment = np.mat(np.zeros((m,2)))
    centroid0 = np.mean(dataSet,axis=0).tolist()[0]
    centList = [centroid0]
    for j in range(m):
        clusterAssment[j,1] = distMeans(np.mat(centroid0),dataSet[j,:])**2
    while (len(centList) < k):
        lowestSSE = np.inf
        for i in range(len(centList)):
            ptsInCurrCluster = dataSet[np.nonzero(clusterAssment[:,0].A == i)[0],:]
            centroidMat,splitClustAss = kMeans(ptsInCurrCluster,2,distMeans)
            sseSplit = np.sum(splitClustAss[:,1])
            sseNotSplit = np.sum(clusterAssment[np.nonzero(clusterAssment[:,0].A!= i)[0],1])
            if (sseSplit + sseNotSplit) < lowestSSE:
                bestCentTosplit = i
                bestNewCents = centroidMat
                bestClustAss = splitClustAss.copy()
                lowestSSE = sseSplit + sseNotSplit
        bestClustAss[np.nonzero(bestClustAss[:,0].A == 1)[0],0] = len(centList)
        bestClustAss[np.nonzero(bestClustAss[:,0].A == 0)[0],0] = bestCentTosplit

        centList[bestCentTosplit] = bestNewCents[0,:]
        centList.append(bestNewCents[1,:])
        clusterAssment[np.nonzero(clusterAssment[:,0].A == bestCentTosplit)[0],:] = bestClustAss
    return np.mat(centList),clusterAssment

if __name__ == "__main__":
    data = loadDataSet("data/testSet.txt")
    datarr = np.mat(data)
    print(min(datarr[:,0]))
    print(max(datarr[:,0]))
    print(min(datarr[:,1]))
    print(max(datarr[:,1]))

    print(randCent(datarr,3))

