import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# read the data set
a = pd.read_table("ex1data1.txt", sep=',')
data = np.array(a)
b = data[:, 0]
c = data[:, 1]
m = len(b)
n = np.ones(m).transpose()
X = np.array([n,b])
q = b.reshape(96,1).transpose()
y = c.reshape(96,1).transpose()
theta = np.zeros((1,2))
print(theta)

plt.plot(q, y,'r+')


# computeCost(theta,X,y,m)   cost = */2m
cost_1 = np.dot(theta,X) - y
cost = np.sum(cost_1**2)/(2*m)


# GradientDescent(q,theta) and compute the final cost of the model
iterations = 1500
alpha = 0.01
for iterat in range(1,iterations):
    cost_1 =np.dot(theta, X) - y
    value = alpha*np.dot(X,cost_1.transpose())/m
    cost = np.sum(cost_1 ** 2) / (2 * m)
    theta = theta - value.transpose()

# get the value of w and b
b = theta[0][0]
w = theta[0][1]
cost = cost

# plot the fitting line
plt.plot(q[0],w*q[0]+b,"r-")
plt.show()

print(w,b,cost)
