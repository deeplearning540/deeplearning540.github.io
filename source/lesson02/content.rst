Lesson 02: Enter Clustering
***************************

Learning Objectives
===================

* Understand that there are two main modes of training a ML algorithm: supervised/unsupervised training
* understand that unsupervised training does not require ground truth data labels
* identify problems that are not backed up by a model (apply ML to fit an arbitrary model)
* relate nearest neighbor clustering to an algorithm in `sklearn`
* examine a dataset and search for features that show a clear separation between samples
* argue in favor of clustering for a provided dataset, e.g. if simple decision boundaries are sufficient


Content
=======

This lesson is based on `Regression <https://carpentries-incubator.github.io/machine-learning-novice-sklearn/03-introducing-sklearn/index.html>`_ and will be shared as a video.


Check your Learning
===================

.. admonition:: Exercise 1

   You are provided a table of measurements from a weather station. Each measurements comes with values for temperature, precipation, cloud structure, date, humidity, and a quality ID. The latter tells you if the instrument was performing OK. You'd like to learn a predictor that is able to predict the quality ID for any new data coming in. This falls into ...

   1. Supervised Learning
   2. Unsupervised Learning


.. admonition:: Nearest Neighbor Clustering 

   Nearest Neighbor clustering builds a tree like structure from the dataset.

   1. Supervised Learning
   2. Unsupervised Learning



Exercises
=========

* cluster the `penguin dataset <https://github.com/allisonhorst/palmerpenguins>`_ into 3 classes when looking at bill length vs flipper length; the data is available `here <https://github.com/allisonhorst/palmerpenguins/tree/master/inst/extdata>`_

* `sklearn based datasets <https://scikit-learn.org/stable/datasets.html>`_:

  * https://scikit-learn.org/stable/datasets/toy_dataset.html#iris-plants-dataset into 3 classes when looking at petal_length vs. petal_width

  * https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html#sklearn.datasets.load_wine not sure yet which features to use
