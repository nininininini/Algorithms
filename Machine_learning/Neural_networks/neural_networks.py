import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data


mnist = input_data.read_data_sets("MNIST_data/",one_hot=True,source_url="http://yann.lecun.com/exdb/mnist/")

batch_xs,batch_ys = mnist.train.next_batch(50000)


# input place holders

with tf.name_scope("input") as scope:
    X = tf.placeholder(tf.float32, [None, 784],name="input_x")
    Y = tf.placeholder(tf.float32, [None, 10],name="input_y")
    keep_prob = tf.placeholder(tf.float32,name="keep_prob")
# weights & bias for nn layers


with tf.name_scope("Layer1") as scope:
    W1 = tf.Variable(tf.random_normal([784, 256]), name="weight1")
    b1 = tf.Variable(tf.random_normal([256]), name="bias1")
    L1 = tf.nn.relu(tf.matmul(X, W1) + b1)
    L1 = tf.nn.dropout(L1, keep_prob=keep_prob)

with tf.name_scope("Layer2") as scope:
    W2 = tf.Variable(tf.random_normal([256, 256]), name="weight2")
    b2 = tf.Variable(tf.random_normal([256]), name="bias")
    L2 = tf.nn.relu(tf.matmul(L1, W2) + b2)
    L2 = tf.nn.dropout(L2, keep_prob=keep_prob)

with tf.name_scope("last") as scope:
    W3 = tf.Variable(tf.random_normal([256, 10]), name="weight3")
    b3 = tf.Variable(tf.random_normal([10]), name="bias3")
    hypothesis = tf.sigmoid(tf.matmul(L2, W3) + b3)

summary = tf.summary.merge_all()

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(
   logits=hypothesis, labels=Y))

optimizer = tf.train.AdamOptimizer(learning_rate=0.1).minimize(cost)

sess = tf.Session(graph=tf.get_default_graph())
sess.run(tf.global_variables_initializer())



for setp in range(10):
   a = sess.run([hypothesis,cost,optimizer],feed_dict={X:batch_xs,Y:batch_ys,keep_prob:0.7})


print(a[1])
# writer = tf.summary.FileWriter("./improve_graph",graph=tf.get_default_graph())

s = sess.run(summary)
correct_prediction = tf.equal(tf.argmax(hypothesis, 1), tf.argmax(Y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

accur = sess.run(accuracy,feed_dict={X:mnist.test.images,Y:mnist.test.labels,keep_prob:1})

print(accur)

