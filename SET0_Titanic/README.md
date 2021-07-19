1) Why did you choose this algorithm?

   This titanic problem is clearly a classification problem. And the most popular classification algorithms are Regression, kNN, Decision Trees, Support Vector Machine, Naive Bayes,    etc. So, I tried each of these algorithms and we got the best accuracy in the Support Vector Machine so went ahead with SVM.
   
2) Why you took any decision? / How you tackled problems?

   (i) There were many missing values in 'Age' and 'Cabin' sections so I filled the 'Age' section with the median of the ages of the respective classes that they are travelling        in.
   
   (ii) There was no sense in taking whole names as an input because they don't belong to any category so extreacted the titles(Mr., Mrs., etc) of the names and mapped them to          numbers.
  
   (iii) Just like the 'title' part in second point, mapped the gender, age group, etc with the numerical values too
 
   (iv) Most people in each class embarked from 'S' so filled all the missing values in the 'Embarked' section with 'S'
  
   (v) More than half of the data didn't contain the value of cabin they belonged to so removed that column instead of assuming half the column
   

3) Results

   After applying all the classification specialist algorithms, the accuracies obtained in each of them was as follows
   
   kNN :- 76.82
   
   Decision Tree :- 75.47
   
   Random Forest :- 75.25
   
   Naive Bayes :- 74.91
   
   SVM :- 77.75
   
   So, we used SVM for finding the test_results
   
   ![Kaggle Submission](https://github.com/bob2510/STEPIN_MiniProject_ML/blob/ae044769dc45afd9be7f9762e8525aca0532bc34/SET0_Titanic/titanic.PNG)
   


4) Conclusions/Learnings

   There were many things that I got to learn while doing this problem like how to handle a classification properly.
   How to preprocess our data properly and in an efficient way.
   
   How to make for missing data properly.
   
   How to use categorical data in a problem efficiently by mapping them
   
   Also, I concluded that SVM, random forest and some other algorithms are very good algorithms for a classification problem
