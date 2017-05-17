import tensorflow as tf

# Hello World
a = tf.constant(1)
b = tf.constant(2)
print type(a)
c = a + b
print type(c)
d = a - b

sess = tf.Session()
print sess.run(c)
print sess.run(d)


# use placeholder to store inputs
a = tf.placeholder(tf.int16)
b = tf.placeholder(tf.int16)
print type(a)

add = tf.add(a, b)
add2 = a + b
mul = tf.multiply(a, b)
feed_dict = {a: 2, b: 3}
print sess.run(add, feed_dict=feed_dict)
print sess.run(add2, feed_dict=feed_dict)
print sess.run(mul, feed_dict=feed_dict)


# matrix opration
matrix1 = tf.constant([[3., 3.]])
matrix2 = tf.constant([[2.], [2.]])
product = tf.matmul(matrix2, matrix1)
print sess.run(product)

# use variable to store parameters
matrix1 = tf.Variable(tf.random_normal([3, 2]))
matrix2 = tf.Variable(tf.random_normal([2, 3]))
product = tf.matmul(matrix1, matrix2)

m1 = [[2, 5], [1, 5], [1, 4]]
m2 = [[4, 2, 1], [5, 5, 4]]

print sess.run(product, feed_dict={matrix1: m1, matrix2: m2})