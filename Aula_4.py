import tensorflow as tf

a = tf.constant(5)
b = tf.constant([3,1,5,8,6])
c = tf.constant([[2,0,4],[3,5,7]])

sess = tf.Session()
saida = sess.run(c)
sess.close()

import numpy as np

a1 = np.array(2)
b1 = np.array([3,1,5,8,6])
c1 = np.array([[2,0,4],[3,5,7]])

#print(b.shape)
const = tf.constant(4, dtype=tf.float64)
print(const)
