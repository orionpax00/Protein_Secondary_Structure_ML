## Analysing the relationship between secondary structures using Machine Learning

We are developing a machine learning model using Support Vector Machine algorithm which will find the similiarity between two protein structures

### Using [SVMlight](http://svmlight.joachims.org/)

> SVM<i><sup>light</sup></i> is an implementation of Support Vector Machines (SVMs) in C.

 + ***For Installation visit*** [http://svmlight.joachims.org/](http://svmlight.joachims.org/)
 + ***Data Preperation***<br> 
 We need atleast 10 similiar and 10 dissimiliar protein structure to which the similiarity of query should be checked [click here](https://orionpax00.github.io/genrating_positive_negative_data_using_blast.html)<br>
 + ***Running***<br>
 create virtualenv using virtualenv [click here](https://orionpax00.github.io/virtualenv_vs_pyenv.html)
 pip install requirements.txt
 python main.py
