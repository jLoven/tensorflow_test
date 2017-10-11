#  10 October 2017
#  Jackie Loven


import tensorflow as tf

#  Each node takes zero or more tensors as inputs and produces a tensor as an output


sess = tf.Session()



#  two floating point tensors:
node1 = tf.constant(3.0, dtype=tf.float32) 
node2 = tf.constant(4.0) # also tf.float32 implicitly
node3 = tf.add(node1, node2)
print("node3:", node3)
print("sess.run(node3):", sess.run(node3))

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a + b  # + provides a shortcut for tf.add(a, b)



