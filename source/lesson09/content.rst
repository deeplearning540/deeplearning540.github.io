Lesson 09: Networks are like onions
***********************************

Content
=======

All content is taken from `here <https://carpentries-incubator.github.io/deep-learning-intro/04-networks-are-like-onions/index.html>`_.

For instructors: the video script for both parts is available `here <https://github.com/deeplearning540/deeplearning540.github.io/blob/main/source/lesson09/script.ipynb>`_.

Check your Learning
===================

.. admonition:: Question 1

   Suppose we create a single Dense (fully connected) layer with 100 hidden units that connect to the input pixels, how many parameters does this layer have?

.. raw:: html

   <details>
   <summary>Solution</summary>

.. code-block:: python

   width, height = (32, 32)
   n_hidden_neurons = 100
   n_bias = 100
   n_input_items = width * height
   n_parameters = (n_input_items * n_hidden_neurons) + n_bias
   print(n_parameters)

   >> 307300


.. raw:: html

   </details>

.. admonition:: Question 2

   Suppose we apply a convolutional layer with ``100`` convolution kernels of size ``3 * 3 * 3`` (the last dimension applies to the rgb channels) to our images of ``32 * 32 * 3`` pixels. How many parameters do we have? Assume, for simplicity, that the kernels do not use bias terms. Compare this to the answer of the previous exercise

.. raw:: html

   <details>
   <summary>Solution</summary>

.. code-block:: rst

   We have 100 matrices with ``3 * 3 * 3 = 27`` values each so that gives ``27 * 100 = 2700`` weights. This is a magnitude of ``100`` less than the fully connected layer with 100 units! Nevertheless, as we will see, convolutional networks work very well for image data. This illustrates the expressiveness of convolutional layers.


.. raw:: html

   </details>

.. admonition:: Question 3

   What, do you think, will be the effect of adding a convolutional layer to your model (see below)? Will this model have more or fewer parameters? Try it out. Create a model that has an additional Conv2d layer with 32 filters after the last MaxPooling2D layer. Train it for 20 epochs and plot the results.

   .. code-block:: python

   inputs = keras.Input(shape=train_images.shape[1:])
   x = keras.layers.MaxPooling2D((2, 2))(x)
   x = keras.layers.Conv2D(32, (3, 3), activation='relu')(inputs)
   x = keras.layers.Conv2D(32, (3, 3), activation='relu')(x)
   x = keras.layers.MaxPooling2D((2, 2))(x)
   # Add your extra layer here
   x = keras.layers.Flatten()(x)
   x = keras.layers.Dense(32, activation='relu')(x)
   outputs = keras.layers.Dense(10)(x)

.. raw:: html

   <details>
   <summary>Solution</summary>

.. code-block:: python

   Model: "cifar_model"
    _________________________________________________________________
    Layer (type)                 Output Shape              Param #
    =================================================================
    input_4 (InputLayer)         [(None, 32, 32, 3)]       0
    _________________________________________________________________
    conv2d_6 (Conv2D)            (None, 30, 30, 32)        896
    _________________________________________________________________
    max_pooling2d_4 (MaxPooling2 (None, 15, 15, 32)        0
    _________________________________________________________________
    conv2d_7 (Conv2D)            (None, 13, 13, 32)        9248
    _________________________________________________________________
    max_pooling2d_5 (MaxPooling2 (None, 6, 6, 32)          0
    _________________________________________________________________
    conv2d_8 (Conv2D)            (None, 4, 4, 32)          9248
    _________________________________________________________________
    flatten_3 (Flatten)          (None, 512)               0
    _________________________________________________________________
    dense_6 (Dense)              (None, 32)                16416
    _________________________________________________________________
    dense_7 (Dense)              (None, 10)                330
    =================================================================
    Total params: 36,138
    Trainable params: 36,138
    Non-trainable params: 0
    _________________________________________________________________


   The number of parameters has decreased by adding this layer. We can see that the conv layer decreases the resolution from 6x6 to 4x4, as a result, the input of the Dense layer is smaller than in the previous network.


.. raw:: html

   </details>


Exercises
=========

1. Repeat the prediction of the image class using the MNIST or fashionMNIST dataset:

* `MNIST <http://yann.lecun.com/exdb/mnist/>`_, handwritten digits classification. More information can be obtained from `keras docs on MNIST <https://keras.io/api/datasets/mnist/>`_.

.. code-block:: python

   from tensorflow.keras.datasets import mnist

   (x_train, y_train), (x_test, y_test) = mnist.load_data()
   assert x_train.shape == (60000, 28, 28)
   assert x_test.shape == (10000, 28, 28)
   assert y_train.shape == (60000,)
   assert y_test.shape == (10000,)

* `fashionMNIST <https://keras.io/api/datasets/fashion_mnist/>`_, fashion item classification. 

.. code-block:: python

   from tensorflow.keras.datasets import fashion_mnist

   (x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
   assert x_train.shape == (60000, 28, 28)
   assert x_test.shape == (10000, 28, 28)
   assert y_train.shape == (60000,)
   assert y_test.shape == (10000,)

2. When completing the notebook on either FashionMNIST or MNIST, what do you observe:

- how does classification accuracy behave?
- add `precision <https://keras.io/api/metrics/classification_metrics/#precision-class>`_ and `recall <https://keras.io/api/metrics/classification_metrics/#recall-class>`_ to the list of metrics. How do either behave?
- does the same model architecture we used for cifar10 overfit on FashionMNIST or MNIST?
- is the effect of dropout layers just as severe? What happens if you increase the dropout rate?
