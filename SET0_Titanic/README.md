1) Why did you choose this algorithm?
   This titanic problem is clearly a classification problem. And the most popular classification problems are Regression, kNN, Decision Trees, Support Vector Machine, Naive Bayes,    etc. So, we tried each of these algorithms and we got the best accuracy in the Support Vector Machine so we will go ahead with SVM.
   
2) Why you took any decision? / How you tackled problems?
   (i) There were many missing values in 'Age' and 'Cabin' sections so I filled the 'Age' section with the median of the ages of the respective classes that they are travelling in
  (ii) There was no sense in taking whole names as an input because they don't belong to any category so extreacted the titles(Mr., Mrs., etc) of the names and mapped them to             numbers
 (iii) Just like the 'title' part in second point, mapped the gender, age group, etc with the numerical values too
  (iv) Most people in each class embarked from 'S' so filled all the missing values in the 'Embarked' section with 'S'
   (v) More than half of the data didn't contain the value of cabin they belonged to so removed that column instead of assuming half the column
   

3) Results
   After applying all the classification specialist algorithms, the accuracies obtained in each of them was as follows
   kNN :- 81.82
   Decision Tree :- 80.47
   Random Forest :- 80.25
   Naive Bayes :- 79.91
   SVM :- 82.61
   So, we used SVM for finding the test_results
   ![alt text](https://github.com/bob2510/STEPIN_MiniProject_ML/blob/Main/SET0_titanic/titanic.PNG?raw=true)
