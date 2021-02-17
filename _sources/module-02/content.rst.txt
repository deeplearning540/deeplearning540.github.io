Lesson 01: Enter Sklearn
************************

Learning Objectives
===================

* Scikit Learn is a Python library with lots of useful machine learning functions.

* Scikit Learn includes a linear regression function.

* It also includes a polynomial modelling function which is useful for modelling non-linear data.


Content
=======

This lesson is based on `Regression <https://carpentries-incubator.github.io/machine-learning-novice-sklearn/03-introducing-sklearn/index.html>`_ and will be shared as a video.


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
