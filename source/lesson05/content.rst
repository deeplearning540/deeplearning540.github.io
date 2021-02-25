Lesson 05: Neural Networks as Code
**********************************

Learning Objectives
===================

**To be updated**

* A perceptron takes multiple inputs, multiplies each by a weight value and sums the weighted inputs. It then applies an activation function to the sum.
* Multiple perceptrons can be combined to form a neural network which can solve functions that aren’t linearly separable.
* We can train a whole neural network with the back propagation algorithm. keras includes an implementation of this algorithm.
* To ensure the whole dataset can be used in training and testing we can train multiple times with different subsets of the data acting as training/testing data. This is called cross validation.


Content
=======

This lesson will be shared as a video.

* for learners: a stub notebook to get you started can be obtained from `the lesson03 repo <https://github.com/deeplearning540/lesson04/blob/main/lesson.ipynb>`_.
* for instructors: the video script is available `here <https://github.com/deeplearning540/deeplearning540.github.io/blob/main/source/lesson04/script.ipynb>`_.

The lesson is based on the wonderful keras introduction by Walter de Back available `here <https://gitlab.com/wdeback/dl-keras-tutorial>`_.

Check your Learning
===================

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

* through OpenML https://docs.openml.org/Datasets/
   * https://sci2s.ugr.es/keel/datasets.php
   * https://archive.ics.uci.edu/ml/datasets.php?format=&task=cla&att=&area=&numAtt=&numIns=&type=&sort=nameUp&view=table

