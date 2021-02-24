Lesson 04: Classification Performance ROCs
******************************************

Learning Objectives
===================

* Return to classification

* discuss true positive rate and true false positive rate

* explain how a cut-off value can be used to (for kmeans classification) can be used to produce a ROC curve

* demo how to construct a ROC curve

* show `plot_roc_curve` in sklearn

* discuss extremes of a ROC curve


Content
=======

This content doesn't exist yet. Clustering can be used for classification. This would pick up the knowledge from previous lesson and focus on classification accuracy and ROC curves.

https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_roc_curve_visualization_api.html#sphx-glr-auto-examples-miscellaneous-plot-roc-curve-visualization-api-py

Check your Learning
===================

.. admonition:: Exercise 1

   **TBA**

   1. ???
   2. ???
   3. ???
   4. ???


Exercises
=========

1. produce a ROC curve for the classifyer you trained in `lesson03 </source/lesson03/content.rst>`_.

2. take another NN based classifyer, e.g. `sklearn.neighbors.RadiusNeighborsClassifier` or `sklearn.neighbors.NearestCentroid` and train it

3. make predictions on the testset with it and produce a ROC 

4. combine the 2 ROC curves and discuss

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
