Deprecated Lesson 01: Diving into Regression
********************************************

Learning Objectives
===================

* Define regression as a very general concept in data science and statistics.
* describe the 3 steps in regression: data, model optimisation/fit and prediction on new data
* explain that regression provides a result with uncertainty (inductive inference)
* use MSE to quantify the uncertainty/error of a regression result
* use a least squares regression for a linear function with sklearn
* describe the PPDAC cycle of data science


Content
=======

* for learners: a stub notebook to get you started can be obtained from `the lesson01 repo <https://github.com/deeplearning540/lesson01/blob/main/lesson.ipynb>`_.
* for instructors: the video script is available `here <https://github.com/deeplearning540/deeplearning540.github.io/blob/main/source/lesson01/script.ipynb>`_.


Check your Learning
===================

The following questions serve as a help for learners to reflect on the content of the videos. Answer at least one question. At best you want to answer these questions as a team.

.. admonition:: Exercise 1

   **In the following, the order of steps was confused, please rearrange:**
   
   1. collect training data, compute accuracy, predict new data, fit training data
   2. compute accuracy, collect training data, predict new data, fit training data
   3. collect training data, fit training data, compute accuracy, predict new data
   4. collect training data, predict new data, fit training data, compute accuracy


.. admonition:: Exercise 2

   **The least squares method for an input data pair `x` and `y` derives it's name as it ...**

   1. Minimizes the sum of the product of `x*y`
   2. Minimizes the sum of the absolute difference between `y` and the predicted `y_hat`
   3. Minimizes the sum of the squared difference between `y` and the predicted `y_hat`
   4. Minimizes the sum of `y**2` and `x**2`


.. admonition:: Exercise 3

   **NaN stands for not-a-number. When loading a data set with `pandas`, NaN values occur in the loaded data because ...**
   **NaN stands for not-a-number. When loading a data set with `pandas`, NaN values occur in the loaded data because ...**

   1. Input files contain string values in a column
   2. Computational Problems occurred, like computing the square root of a negative number
   3. Data could not be parsed correctly when reading input files into memory
   4. there was no internet connection



Exercises
=========

Inspired by `the sustainability math project <http://sustainabilitymath.org/statistics-materials/>`_, perform a linear regression on the following data sets:

* Arctic Ice Data

  * Data source: http://sustainabilitymath.org/excel/ArcticIceDataMonth-R.csv 
  * Content: average Arctic Ice Extent (in millions of km^2) from 1979 to present by month.
  * Task: perform a linear regression for the months March (winter peak month) and September (summer low month) for the entire given time period (40 years)

* World Grain

  * Data source: about different grains and their production, end-of-year-stock and consumption in the US can be downloaded here:

    * :download:`Grain Production CSV </_static/data/csv/US-Grain-Production.csv>`
    * :download:`Grain End-of-year Stock CSV </_static/data/csv/US-Grain-EndOfYearStock.csv>`
    * :download:`Grain Consumption CSV </_static/data/csv/US-Grain-Consumption.csv>`

  * Content: grain production, consumption, and ending stocks, totals and by per capita.
  * Task: conduct a linear regression for grain production/consumption/stock versus time for a grain kind of your liking (60 years)
  
  
* Hourly Wage (by Race) and Gender

  * Data source: http://sustainabilitymath.org/excel/EPI-Wages-R.csv
  * Content: median and average hourly wages (in 2019 dollars) with categories of men and women by White, Black, and Hispanic.
  * Task: conduct a linear regression for wages earned versus time (47 years) for both men and women on this subset: :download:`reduced wages data set </_static/data/csv/EPI-Wages-subset.csv>`
  * Task: conduct a linear regression for wages earned versus time (47 years) for both men and women on this subset: :download:`reduced wages data set </_static/data/csv/EPI-Wages-subset.csv>`
  * At which year will equal pay be achieved? At what wage?
