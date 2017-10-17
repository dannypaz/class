"""DQN.

Uses reinforcement learning through trial and error to maximize action based on reward.
This is called Q Learning which is an agent envrioment loop.

Policy is mapping of state to action. Learns from past policies.

CNN reads in pixel data so based on just game state.
"""

from collections import deque # queue data structure. fast appends. and pops. replay memory
import random

import numpy as np
import tensorflow as tf
import pong  # Pong game


# hyper params
ACTIONS = 3  # up,down, stay
# define our learning rate
GAMMA = 0.99
# for updating our gradient or training over time
INITIAL_EPSILON = 1.0
FINAL_EPSILON = 0.05
# how many frames to anneal epsilon
EXPLORE = 500000
OBSERVE = 50000
# store our experiences, the size of it
REPLAY_MEMORY = 500000
# batch size to train on
BATCH = 100
# input image size in pixels
INPUT_SIZE = 84

# create tensorflow graph
def createGraph():

    # CNN
    # creates an empty tensor with all elements set to zero with a shape

    W_conv1 = tf.Variable(tf.zeros(shape=[2,2,4,100])) # TODO:
    b_conv1 = tf.Variable(tf.zeros(shape=[100])) # TODO:

    W_conv2 = tf.Variable(tf.zeros(shape=[2,2,100,50])) # TODO:
    b_conv2 = tf.Variable(tf.zeros(shape=[50])) # TODO:

    W_conv3 = tf.Variable(tf.zeros(shape=[2,2,50,40])) # TODO:
    b_conv3 = tf.Variable(tf.zeros(shape=[40])) # TODO:

    W_fc4 = tf.Variable(tf.zeros(shape=[3136,30])) # TODO:
    b_fc4 = tf.Variable(tf.zeros(shape=[30]) )# TODO:

    W_fc5 = tf.Variable(tf.zeros(shape=[30,20])) # TODO:
    b_fc5 = tf.Variable(tf.zeros(shape=[20])) # TODO:

    # input for pixel data
    s = tf.placeholder("float", shape=[None, INPUT_SIZE, INPUT_SIZE, 4])

    # Computes rectified linear unit activation fucntion on a 2-D convolution
    # given 4-D input and filter tensors

    conv1 = tf.nn.relu(tf.nn.conv2d(s, W_conv1,[1,1,1,1],"SAME") + b_conv1 ) # TODO:

    conv2 = tf.nn.relu(tf.nn.conv2d(conv1, W_conv2,[1,1,1,1],"SAME") + b_conv2) # TODO:


    conv3 = tf.nn.relu(tf.nn.conv2d(conv2, W_conv3,[1,1,1,1],"SAME") + b_conv3) # TODO:

    conv3_flat = tf.reshape(conv3, [-1, 7 * 7 * 64])

    fc4 = tf.nn.relu(tf.matmul(conv3_flat, W_fc4) + b_fc4)

    fc5 = tf.matmul(fc4, W_fc5) + b_fc5

    # return input and output to the network
    return s, fc5


# deep q network. feed in pixel data to graph session
def trainGraph(inp, out, sess):

    # to calculate the argmax, we multiply
    # the predicted output with a vector
    # with one value 1 and rest as 0
    argmax = tf.placeholder("float", [None, ACTIONS])
    gt = tf.placeholder("float", [None])  # ground truth

    # action
    y_pred = tf.reduce_sum(tf.matmul(argmax, out )) # TODO:

    # cost function we will reduce through backpropagation
    cost = tf.reduce_mean(tf.squared_difference(y_pred, gt)) # TODO:

    # optimization function to reduce our minimize our cost function
    train_step = tf.train.AdamOptimizer(1e-6).minimize(cost)


    # initialize our game
    game = pong.PongGame()

    # create a queue for experience replay to store policies
    D = deque()

    # intial frame
    frame = game.getPresentFrame()
    # convert rgb to gray scale for processing
    frame = cv2.cvtColor(cv2.resize(frame, (INPUT_SIZE, INPUT_SIZE)), cv2.COLOR_BGR2GRAY)
    # binary colors, black or white
    ret, frame = cv2.threshold(frame, 1, 255, cv2.THRESH_BINARY)
    # stack frames, that is our input tensor
    inp_t = np.stack((frame, frame, frame, frame), axis=2)

    # saver
    saver = tf.train.Saver()

    sess.run(tf.initialize_all_variables())

    t = 0
    epsilon = INITIAL_EPSILON

    # training time
    while(1):
        # output tensor
        out_t = out.eval(feed_dict={inp: [inp_t]})[0]
        # argmax function
        argmax_t = np.zeros([ACTIONS])

        # random action with prob epsilon
        if(random.random() <= epsilon):
            maxIndex = random.randrange(ACTIONS)
        # predicted action with prob (1 - epsilon)
        else:
            maxIndex = np.argmax(out_t)
        argmax_t[maxIndex] = 1

        if epsilon > FINAL_EPSILON:
            epsilon -= (INITIAL_EPSILON - FINAL_EPSILON) / EXPLORE

        # reward tensor if score is positive
        reward_t, frame = game.getNextFrame(argmax_t)

        # get frame pixel data
        frame = cv2.cvtColor(cv2.resize(frame, (INPUT_SIZE, INPUT_SIZE)), cv2.COLOR_BGR2GRAY)
        ret, frame = cv2.threshold(frame, 1, 255, cv2.THRESH_BINARY)
        frame = np.reshape(frame, (INPUT_SIZE, INPUT_SIZE, 1))

        # new input tensor
        inp_t1 = np.append(frame, inp_t[:, :, 0:3], axis=2)

        # add our input tensor, argmax tensor, reward and updated input tensor
        # to stack of experiences
        D.append((inp_t, argmax_t, reward_t, inp_t1))

        # if we run out of replay memory, make room
        if len(D) > REPLAY_MEMORY:
            D.popleft()

        # training iteration
        if t > OBSERVE:

            # get values from our replay memory
            minibatch = random.sample(D, BATCH)

            inp_batch = [d[0] for d in minibatch]
            argmax_batch = [d[1] for d in minibatch]
            reward_batch = [d[2] for d in minibatch]
            inp_t1_batch = [d[3] for d in minibatch]

            gt_batch = []
            out_batch = out.eval(feed_dict={inp: inp_t1_batch})

            # add values to our batch
            for i in range(0, len(minibatch)):
                gt_batch.append(reward_batch[i] + GAMMA * np.max(out_batch[i]))

            # train on that
            train_step.run(feed_dict={
                           gt: gt_batch,
                           argmax: argmax_batch,
                           inp: inp_batch
                           })

        # update our input tensor the the next frame
        inp_t = inp_t1
        t = t+1

        # print our where wer are after saving where we are
        if t % 10000 == 0:
            saver.save(sess, './' + 'pong' + '-dqn', global_step=t)

        print("TIMESTEP", t, "/ EPSILON", epsilon, "/ ACTION", maxIndex,
              "/ REWARD", reward_t, "/ Q_MAX %e" % np.max(out_t))


if __name__ == "__main__":
    # create session
    sess = tf.InteractiveSession()

    # input layer and output layer by creating graph
    inp, out = createGraph()

    # train our graph on input and output with session variables
    trainGraph(inp, out, sess)
