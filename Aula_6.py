import tensorflow as tf

variavel = tf.Variable(2)
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    rodar = sess.run(variavel)
    #print(rodar)

    matriz = tf.random_normal((3,5),,01)
    variavel2 = tf.Variable(matriz)
    #print(matriz)

init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    rodar = sess.run(variavel2)
    print(rodar)
