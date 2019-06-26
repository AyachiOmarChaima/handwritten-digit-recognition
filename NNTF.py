import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import numpy as np
#from PIL import Image
import matplotlib.image as mpimg
print('chaima')

def predictionfun(filename):
    mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)  # y labels are oh-encoded
    n_input = 784  # input layer (28x28 pixels)
    n_hidden1 = 512  # 1st hidden layer
    n_hidden2 = 256  # 2nd hidden layer
    n_hidden3 = 128  # 3rd hidden layer
    n_output = 10  # output layer (0-9 digits)

    n_iterations = 6000
    batch_size = 128
    dropout = 0.5

    X = tf.placeholder("float", [None, n_input])
    Y = tf.placeholder("float", [None, n_output])
    keep_prob = tf.placeholder(tf.float32)

    weights = {
        'w1': tf.Variable(tf.truncated_normal([n_input, n_hidden1], stddev=0.1)),
        'w2': tf.Variable(tf.truncated_normal([n_hidden1, n_hidden2], stddev=0.1)),
        'w3': tf.Variable(tf.truncated_normal([n_hidden2, n_hidden3], stddev=0.1)),
        'out': tf.Variable(tf.truncated_normal([n_hidden3, n_output], stddev=0.1)),
    }

    biases = {
        'b1': tf.Variable(tf.constant(0.1, shape=[n_hidden1])),
        'b2': tf.Variable(tf.constant(0.1, shape=[n_hidden2])),
        'b3': tf.Variable(tf.constant(0.1, shape=[n_hidden3])),
        'out': tf.Variable(tf.constant(0.1, shape=[n_output]))
    }

    # Feed forward
    layer_1 = tf.add(tf.matmul(X, weights['w1']), biases['b1'])
    layer_2 = tf.add(tf.matmul(layer_1, weights['w2']), biases['b2'])
    layer_3 = tf.add(tf.matmul(layer_2, weights['w3']), biases['b3'])
    output_layer = tf.matmul(layer_3, weights['out']) + biases['out']

    cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=Y, logits=output_layer))

    train_step = tf.train.GradientDescentOptimizer(1e-4).minimize(cross_entropy)

    # tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)

    correct_pred = tf.equal(tf.argmax(output_layer, 1), tf.argmax(Y, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

    init = tf.global_variables_initializer()
    sess = tf.Session()
    sess.run(init)

    # train on mini batches
    for i in range(n_iterations):
        batch_x, batch_y = mnist.train.next_batch(batch_size)
        sess.run(train_step, feed_dict={
            X: batch_x, Y: batch_y, keep_prob: dropout
        })

    img = (mpimg.imread(filename)).reshape((28 * 28))

    prediction = sess.run(tf.argmax(output_layer, 1), feed_dict={X: [img]})

    print("Prediction for test image:", np.squeeze(prediction))
    return  np.squeeze(prediction)
