Lesson 01: Diving into Regression
---------------------------------

Learning Objectives
~~~~~~~~~~~~~~~~~~~

* Define regression as a very general concept in data science and statistics.
* describe the 3 steps in regression: data, model optimisation/fit and prediction on new data
* explain that regression provides a result with uncertainty (inductive inference)
* use RMS to quantify the uncertainty/error of a regression result
* implement a least squares regression for a linear function
* implement a least squares regression for a non-linear function by reusing linear modelling and a feature transform
* use linear regression on real-world data


Content
~~~~~~~

This lesson is based on `Regression <https://carpentries-incubator.github.io/machine-learning-novice-sklearn/02-regression/index.html>`_.


Check your Learning
~~~~~~~~~~~~~~~~~~~

* The least squares method for an input data pair `x` and `y` derives it's name as it ...

1. Minimizes the sum of the product of `x*y`
2. Minimizes the sum of the absolute difference between `y` and the predicted `y_hat`
3. Minimizes the sum of the squared difference between `y` and the predicted `y_hat`
4. Minimizes the sum of `y**2` and `x**2`

* 

Exercises
~~~~~~~~~

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
