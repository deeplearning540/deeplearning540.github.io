.. deeplearning540 documentation master file, created by
   sphinx-quickstart on Tue Feb 16 17:06:02 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to deeplearning in 540 minutes!
=======================================

Version |version|
*****************

The content below provides a high level overview on the content to teach.

.. Probably a bug in the deploy action (peaceiris/actions-gh-pages@v3): we
   can't use the folder name "lesson01". Must be something else, "lesson_01"
   works. "lesson01" works when building html locally, but the GH action build
   throws a 404 when accessing
   https://deeplearning540.github.io/lesson01/content.html . All other lessons,
   e.g. ".../lesson01/content.html" work just fine.

.. toctree::
   :glob:
   :maxdepth: 2
   :caption: Lesson Modules

   lesson_01/*
   lesson0*/*
   lessonb01/*



For Instructors
===============

.. toctree::
   :glob:
   :maxdepth: 2
   :caption: Extras

   extras/*

.. toctree::
   :glob:
   :maxdepth: 1
   :caption: Deprecated Material (will be removed in the next release)

   _lesson0*/*


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _Lesson 04:
