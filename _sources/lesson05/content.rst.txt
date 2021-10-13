Lesson 05: Introduction Deep Learning
*************************************

All content is taken from `here <https://carpentries-incubator.github.io/deep-learning-intro/01-introduction/index.html>`_.

This material revolves mostly around the capabilities and inabilities of Deep Learning.

What is AI?
===========

.. image:: https://carpentries-incubator.github.io/deep-learning-intro/fig/AI_ML_DL_bubble_square_draft.png

No More Feature Engineering
===========================


.. image:: https://carpentries-incubator.github.io/deep-learning-intro/fig/ML_DL_draft.png


The Deep Learning Workflow
==========================

.. image:: graphviz/pipeline.png


Exercises
=========

.. admonition:: Exercise 1

   Which of the following would you apply Deep Learning to?

   1. Recognising whether or not a picture contains a bird.
   2. Calculating the median and interquartile range of a dataset.
   3. Identifying MRI images of a rare disease when only one or two example images available for training.
   4. Identifying people in pictures after being trained only on cats and dogs.
   5. Translating English into French.

.. raw:: html

   <details>
   <summary>Solution</summary>

.. code-block:: rst

   1. yes, a classification problem using images as input
   2. no, even though it is a regression problem, you'd need tons of training data and still be off by quite a bit
   3. no, not enough training data available
   4. no, likely a deep learning model will not be able to do that
   5. yes, tons of training data available from translated books or wikipedia articles

.. raw:: html

   </details>

.. admonition:: Exercise 2

   Think about a problem you’d like to use Deep Learning to solve.

   * What do you want a Deep Learning system to be able to predict (or tell you)?
   * What data inputs and outputs will you need?
   * Do you think you’ll need to train the network or will a pre-trained network be suitable?
   * What data do you have to train with? What preparation will your data need? Consider both the data you are going to predict/classify from and the data you’ll use to train the network.

   Discuss your answers with the group or the person next to you.
