import sys
sys.path.append("..")
import softmax
from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf

mnist = input_data.read_data_sets("MNIST_data/",one_hot=True,source_url="http://yann.lecun.com/exdb/mnist/")
# mnist data   100 --- 100 trainning set
batch_xs,batch_ys = mnist.train.next_batch(1000)

#MNIST data image of shape 28 * 28 = 784
length = 784

# 0 - 9 digits recognition = 10 classes
nb_classes = 10

# get W,b,cost from "../softmax.py"
W,b,cost = softmax.softmax(length,nb_classes,batch_xs,batch_ys,20000)

print(cost)
#               cost = 0.6859

X = tf.placeholder("float",[None,length])
Y = tf.placeholder("float",[None,nb_classes])
hypothesis = tf.nn.softmax(tf.matmul(X,W)+b)

# Test model
is_correct = tf.equal(tf.argmax(hypothesis,1),tf.argmax(Y,1))

# Calculate accuracy
accuracy = tf.reduce_mean(tf.cast(is_correct,tf.float32))

sess = tf.Session()

a = accuracy.eval(session=sess,feed_dict={X: mnist.test.images, Y: mnist.test.labels})

print(a)
#               a = 0.8439





