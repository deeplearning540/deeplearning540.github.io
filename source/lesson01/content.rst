Lesson 01: Diving into Regression
*********************************

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

This lesson is based on `Regression <https://carpentries-incubator.github.io/machine-learning-novice-sklearn/02-regression/index.html>`_ and will be shared as a video. The video script is available `here </source/lesson01/script.ipynb>`_.


Check your Learning
===================

.. admonition:: Exercise 1

   **In the following, the order of steps was confused, please rearrange:**
   **predict new data, collect training data, fit training data, compute accuracy**

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

Exercises
=========

Inspired by `the sustainability math project <http://sustainabilitymath.org/statistics-materials/>`_, perform a linear regression on the following data sets:

* Arctic Ice Data

  * http://sustainabilitymath.org/excel/ArcticIceDataMonth-R.csv 
  * The file contains average Arctic Ice Extent from 1979 to present by month. It is excellent data for linear regression assignments.
  * March (winter peak month)
  * September (summer low month) 

* World Grain

  * http://sustainabilitymath.org/excel/Grain-R.csv (csv only contains the grain totals, the xlsx file yields all)
  * The data contains grain (barley, corn, millet, oats, rice, rye, sorghum, & wheat) production, consumption, and ending stocks, as well as totals and by per capita. Most of the production and consumption data is linear.
  * conduct a linear regression for each corn type, for production volume versus time
  * See also:

    * :download:`Grain Production </_static/data/csv/US-Grain-Production.csv>`
    * :download:`Grain End-of-year Stock </_static/data/csv/US-Grain-EndOfYearStock.csv>`
    * :download:`Grain Consumption </_static/data/csv/US-Grain-Consumption.csv>`

* Hourly Wage (by Race) and Gender

  * http://sustainabilitymath.org/excel/EPI-Wages-R.csv
  * The excel file contains a number of data sets suitable for linear regression. It contains median and average hourly wages (in 2019 dollars) with categories of men and women by White, Black, and Hispanic.
  * conduct a linear regression for wages earned versus year on this :download:`reduced wages dataset </_static/data/csv/EPI-Wages-subset.csv>`
