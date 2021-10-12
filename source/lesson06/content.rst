Lesson 06: Classification by a Neural Network using Keras
*********************************************************

All content is taken from `here <https://carpentries-incubator.github.io/deep-learning-intro/02-keras/index.html>`_.

* **Preface** describing the inner workings of an artificial neural network (Multi-layer perceptron)
* **Part 1** creates a neural network using the ``keras`` interface in ``tensorflow``
* **Part 2** continues to look at the training history, performs a prediction and constructs a confusion matrix from it

Check Your Learning
===================

.. admonition:: Exercise 1 / Preface

   The architecture presented in the video is often referred to as a feed-forward network. Come up with reasons why this might be the case? Compare your answers with the mentor.
   
.. admonition:: Exercise 2 / Preface

   You have created a neural network that takes ``8`` values as input. The network has two hidden (dense) layers of ``10`` neurons each. The output layer has size ``3`` and predicts 3 values. How many parameters does this network have which need to be optimized during training?

   1. 21
   3. 233
   2. 210
   4. 54

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
