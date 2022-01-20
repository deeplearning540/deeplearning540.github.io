Lesson 07: How did we train
******************************

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

**The slides** shown in the video can be obtained from `the lesson repo <https://github.com/deeplearning540/lesson06/releases/download/v2021.03.03-a/refs.tags.v2021.03.03-a-slides.pdf>`_.

This content is based on discussions in `Mathematics for Machine Learning book <https://mml-book.github.io/>`_ by Deisenroth, A. Aldo Faisal, and Cheng Soon Ong, as well as the wonderful presentation in Sebastian Raschka's `lecture L6.2 Understanding Automatic Differentiation via Computation Graphs <https://youtu.be/oY6-i2Ybin4>`_.



Check your Learning
===================

.. admonition:: Question 1

   The advantage of mini-batched based optimisation compared to online gradient descent or full data set gradient descent is ...

   1. a mini-batch represents the entire data set and hence is enough to optimize on

   2. the optimisation converges faster

   3. the optimisation can be performed in memory independent of the data set size

   4. the optimisation will converge always into a global optimum

.. raw:: html

   <details>
   <summary>Solution</summary>

.. code-block:: rst

   1. no, the optimisation is done on randomly shuffled mini-batched step-by-step 
   2. no, we have no evidence/proof for this
   3. yes, we only have to handle mini-batches in memory and hence can scale well
   4. no, we have no evidence/proof for this

.. raw:: html

   </details>


.. admonition:: Question 2

   Categorical Cross-Entropy is based in parts on a well-known divergence in statistics. A divergence is a method to compare two probability density functions. It provides a large value if two distributions are different and a small value if they are similar. This well-known divergance that builds the Categorical Cross-Entropy is ...

   1. Mean-Squared-Error divergence
   2. Negative-Log-Likelihood divergence
   3. Kullback-Leibler divergence
   4. Maximum-Mean-Discreptancy divergence

.. raw:: html

   <details>
   <summary>Solution</summary>

.. code-block:: rst

   1. no, Categorical Cross-Entropy is used for classification. The MSE is often used for regression.
   2. no, Negative-Log-Likelihood is a very broad concept 
   3. yes! 
   4. no, but this is yet another divergence or metric

.. raw:: html

   </details>


.. admonition:: Question 3

   The gradient that is required for gradient descent is the gradient ...

   1. of the loss function ``L`` with respect to the testset input data, ``dL/dx``, given the network parameters ``theta``
   2. of the network ``f`` with respect to the input data, ``df/dx``, given the network parameters ``theta``
   3. of the network ``f`` with respect to the network parameters, ``df/dtheta``, given the training data ``x``
   4. of the loss function ``L`` with respect to the network parameters, ``dL/dtheta``, given the training data ``x``

.. raw:: html

   <details>
   <summary>Solution</summary>

.. code-block:: rst

   1. no, this would lead us astray for multiple reasons: shape of ``dL/dx`` might not help to update ``theta``, changes with respect to the data do not help to optimize ``theta``
   2. no, the output of ``f`` has an arbitrary scale and no implications to solve the task (classification/regression)
   3. no, the output of ``f`` has an arbitrary scale and no implications to solve the task (classification/regression)
   4. yes! (we are interested in knowing the slope of the loss ``L`` with respect to the parameters ``theta`` so that we know how to alter it accordinly)

.. raw:: html

   </details>


Exercises
=========

* perform the same single-neuron backpropagation as in the video but using the `sigmoid activation <https://en.wikipedia.org/wiki/Sigmoid_function>`_ function. Use `b=1`, `x=.5` and `w=3` for the inputs.

* perform the same single-neuron backpropagation as in the video but include the loss function for the two sample pairs (a) `{y=1, y_hat=1}` and (b) `{y=1, y_hat=0}`. How would your single weight be changed for (b) with respect to (a)? 


