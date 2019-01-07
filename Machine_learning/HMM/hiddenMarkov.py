# *_* coding:utf-8 *_*

import numpy as np


Q = [1, 2, 3]
V = ['红', '白']
A = [[0.5, 0.2, 0.3], [0.3, 0.5, 0.2], [0.2, 0.3, 0.5]]
B = [[0.5, 0.5], [0.4, 0.6], [0.7, 0.3]]
# O = ['红', '白', '红', '红', '白', '红', '白', '白']
O = ['红', '白', '红']    #习题10.1的例子
PI = [[0.2, 0.4, 0.4]]

class HiddenMarkov:
    def forward(self,Q,V,A,B,O,PI):
        N = len(Q)     # 状态数量
        M = len(O)     # 观测结果次数 = 时刻数量
        T = M          # 时刻数量
        alpha = np.zeros((M,N))    # alpha对应 任意时刻的任意状态
        for t in range(T):
            indexofO = V.index(O[t])     # 任意时刻的t对应的观测结果的索引  用于索引观测概率矩阵中结果概率位置
            for i in range(N):   # 对于任意时刻下 处于的不同状态
                B_t = B[i][indexofO]    # 该时刻该状态下 该观测结果的概率

                if t == 0:  # 初始状态
                    alpha[t][i] = PI[0][i] * B_t   # alpha 为到时刻t为止的前向概率

                else:
                    for j in range(N):
                        alpha[t][i] += alpha[t-1][j]*A[j][i]*B_t   # 迭代前向算法
        P = sum(alpha[T-1][i] for i in range(N) )

        return P

    def backward(self,Q,V,A,B,O,PI):
        N = len(Q)
        M = len(O)
        betas = np.zeros((M,N))
        betas[M-1] = 1.00
        T = M
        for t in range(M-2,-1,-1):
            indexofO = V.index(O[t+1])  #找出序列对应的索引
            for i in range(N):
                for j in range(N):
                    B_t = B[j][indexofO]
                    betas[t][i] += betas[t+1][i]*A[i][j]*B_t


        P = np.sum(PI[0][i]*B[i][V.index(O[0])]*betas[0][i] for i in range(N))
        return P

    def viterbi(self,Q,V,A,B,O,PI):
        N = len(Q)
        M = len(O)
        T = M
        deltas = np.zeros((M,N))
        psis = np.zeros((M,N))
        for t in range(T):
            indexofO = V.index(O[t])
            if t == 0:
                deltas[t] = np.dot(PI[t],B[:][indexofO])




HMM = HiddenMarkov()
p = HMM.forward(Q,V,A,B,O,PI)
p2 = HMM.backward(Q,V,A,B,O,PI)
print(p)
print(p2)