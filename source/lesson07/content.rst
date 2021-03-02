Lesson 07: CNNs
*********************

Learning Objectives
===================

- list/repeat the three ingredients to a feed forward network: input, hidden layers, output
- classify/categorize parts of a feed forward network when presented a network architecture (as from `keras.model.summary()`)
- describe a convolutional layer
- describe a max pooling layer
- calculate the output data shape of an image when transformed by a fixed convolutional layer

- interpret errors with convolutional layers
- execute a 3 layer network on the MNIST data (or similar)
- differentiate a dense layer and a convolutional layer
- experiment with values of dense layer and a convolutional layer
- select a layer type depending on the input data
- develop a 5 layer network that comprises both layer types

Content
=======

This lesson will be shared as a video.

* for learners: a stub notebook to get you started can be obtained from `the lesson03 repo <https://github.com/deeplearning540/lesson07/blob/main/lesson07.ipynb>`_.
* for instructors: the video script is available `here <https://github.com/deeplearning540/deeplearning540.github.io/blob/main/source/lesson07/script.ipynb>`_.

This lesson is based on the wonderful keras introduction by Walter de Back
- https://gitlab.com/wdeback/dl-keras-tutorial/-/blob/master/notebooks/2-convolution.ipynb
- https://gitlab.com/wdeback/dl-keras-tutorial/-/blob/master/notebooks/3-cnn-mnist.ipynb

Check your Learning
===================

.. admonition:: Exercise 1

   Fill in the blanks to produce a CNN for classification!

   .. code-block:: python

   from tensorflow import keras  
   from keras.layers import Input, Dense, Dropout, Flatten, ____2D, _________2D

   #load the data

   #define the network
   conv1 = Conv2D(16, kernel_size=(3,3), activation='______', input_shape=X_train.shape[1:])
   conv2 = ______(32, kernel_size=(3,3), activation='relu')
   mpool = MaxPooling2D(pool_size=(2,2))

   ## MLP layers
   flat = Flatten()
   dense1 = Dense(128, _____________)
   dense2 = Dense(num_classes, __________)

   #compile and train
   
   x_inputs = Input(shape=X_train.shape[1:])

   x = conv1(_______)
   x = ______(x)
   x = ______(x)

   x = flat(x)
   x = dense1(x)
   output_yhat = dense2(x)

   model = keras.Model(inputs = _______, outputs = _______, name="hello-world-cnn")

.. admonition:: Exercise 4

   For an MNIST input image, how many parameters does a `Conv2D` layer require when being defined to produce `16` feature maps as output and a `3x3` neighborhood. How many parameters does a `Dense` layer with `16` outputs have? Compute the two parameter counts!

   

Exercises
=========

* run the lesson notebook using the `fashionMNIST` dataset. Use the code below to load it. Try to reach a similar accuracy as you saw with the orginal MNIST. Does the same architecture work exactly the same with `fashionMNIST`? 

  .. code-block:: python

  from keras.datasets import fashion_mnist

  (x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()

* using the `MNIST` dataset, we saw that overfitting can be problematic. When reducing the size of the network in terms of number of parameters, the downside of this is that our network looses capacity to learn features. Cut the dense layer from `128` neurons to `64` and `32`. What do you observe with these network sizes? Compare the accuracy of the trimmed networks with a network that uses a `drop-out layer <https://keras.io/api/layers/regularization_layers/dropout/>`_ which masks `25%` of the neurons. 



