1) Why this algorithm?

   This is yet another classification problem so algoeithms like kNN, Random forest, Decision tree, ets work very good.
   
   So, I chose Random forest and Decision tree for finding the corresponding result
   
   And, the Random forest gave a very good result so I chose Random forest.
   
   
   
2) Why you took any decisions?/ How did you tackle the problem>

   Replaced the missing values of Age and Credil_limit with the median values.
   
   Instead of dealing with 6 months seperately, divided 6 months into two quarters and added the values of three months into one. Then, as the problem statement was to find the 
   
   people who will leave the bank so the ratio of customers in this quarter to customers in last quarter is very useful for obtaining a good resulrs.
   
   Just like Titanic problem, gave numerical values to some of the cateegorical variables like gender.
   
   AS there was no test data, so I splitted the data into train and test with a ratio of 7:3.
   
   
   
 3) Results
    
    The accuracy rate optained fron the random forest algorithm was around 90.76 which is quite good, given the random data provided to us.
     
    The accuracy rate obtained from the Decision Tree wwas around 86.63
     
     
4) Conclusions

    Need to remove useless data from the dataset within time  
