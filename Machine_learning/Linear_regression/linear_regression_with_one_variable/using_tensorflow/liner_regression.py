import tensorflow as tf
import pandas as pd
import numpy as np

a = pd.read_table("../ex1data1.txt",sep=',')
data = np.array(a)

# x and y data
x_train = tf.convert_to_tensor(list(data[:,0]))
y_train = tf.convert_to_tensor(list(data[:,1]))
w = tf.Variable(tf.random_normal([1]),name="weight")
print(w.dtype)
b = tf.Variable(tf.random_normal([1]),name="bias")

# Our hypothesis x*w+b
hypothesis = x_train*w + b

# cost = */m  loss function
cost = tf.reduce_mean(tf.square(hypothesis-y_train))

# Minimize
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)

# Launch the graph in a session
sess = tf.Session()

# Initialize the global variable in a graph
sess.run(tf.global_variables_initializer())

# Fit the line and see some training data
for step in range(1500):
    sess.run(train)
    if step % 200 == 0:
        print(step,sess.run(cost),sess.run(w),sess.run(b))

#  get the final w b and cost
print(sess.run(cost),sess.run(w),sess.run(b))