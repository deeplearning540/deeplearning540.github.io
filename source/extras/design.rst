Lesson Design
*************

Group work organization
=======================

To provide an optimal learning experience, learners will assign themselves to
groups of about 10 persons (max) on day 1 of the course. Each group gets one
mentor assigned who will guide learners through all lessons. That way, groups
can go through the material at a pace which will fit the majority of
participants.

On day 1, lesson 01 might be taught live to all learners. After that, groups
start their individual work with lesson 02.

On each subsequent day, all groups (or each group individually) will meet in
the morning to quickly recap the last day.

If time permits, the end of the last day will provide the opportunity for a
"bring your data" type session, where all learners discuss their concrete ML
use cases among each other and with all mentors.

Lesson
======

Each lesson always follows the same structure and is expected to last about 1h.

1. Learners watch the video
2. Learners answer the `check your learning` questions as a team (at best in a hackmd/codimd document)
3. Learners dive into the exercise on their own or in small teams
4. Short Q&A with the mentor

Instructors help with show stoppers like syntax errors or comprehension questions where they can.

**Important** If your learners take longer than 1h for the module, this is not a problem. Try to concentrate on the major learning goals. If you get the feeling that 20% are bored and 60% understood it, you are good.

Audience
========

Inspired by the `Carpentries' Deciding what to teach <https://cdh.carpentries.org/deciding-what-to-teach.html#target-audience>`_:

* What is the expected educational level of your audience?

  * majority are PhD students (80-90%)
  * minority will be master students

* What type of exposure do your audience members have to the technologies you plan to teach?

  * the exposure is typically very mixed or very low, HEP has been working with root (i.e. C/C++ based data science frameworks) for a long time
  * use of python for machine learning is not wide spread
  * use of GPUs is very rare

* What types of tools do they already use?

  * ``root`` and C REPL it provides
  * (more rare) python based data analysis (``pandas``, ``matplotlib``, ...)

* What are the pain points they are currently experiencing?

  * data analysis is focused on root
  * knowledge about machine learning is present only as pieces of a puzzle
  * some students might have seen ``keras`` through ``TMVA``
  * pattern extraction is limited to the use of ``ROOT`` based tools (sometimes under the lack of deeper understanding)

* What types of data does your target audience work with? What are the commonalities in the datasets your target audience will encounter?

  * ``ROOT`` files with ``TTree`` structures that represent a big table, where each row has the same number of columns, but each column can have different width
  * learners will not be used to working with fixed size tables
  * learners will not be used to working with images


Pre-Workshop Survey
===================

All learners were offered this pre-workshop survey. Every question is a multiple choice question.

* You are provided with a Python list of integer values. The list has length 1024 and you would like to obtain all entries from index 50 to 101. How would you do this?

* You need to open 102 data files and extract an object from them. For this, you compose a small function to open a single file which requires 3 input parameters. The parameters are a file location, the name of the object to retrieve and a parameter that controls the verbosity of the function. The latter parameter has the default value `False`.

* You call a function in your code that sometimes throws a `ValueError` exception. You'd like to intercept that exception and process the traceback before re-raising the exception. How would you do that?

* You are provided a list of 512 random float values. These values range between 0 and 100. You would like to remove any entry in this list that is larger than 90 or smaller than 10.

* You are provided with a CSV file. The file has 35000 rows. The file has 45 columns. Each column is separated by the "," symbol from the other. You would like to open the file in Python, calculate the arithmetic mean, the minimum and maximum of column number 5, 12 and 39.

* A probability density function (PDF) in statistics is something very distinct from a probability mass function (PMF). What is the difference?

* You are given a dataset from experiments that you want to use for machine learning (13 columns with 25000 rows). One column is particularly useful and is encoded as real numbers in a range from -15 to 12. You would like to normalize this data so that it fits into the range of real numbers between 0 and 1. How would you do this?

* You are presented a training data set of 10000 samples. You would like to train a classifier on this datasets. However, you observe that class 0 dominates the training set at 60%, the other classes equally share 20% of the rows each. How do you prepare your training procedure?

* You are given a classifier model (neural network) by a colleague. Your peer trained it on a very large dataset. You just need it for inference. You reassure yourself that the model you loaded from disk really contains the weights by running the 'predict' function on an unseen (not used in training) validation set by your colleague. The model doesn't make the same predictions as your colleague told you. What could be the cause?

For any of the above, the learner is allowed to select one possible answer from options such as below:

1. I can do that. Give me something that understands python and I'll show you.

2. I'd need to look up the syntax in a cheatsheet or some old code and I'm good to do this.

3. I am unclear about this, I'd have to consult a colleague or a search engine to do this.

4. I am not sure what to do.
