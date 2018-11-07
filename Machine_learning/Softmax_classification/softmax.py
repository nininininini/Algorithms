import tensorflow as tf


def softmax(length,nb_classes,x_data,y_data,iterate):

    X = tf.placeholder("float",[None,length])
    Y = tf.placeholder("float",[None,nb_classes])

    W = tf.Variable(tf.random_normal([length,nb_classes]),name="weight")
    b = tf.Variable(tf.random_normal([nb_classes]),name="bias")


    hypothesis = tf.nn.softmax(tf.matmul(X,W)+b)

    cost = tf.reduce_mean(-tf.reduce_sum(Y*tf.log(hypothesis),axis=1))

    optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)



    with tf.Session() as sess:
        # Initialize TensorFlow variables
        sess.run(tf.global_variables_initializer())
        # Training cycle
        for step in range(iterate):
            sess.run(optimizer,feed_dict={X:x_data,Y:y_data})

        return (sess.run([W,b,cost],feed_dict={X:x_data,Y:y_data}))



# setting test values
length = 4
nb_classes =3
x_data = [[1, 2, 1, 1], [2, 1, 3, 2], [3, 1, 3, 4], [4, 1, 5, 5], [1, 7, 5, 5],[1, 2, 5, 6], [1, 6, 6, 6], [1, 7, 7, 7]]
y_data = [[0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 1, 0], [0, 1, 0], [0, 1, 0], [1, 0, 0], [1, 0, 0]]
iterate = 10



if __name__ == '__main__':

    softmax(length,nb_classes,x_data,y_data,iterate)
