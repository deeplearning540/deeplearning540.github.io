Lesson 02: Enter Clustering
***************************

Learning Objectives
===================

* Understand that there are two main modes of training a ML algorithm: supervised/unsupervised training
* understand that unsupervised training does not require ground truth data labels
* identify problems that are not backed up by a model (apply ML to fit an arbitrary model)
* relate nearest neighbor clustering to an algorithm in `sklearn`
* examine a data set and search for features that show a clear separation between samples
* examine a data set and search for features that show a clear separation between samples
* argue in favor of clustering for a provided data set, e.g. if simple decision boundaries are sufficient


Content
=======

The content is split in 2 parts:

* notebook to code along are available from `the lesson02 repo <https://github.com/deeplearning540/lesson02/>`_:
    * `the notebook for part1 <https://github.com/deeplearning540/lesson02/blob/main/part1.ipynb>`_ (introduction to machine learning and a first look at data).
    * `the notebook for part2 <https://github.com/deeplearning540/lesson02/blob/main/part2.ipynb>`_ (introducing and using kMeans clustering).

For instructors: the video script for both parts is available `here <https://github.com/deeplearning540/deeplearning540.github.io/blob/main/source/lesson02/script.ipynb>`_.


Check your Learning
===================

The following questions serve as a help for learners to reflect on the content of the videos. Answer at least one question. At best you want to answer these questions as a team.

.. admonition:: Exercise 1

   You are provided a table of measurements from a weather station. Each measurements comes with values for temperature, precipation, cloud structure, date, humidity, and a quality ID. The latter tells you if the instrument was performing OK. You'd like to learn an algorithm that is able to predict the quality ID (5 possible integer values from 0 to 4) for any new data coming in. This falls into ...

   1. Supervised Learning
   2. Unsupervised Learning
   3. Reinforcement Learning


.. admonition:: Exercise 2

   You are given a data set of iris flowers. The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters. Which of the following feature combinations lend themselves for clustering? See `this overview plot <https://en.wikipedia.org/wiki/Iris_flower_data_set#/media/File:Iris_data set_scatterplot.svg>`_ for help. (Multiple choices possible.)

   1. Sepal.Length versus Sepal.Width
   2. Sepal.Length versus Petal.Width
   3. Petal.Length versus Petal.Width
   4. Sepal.Width versus Petal.Width

.. admonition:: Exercise 3

   You are helping to organize a conference of more than 1000 attendants. All participants have already paid and are expecting to pick up their conference t-shirt on the first day. Your team is in shock as it discovers that t-shirt sizes have not been recorded during online registration. However, all participants were asked to provide their age, gender, body height and weight. To help out, you sit down to write a python script that predicts the t-shirt size for each participant using a clustering algorithm. You know that you can only get 7 t-shirt sizes (XS, S, M, L, XL, XXL). This falls into:

   1. Supervised Learning
   2. Unsupervised Learning
   3. Reinforcement Learning


Exercises
=========

Choose any exercise from the two categories below. Regarding the data set, consult the corresponding section.

* Cluster at least one of the synthetic data sets in the `x1` and `x2` plane. 

* Cluster the `iris plants <https://scikit-learn.org/stable/data sets/toy_data set.html#iris-plants-dataset>`_ data set. Use the columns `petal_length` vs. `petal_width`. The class label is provided as the `target` column.


Data sets
=========

* Data sets for clustering. Each of the following synthetic data sets contains several features `x1`, `x2`, ... and a `label` column which comprises (2 classes).

  * `clustering_data_00.csv <https://raw.githubusercontent.com/deeplearning540/lesson02/main/data/clustering_data_00.csv>`_
  * `clustering_data_01.csv <https://raw.githubusercontent.com/deeplearning540/lesson02/main/data/clustering_data_01.csv>`_
  * `clustering_data_02.csv <https://raw.githubusercontent.com/deeplearning540/lesson02/main/data/clustering_data_02.csv>`_
  * `clustering_data_03.csv <https://raw.githubusercontent.com/deeplearning540/lesson02/main/data/clustering_data_03.csv>`_
  * `clustering_data_04.csv <https://raw.githubusercontent.com/deeplearning540/lesson02/main/data/clustering_data_04.csv>`_
  * `clustering_data_05.csv <https://raw.githubusercontent.com/deeplearning540/lesson02/main/data/clustering_data_05.csv>`_
  * `clustering_data_06.csv <https://raw.githubusercontent.com/deeplearning540/lesson02/main/data/clustering_data_06.csv>`_
  * `clustering_data_07.csv <https://raw.githubusercontent.com/deeplearning540/lesson02/main/data/clustering_data_07.csv>`_
  * `clustering_data_08.csv <https://raw.githubusercontent.com/deeplearning540/lesson02/main/data/clustering_data_08.csv>`_
  * `clustering_data_09.csv <https://raw.githubusercontent.com/deeplearning540/lesson02/main/data/clustering_data_09.csv>`_

* `iris plants <https://scikit-learn.org/stable/data sets/toy_data set.html#iris-plants-dataset>`_ data set. Use the columns `petal_length` vs. `petal_width`. The class label is provided as the `target` column. To obtain the dataframe from this data set do the following:

.. code-block:: python

  import pandas as pd
  from sklearn.datasets import load_iris
  iris = load_iris()
  df = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                    columns= iris['feature_names'] + ['target'])

