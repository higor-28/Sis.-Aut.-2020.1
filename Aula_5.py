import tensorflow as tf

A = tf.constant([[1,2,3],[4,5,6]])
B = tf.constant([[0,0],[1,0],[0,1]])

result = tf.matmul(A,B)
print(tf.Session().run(result))
x = tf.expand_dims(x,1)
resultado2 = tf.matmul(A,x)
print(tf.Session().run(resultado2))
