Lesson 05: Neural Networks as Code
**********************************

Learning Objectives
===================

..
   **To be updated**

* A perceptron takes multiple inputs, multiplies each by a weight value and sums the weighted inputs. It then applies an activation function to the sum.
* Multiple perceptrons can be combined to form a neural network which can solve functions that aren’t linearly separable.
* We can train a whole neural network with the back propagation algorithm. keras includes an implementation of this algorithm.
* To ensure the whole data set can be used in training and testing we can train multiple times with different subsets of the data acting as training/testing data. This is called cross validation.
* To ensure the whole data set can be used in training and testing we can train multiple times with different subsets of the data acting as training/testing data. This is called cross validation.


Content
=======

This lesson will be shared as a video.

* for learners: a stub notebook to get you started can be obtained from `the lesson03 repo <https://github.com/deeplearning540/lesson04/blob/main/lesson.ipynb>`_.
* for instructors: the video script is available `here <https://github.com/deeplearning540/deeplearning540.github.io/blob/main/source/lesson04/script.ipynb>`_.

The lesson is based on the wonderful keras introduction by Walter de Back available `here <https://gitlab.com/wdeback/dl-keras-tutorial>`_.


Check your Learning
===================

The following questions serve as a help for learners to reflect on the content of the videos. Answer at least one question. At best you want to answer these questions as a team.

.. admonition:: Exercise 1

   A hidden layer of an artificial neural network consists a fixed set of parts. These are ...

   1. weights :math:`W` and a bias term :math:`\vec{b}`
   2. weights :math:`W` and a non-linear activation function :math:`F`
   3. a bias term :math:`\vec{b}` and a non-linear activation function :math:`F`
   4. weights :math:`W`, a bias term :math:`\vec{b}` and a non-linear activation function :math:`F`

.. admonition:: Exercise 2

   Unlike `scikit-learn`, `keras` is a machine learning framework that ...

   1. offers one-stop-shop prepared networks that are already published 
   2. offers building blocks to construct neural networks on CPU or GPU architectures
   3. offers an API to either wrap around backends (keras library) or represents the high-level API for `tensorflow`
   4. all of the above



Exercises
=========

* Reproduce the training with a small ANN using the iris data set including all 4 feature columns. Follow the steps below to load the data set. Compare the loss plot and the accuracy with the penguins data set: what do you see? Is the MLP overkill here too?
* Reproduce the training with a small ANN using the iris data set including all 4 feature columns. Follow the steps below to load the data set. Compare the loss plot and the accuracy with the penguins data set: what do you see? Is the MLP overkill here too?

  .. code-block:: python

  import pandas as pd
  import seaborn as sns
  
  iris = sns.load_iris()
  X = df_iris[['sepal_length','sepal_width','petal_length','petal_width']].values
  y = df_iris['species'].values


* (optional) We built an extremely simple feed-forward network model. To experiment more, load the `MNIST database of handwritten digits <http://keras.io/datasets/>`_ and see if you can beat a standard scikit-learn classifier. Unlike the Iris data set, this is a situation where the power and relative complexity of neural networks is justified. Try it yourself first, but if you get stuck, take a look at `this notebook <https://github.com/wxs/keras-mnist-tutorial/blob/master/MNIST%20in%20Keras.ipynb>`_.
