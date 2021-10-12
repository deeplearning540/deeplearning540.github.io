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

Exercise 1
----------

The goal of this exercise is to fit a neural network to predict wine classes from the
`sklearn wine dataset <https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html>`_.

Please consider the following aspects when solving this exercise:

1. The dataset can be loaded via ``from sklearn.datasets import load_wine; dataset = load_wine()``.
   * Consider ``print(dataset['DESCR'])`` for more information about the dataset.
   * ``dataset['data']`` contains the features which can be used as input data.
   * ``dataset['target']`` contains the wine class labels.
2. ``pd.get_dummies`` is helpful to obtain a one-hot encoded version of class labels.
3. ``train_test_split`` should be performed as usual.
4. When inspecting the features, you will realize that they all have different number ranges.
   Hence, normalizing the data is required.
   The `StandardScaler <https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html>`_
   might be handy.
5. Regarding the network architecture, it's best to start small (in terms of number of layers and
   number of neurons) and only increase if performance is not sufficient. This helps to speed up
   the training process.
6. If you need help with the code to set up and fit the neural network, please consider the lecture notes
   about the penguin dataset; it's quite similar.
7. Finally, when you are satisfied with the training process, assess the performance of your network
   with help of the test set (confusion matrix, accuracy, etc).

Bonus 1
~~~~~~~

It's great to see the loss decreasing during training, but given a certain loss value, it's still not
easy to judge how well the model *actually* performs.
It would be nice to observe higher level metrics, such as accuracy for example.
Fortunately, the ``model.compile`` method has a parameter which allows for adding such ``metrics``.
These will eventually be stored in the fit ``history``, just like the ``'loss'``.

The goal of this exercise is to add accuracy as a metric when fitting the model.
Then the accuracy can be plotted for each epoch, similar to the loss value.
For more information, please consider the documentation of the
`model.compile method <https://www.tensorflow.org/api_docs/python/tf/keras/Model#compile>`_.

What other metrics that are useful for classification could you add?
Consider `tf.keras.metrics <https://www.tensorflow.org/api_docs/python/tf/keras/metrics>`_
for suggestions.

Bonus 2
~~~~~~~

The optimizer classes from Keras all have an impotant parameter, namely the ``learning_rate``.
The goal of this exercise is to get a feeling for how the learning rate influences the training process.
First, recall how and where the learning rate enters the training process (see the lecture slides).
Then you can try various other (extreme) learning rates, such as ``10`` or ``1e-5``. How does it
change the model performance during fitting? Discuss your findings.


