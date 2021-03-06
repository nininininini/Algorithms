# _*_ coding:utf-8 _*_
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

tf.set_random_seed(1)    # set random seed

# 导入数据
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

# hyperparameters
lr = 0.01               # learning rate
training_iters = 10000  # train step 上限
batch_size = 128
n_inputs = 28           # MNIST data input (img shape: 28*28)
n_steps = 28            # time steps
n_hidden_units = 128    # neurons in hidden layers
n_classes = 10          # MNIST classes (0-9 digits)

# x,y placeholder
x = tf.placeholder(tf.float32,[None,n_steps,n_inputs])
y = tf.placeholder(tf.float32,[None,n_classes])

# 对weights,biases 初始值的定义
weights = {
    # shape (28,128)
    'in' : tf.Variable(tf.random_normal([n_inputs,n_hidden_units])),
    # shape (128,10)
    'out': tf.Variable(tf.random_normal([n_hidden_units,n_classes]))
}
biases = {
    # shape (128, )
    'in': tf.Variable(tf.constant(0.1,shape=[n_hidden_units, ])),
    # shape (10, )
    'out': tf.Variable(tf.constant(0.1,shape=[n_classes, ]))
}

def RNN(X,weights,bias):
    # 原始的 X 是三维数组，我们需要把它变成二维数组才能使用weighs的矩阵乘法
    # X ==> (128 batches * 28 steps, 28 inputs)
    X = tf.reshape(X,[-1,n_inputs])

    # X_in = W*x + b
    X_in = tf.matmul(weights['in'],X)+bias['in']

    # X_in ==> (128 batches, 28 steps, 128 hidden) 换回3维
    X_in = tf.reshape(X_in,[-1,n_steps,n_hidden_units])

    # 使用 basic LSTM Cell.
    lstm_cell = tf.contrib.rnn.BasicLSTMCell(n_hidden_units,forget_bias=1.0)
    init_state = lstm_cell.zero_state(batch_size,dtype=tf.float32) #初始化全零 state

    outputs,final_state = tf.nn.dynamic_rnn(lstm_cell,X_in,initial_state=init_state,time_major=False)
    results = tf.matmul(final_state[1], weights['out']) + biases['out']

    return results



pred = RNN(x,weights,biases)
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(pred,y))
train_op = tf.train.AdamOptimizer(lr).minimize(cost)


correct_pred = tf.equal(tf.arg_max(pred,1),tf.arg_max(y,1))
accuracy = tf.reduce_mean(tf.cast(correct_pred,tf.float32))

# init = tf.initialize_all_variables() tf 马上就要废弃这种写法
# 替换成下面的写法：
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    step = 0
    while step*batch_size < training_iters:
        batch_xs,batch_ys = mnist.train.next_match(batch_size)
        batch_xs = batch_xs.reshape([batch_size,n_steps,n_inputs])
        sess.run([train_op],feed_dict={
            x : batch_xs,
            y : batch_ys,
        })
        if (step % 20 == 0):
            print(sess.run(accuracy,feed_dict={
                x : batch_xs,
                y : batch_ys,
            }))
            step += 1
