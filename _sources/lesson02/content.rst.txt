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

* for learners: a stub notebook to get you started can be obtained from `the lesson02 repo <https://github.com/deeplearning540/lesson02/blob/main/lesson.ipynb>`_.
* for instructors: the video script is available `here <https://github.com/deeplearning540/deeplearning540.github.io/blob/main/source/lesson02/script.ipynb>`_.


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

Choose any exercise from the two categories below. Regarding the dataset, consult the corresponding section.

* Cluster at least one of the synthetic datasets in the `x1` and `x2` plane. 

* Cluster the `iris plants <https://scikit-learn.org/stable/datasets/toy_dataset.html#iris-plants-dataset>`_ dataset. Use the columns `petal_length` vs. `petal_width`. The class label is provided as the `target` column.


Datasets
========

* Datasets for clustering. Each of the following synthetic datasets contains several features `x1`, `x2`, ... and a `label` column which comprises (2 classes).

  * `clustering_data_00.csv <https://github.com/deeplearning540/lesson02/blob/main/data/clustering_data_00.csv>`_
  * `clustering_data_01.csv <https://github.com/deeplearning540/lesson02/blob/main/data/clustering_data_01.csv>`_
  * `clustering_data_02.csv <https://github.com/deeplearning540/lesson02/blob/main/data/clustering_data_02.csv>`_
  * `clustering_data_03.csv <https://github.com/deeplearning540/lesson02/blob/main/data/clustering_data_03.csv>`_
  * `clustering_data_04.csv <https://github.com/deeplearning540/lesson02/blob/main/data/clustering_data_04.csv>`_
  * `clustering_data_05.csv <https://github.com/deeplearning540/lesson02/blob/main/data/clustering_data_05.csv>`_
  * `clustering_data_06.csv <https://github.com/deeplearning540/lesson02/blob/main/data/clustering_data_06.csv>`_
  * `clustering_data_07.csv <https://github.com/deeplearning540/lesson02/blob/main/data/clustering_data_07.csv>`_
  * `clustering_data_08.csv <https://github.com/deeplearning540/lesson02/blob/main/data/clustering_data_08.csv>`_
  * `clustering_data_09.csv <https://github.com/deeplearning540/lesson02/blob/main/data/clustering_data_09.csv>`_

* `iris plants <https://scikit-learn.org/stable/datasets/toy_dataset.html#iris-plants-dataset>`_ dataset. Use the columns `petal_length` vs. `petal_width`. The class label is provided as the `target` column. To obtain the dataframe from this dataset do the following:

.. code-block:: python

  import pandas as pd
  from sklearn.datasets import load_iris
  iris = load_iris()
  df = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                    columns= iris['feature_names'] + ['target'])

