Deprecated Lesson 08: Capstone
******************************

Learning Objectives
===================

- experiment with different methods of machine learning
- structure the project on your own or in a team
- compare your results in a team

Physics
=======

The top quark was the last being discovered. Final states with top quarks remain a very effective field to probe new or known physics. In this capstone project, you are to classify events containing a top quark or not.

The event signature of top quarks can be quite distinct from other processes. In this capstone project, 2 types of events have been isolated: 1-prong and 3-prong events. 1-prong events mark the background process that is to be discarded. 3-prong events mark the signal process and are to be found.

For this, two notebooks have been prepared that mark the basis for an analysis:

- `Top Tagging 1 notebook <https://github.com/deeplearning540/deeplearning540.github.io/blob/main/source/lesson08/TopTagging_1.ipynb>`_ allows you to conduct the analysis using the tabular features of the events only
- `Top Tagging 2 notebook <https://github.com/deeplearning540/deeplearning540.github.io/blob/main/source/lesson08/TopTagging_2.ipynb>`_ allows you to conduct the analysis using the events features as images

It is for you to decide which data set you'd like to experiment with: tabular or image like data. Please compose a classification algorithm that provides a area-under-the-curve of a ROC curve as high as possible.

More information on the project can be obtained from `the original competition repo <https://github.com/dkgithub/wuhan_DL_labs/blob/master/top-tagging/Lab_2nd_week.pdf>`_.
