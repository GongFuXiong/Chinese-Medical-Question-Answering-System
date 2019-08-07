# coding:utf-8

import tensorflow as tf
from tensorflow.python.ops import rnn, rnn_cell
from tensorflow.contrib import rnn  			# 修改最新的
## define lstm model and reture related features


# return n outputs of the n lstm cells
def biLSTM(x, hidden_size):
	# biLSTM��
	# ���ܣ����bidirectional_lstm����
	# ������
	# 	x: [batch, height, width]   / [batch, step, embedding_size]
	# 	hidden_size: lstm���ز�ڵ����
	# �����
	# 	output: [batch, height, 2*hidden_size]  / [batch, step, 2*hidden_size]

	# input transformation
	input_x = tf.transpose(x, [1, 0, 2])
	# input_x = tf.reshape(input_x, [-1, w])
	# input_x = tf.split(0, h, input_x)
	input_x = tf.unstack(input_x)

	# define the forward and backward lstm cells
	# lstm_fw_cell = rnn_cell.BasicLSTMCell(hidden_size, forget_bias=1.0, state_is_tuple=True)
	lstm_cell = rnn.BasicLSTMCell(hidden_size, forget_bias=1.0, state_is_tuple=True)			# 修改的
	# lstm_bw_cell = rnn_cell.BasicLSTMCell(hidden_size, forget_bias=1.0, state_is_tuple=True)
	output,states = rnn.static_rnn(lstm_cell, input_x, dtype=tf.float32)

	# output transformation to the original tensor type
	output = tf.stack(output)
	output = tf.transpose(output, [1, 0, 2])
	return output

