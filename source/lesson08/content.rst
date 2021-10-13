Lesson 08: Monitor the training process
***************************************

Content
=======

All content is taken from `this carpentries incubator project <https://carpentries-incubator.github.io/deep-learning-intro/03-monitor-the-model/index.html>`_.

For instructors: the video script for both parts is available `here <https://github.com/deeplearning540/deeplearning540.github.io/blob/main/source/lesson08/script.ipynb>`_.


Check your Learning
===================

.. admonition:: Exercise 1

   Overfitting describes the situation where ...

   1. a neural network produces predictions that are more precise than the training data set allows

   2. a neural network produces random predictions

   3. a neural network learns the distribution of the training and test data exactly 

   4. a neural network learns the distribution of the training data exactly and is incapable to predict the test set well

.. raw:: html

   <details>
   <summary>Solution</summary>

.. code-block:: rst

   1. no, this is describes a situation that rarely occurs but everyone aspires to (you have found a very good predictor!)
   2. no, this is called underfitting - the network is incapable of making any predictions better than random choice
   3. no, this is an unrealistic situation as the network should not be able to predict exactly the test set (unseen data)
   4. yes, overfitting describes the situation where a predictor is incapable to generalize, i.e. it predicts the training set extremely well, but almost performs random predictions on unseen data (i.e. the test set)

.. raw:: html

   </details>


.. admonition:: Exercise 2

   Overfitting counter-measures include ... (multiple answers possible)

   1. defining a baseline which corresponds to random guessing and comparing current prediction quality to this

   2. trying to obtain more data

   3. varying the size of the neural network with respect to hidden layers, number of neurons, layers types in use and other hyperparameters

   4. ignoring quality measurements on the test or validation sets completely

.. raw:: html

   <details>
   <summary>Solution</summary>

.. code-block:: rst

   1. yes, this is also often called using a dummy predictor 
   2. yes, this would potentially help as the training data would then yield more variability which can more closer to reality and help predicting the test set
   3. yes, this would help adopt the capacity of the network to the amount of training data available
   4. no, this will not help at all or change anything

.. raw:: html

   </details>


Exercises
=========

Repeat the prediction of the sunshine hours using the data from one other city, e.g. 

* ``BUDAPEST_sunshine``
* ``DE_BILT_sunshine``
* ``DRESDEN_sunshine``
* ...
* ``SONNBLICK_sunshine``
* ``STOCKHOLM_sunshine``

Do you observe a similar situation than with BASEL? To answer this, choose from any of the following aspects to guide your answer:

* How does the situation change if you include ``5`` years instead of ``3``?
* What are the model configurations that work best for you, e.g. to bring the ``RMSE`` down below ``1`` hour?
* What happens if you choose the ``sigmoid`` activation?
* What happens if you choose a larger ``batch_size``, e.g. ``64`` or ``128``?
