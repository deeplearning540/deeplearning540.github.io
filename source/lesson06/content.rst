Lesson 06: How did we train
***************************

Learning Objectives
===================

This lesson takes references to lesson 06.

- list/repeat the three ingredients to a feed forward network: input, hidden layers, output

- describe training with mini-batched based weight-update rule

- describe a softmax layer
- motivate the loss function of categorical crossentropy (information theory vs. statistics)

- define backpropagation
- calculate example backpropagation
- generalize to full network


Content
=======

Based on discussions in `Mathematics for Machine Learning book <https://mml-book.github.io/>`_ by Deisenroth, A. Aldo Faisal, and Cheng Soon Ong.

Check your Learning
===================

.. admonition:: Exercise 1

   The advantage of mini-batched based optimisation is ...

   1. a mini-batch represents the entire dataset and hence is enough to optimize on
   2. the optimisation converges faster
   3. the optimisation can be performed in memory independent of the dataset size
   4. the optimisation will converge always in a global optimum


.. admonition:: Exercise 2

   Categorical Cross-Entropy is part of a well-known divergence in statistics. A divergence is a method to compare two probability density functions. It provides a large value if two distributions are not similar. This well-known divergance that spurrs the Categorical Cross-Entropy is ...

   1. Mean-Squared-Error divergence
   2. Negative-Log-Likelihood divergence
   3. Kullback-Leibler divergence
   4. Maximum-Mean-Discreptancy divergence


.. admonition:: Exercise 3

   The gradient that is required for gradient descent is the gradient ...

   1. of the loss function `L` with respect to the testset input data, `df/dx`, given the network parameters `theta`
   2. of the network `f` with respect to the input data, `df/dx`, given the network parameters `theta`
   3. of the network `f` with respect to the network parameters, `df/dtheta`, given the training data `x`
   4. of the loss function `L` with respect to the network parameters, `df/dtheta`, given the training data `x`


Exercises
=========

* perform the same single-neuron backpropagation as in the video but using the `sigmoid activation <https://en.wikipedia.org/wiki/Sigmoid_function>`_ function. Use `b=1`, `x=.5` and `w=3` for the inputs.

* perform the same single-neuron backpropagation as in the video but include the loss function for the two sample pairs (a) `{y=1, y_hat=1}` and (b) `{y=1, y_hat=0}`. How would your single weight be changed for (b) with respect to (a)? 


