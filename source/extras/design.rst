Lesson Design
*************

Lesson
======

Each lesson always follows the same structure and is expected to last about 1h.

1. learners watch the video
2. learners answer the `check your learning` questions as a team (at best in a hackmd/codimd document)
3. learners dive into the exercise on their own 

Instructors help with show stoppers like syntax errors where they can. 

Audience
========

Inspired by the `Carpentries' Deciding what to teach <https://cdh.carpentries.org/deciding-what-to-teach.html#target-audience>_`:

* What is the expected educational level of your audience?

  * majority are PhD students (80-90%)
  * minority will be master students

* What type of exposure do your audience members have to the technologies you plan to teach?

  * the exposure is typically very mixed or very low, HEP has been working with root (i.e. C/C++ based data science frameworks) for a long time
  * use of python for machine learning is not wide spread
  * use of GPUs is very rare

* What types of tools do they already use?

  * root and C REPL it provides
  * (more rare) python based data analysis (`pandas`, `matplotlib`, ...) 

* What are the pain points they are currently experiencing?

  * data analysis is focussed on root
  * knowledge about machine learning is present only as pieces of a puzzle
  * some students might have seen `keras` through `TMVA`
  * pattern extraction is limited to the use of `ROOT` based tools (sometimes under the lack of deeper understanding)

* What types of data does your target audience work with? What are the commonalities in the datasets your target audience will encounter?

  * `ROOT` files with `TTree` structures that represent a big table, where each row has the same number of columns, but each column can have different width
  * learners will not be used to working with fixed size tables
  * learners will not be used to working with images


Pre-Workshop Survey
===================

All learners were offered this pre-workshop survey. Every question is a multiple choice question. 

* You are provided with a python list of integer values. The list has length 1024 and you would like to obtain all entries from index 50 to 101. How would you do this? 

* You need to open 102 data files and extract an object from them. For this, you compose a small function to open a single file which requires 3 input parameters. The parameters are a file location, the name of the object to retrieve and a parameter that controls the verbosity of the function. The latter parameter has the default value "False".  

* You are provided a list of 512 random float values. These values range between 0 and 100. You would like to remove any entry in this list that is larger than 90 or smaller than 10. 

* You are provided with a CSV file. The file has 35000 rows. The file has 45 columns. Each column is separated by the "," symbol from the other. You would like to open the file in python, calculate the arithmetic mean, the minimum and maximum of column number 5, 12 and 39.   

* You are provided with a CSV file. The file has 35000 rows. The file has 45 columns. Each column is separated by the "," symbol from the other. You would like to open the file in python, remove all entries where the value of column 21 is larger than 50. The values removed are to be replaced by 0.  

* You are provided with a CSV file. The file has 35000 rows. The file has 45 columns. Each column is separated by the "," symbol from the other. When you load the file and plot the histogram of column 40, you are suspicious that the floating point values are not normally distributed. But, the producer of the CSV file assures you that all columns are normally distributed. To make sure, you sit down to code a function which tests any given column if it is normally distributed. 

* You are given a dataset from experiments that you want to use for machine learning (13 columns with 25000 rows). One column is particularly useful and is encoded as real numbers in a range from `-15` to `12`. You would like to normalize this data so that it fits into the range of real numbers between `0` and `1`. How would you do this? 

* Your colleague cries out in joy at his desk. "I get 99% accuracy! I get 99% accuracy!" he says full of joy the entire office of 5 PhD students. When asked what he did differently, he says that he used the entire dataset available for supervised training. To save your colleague you kindly ask "Great. And what is the accuracy on the ... set ?" What should be filled for the blank dots? 

* You are helping to organize a conference of more than 1000 attendants. All participants have already paid and are expecting to pick up their conference t-shirt on the first day. Your team is in shock as it discovers that t-shirt sizes have not been recorded during online registration. However, all participants were asked to provide their age, gender, body height and weight. To help out, you sit down to write a python script that predicts the t-shirt size for each participant using a clustering algorithm.

For any of the above, the learner is allowed to select one possible answer from options such as below:

1. I can do that. Give me something that understands python and I'll show you.

2. I'd need to look up the syntax in a cheatsheet or some old code and I'm good to do this.

3. I am unclear about this, I'd have to consult a colleague or a search engine to do this.

4. I am not sure what to do.
