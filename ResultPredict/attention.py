#!/usr/bin/python
# -*- coding:UTF-8 -*-
import tensorflow as tf
def attention(inputs,attention_size,topic_vector,time_major=False):
    if time_major:
        inputs=tf.array_ops.transpose(inputs,[1,0,2])
    batch_size=inputs.shape[0].value
    hidden_size=inputs.shape[2].value
    with tf.variable_scope("attention_W"):
        w_omega=tf.get_variable("w_omega",[attention_size,hidden_size],initializer=tf.glorot_normal_initializer())
    u_omega=tf.tensordot(topic_vector,w_omega,axes=1)
    u_omega=tf.reshape(u_omega,[batch_size,-1])
    vu=tf.matmul(inputs,tf.expand_dims(u_omega,-1))
    vu=tf.reshape(tf.squeeze(vu),[batch_size,-1])
    alphas=tf.nn.softmax(vu,name='alphas')
    output=tf.reduce_sum(inputs*tf.expand_dims(alphas,-1),1)
    return output