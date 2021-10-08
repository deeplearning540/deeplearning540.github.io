Lesson 06: Classification by a Neural Network using Keras
*********************************************************

All content is taken from `here <https://carpentries-incubator.github.io/deep-learning-intro/02-keras/index.html>`_.

* Part 1 starts from the beginning and
* Part 2 continues to the end of the content

Check Your Learning
===================

.. admonition:: Exercise 1 / Part 1

   Take a look at the training and test set we created. Run the ``sklearn.metrics.train_test_split`` function multiple times with different parameters, e.g. vary the ``random_state``, switch ``stratify``. 

   - How many samples do the training and test sets have each time?
   - Are the classes in the training set well balanced compared to the output of ``penguin_features.species_.value_counts()``?

.. admonition:: Exercise 2 / Part 1

   With the code snippets in the video, we defined a keras model with 1 hidden layer with 10 neurons and an output layer with 3 neurons.

   - recap: How many parameters does the resulting model have?
   - What happens to the number of parameters if we increase or decrease the number of neurons in the hidden layer?
   - Ask your neighbor to tell you a choice of layer number and layer width. Predict how many parameters will be needed. Then implement this and check!


Exercises
=========

TBA
