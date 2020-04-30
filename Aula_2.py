import tensorflow as tf

frase = tf.constant('Ola mundo!!')
with tf.Session() as sess:
    rodar = sess.run(frase)
print(rodar.decode('UTF-8'))
