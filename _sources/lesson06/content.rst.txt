
Lesson 06: Classification by a Neural Network using Keras
*********************************************************

All content is taken from `this lesson <https://carpentries-incubator.github.io/deep-learning-intro/02-keras/index.html>`_.

* **Preface** describing the inner workings of an artificial neural network (Multi-layer perceptron)
* **Part 1** creates a neural network using the ``keras`` interface in ``tensorflow``
* **Part 2** continues to look at the training history, performs a prediction and constructs a confusion matrix from it


Check Your Learning
===================

.. admonition:: Exercise 1 / Preface

   The architecture presented in the video is often referred to as a feed-forward network. Come up with reasons why this might be the case? Compare your answers with the mentor.

.. raw:: html

   <details>
   <summary>Solution</summary>

.. code-block:: rst

   Because the data is fed in a forward fashion through the network, from inputs to outputs.

.. raw:: html

   </details>


.. admonition:: Exercise 2 / Preface

   You have created a neural network that takes ``8`` values as input. The network has two hidden (dense) layers of ``10`` neurons each. The output layer has size ``3`` and predicts 3 values. How many parameters does this network have which need to be optimized during training?

   1. 21
   2. 233
   3. 210
   4. 54

.. raw:: html

   <details>
   <summary>Solution</summary>

.. code-block:: rst

   1. (please reconsider) you have added all numbers in the exercise  
   2. (correct) layer1: 8*10 + 10 = 90, layer2: 10*10+10=110; output: 10*3+3=33
   3. (please reconsider) you omitted the bias terms
   4. (please reconsider) you have added dimensionalities instead of multiplying them to obtain the size of the matrix

.. raw:: html

   </details>

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


Exercise 2
----------

The goal of this exercise is to train a neural network to predict binary class labels on a synthetic
dataset and compare the results to those obtained with a linear classifier.

The dataset can be found :download:`here for download </_static/data/csv/lesson06/exc2_data.csv>`.
It contains 2 columns ``x`` and ``y`` and an additional ``target`` column containing the class labels
(either ``0`` or ``1``). The dataset can be visualized via
``sns.scatterplot(data=data_frame, x='x', y='y', hue='target')``.

The goal is to train a neural network, similar to Exercise 1, to predict the class labels of the dataset.

Bonus 1
~~~~~~~

Try to use a linear classifier, such as
`RidgeClassifier <https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifier.html>`_
to make predictions about the class labels. You can use the function below to visualize the predictions and ground truth labels:

.. code-block:: py

   import matplotlib.pyplot as plt
   import pandas as pd

   def plot_prediction(X, y, y_pred, *, title=''):
       if isinstance(X, pd.DataFrame):
           X = X.to_numpy()
       fig, (left, right) = plt.subplots(ncols=2, figsize=(14, 6))
       fig.suptitle(title)
       left.set(title='Ground truth labels')
       left.scatter(*X.transpose(), c=y)
       right.set(title='Predicted labels')
       right.scatter(*X.transpose(), c=y_pred)
       plt.show()

You will find that the performance of the linear classifier is not very good.
How can we still use a linear classifier and get similarly good performance as for the neural network?

.. note::

   Hint: Similar to how we scaled the input data for the wine dataset using the ``StandardScaler``, we are
   free to transform the data before feeding it to the linear classifier. A particular coordinate transformation
   might be useful to make this a linear problem.

In the light of your findings, discuss in what situations a neural network might be more useful than a more
simple method such as a linear classifier, and vice versa.
What is a particular advantage of neural networks
(think about `Feature engineering <https://en.wikipedia.org/wiki/Feature_engineering>`_)?
