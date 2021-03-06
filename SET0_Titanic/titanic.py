# -*- coding: utf-8 -*-
"""Titanic.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gLAGdmU-SaFbgp21hw7Lr6wc6-gA2gl_

Mounting Google drive
"""

from google.colab import drive
drive.mount('/content/drive')

"""Importing libraries"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline

"""### **DATA**

Importing the data and analysing it
"""

train = pd.read_csv('/content/drive/MyDrive/Titanic/train.csv')
test = pd.read_csv('/content/drive/MyDrive/Titanic/test.csv') 

train.head(10)

"""Checking for null values in both training and test data"""

train.info()

test.info()

"""NULL values in Train Dataset"""

train.isnull().sum()

"""NULL Values is Test Dataset"""

test.isnull().sum()

"""### **Bar Charts for categorical data**

Defining "bar_chart" for visualizing categorical features properly
"""

def bar_chart(feature):
    survived = train[train['Survived']==1][feature].value_counts()
    dead = train[train['Survived']==0][feature].value_counts()
    df = pd.DataFrame([survived,dead])
    df.index = ['Survived','Dead']
    df.plot(kind='bar',stacked=True, figsize=(10,5))

bar_chart('Sex')

"""From the above analysis, it is clear that Womans are more likely to survive"""

bar_chart('Pclass')

"""The passengers from Third class are more likely to die

The passengers from 1st class are more likely to survive
"""

bar_chart('SibSp')

"""A person with no siblings/spouse most likely died

A person with one or more siblings are more likely to survive
"""

bar_chart('Parch')

"""A person who boarded with a parent/children more likely survived

A person with no parent/children more likely died
"""

bar_chart('Embarked')

"""A person from C more likely survived

A person from S more likely died

A person from Q more likely died
"""

train.head()

"""### **NAME**

We need to process 'Name' column before it can be useful and it need to be done on both train as well as test data
"""

train_test_data = [train,test]
for data in train_test_data:
  data['Title'] = data['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)

train['Title'].value_counts()

test['Title'].value_counts()

"""So, Mr, Miss and Mrs are majority of titles and other titles can be put in 'others' category

Mr : 0
Miss : 1
Mrs: 2
Others: 3
"""

title_mapping = {"Mr": 0, "Miss": 1, "Mrs": 2, 
                 "Master": 3, "Dr": 3, "Rev": 3, "Col": 3, "Major": 3, "Mlle": 3,"Countess": 3,
                 "Ms": 3, "Lady": 3, "Jonkheer": 3, "Don": 3, "Dona" : 3, "Mme": 3,"Capt": 3,"Sir": 3 }
for dataset in train_test_data:
    dataset['Title'] = dataset['Title'].map(title_mapping)

train.head()

test.head()

bar_chart('Title')

"""So if your title is Mr., then you are more likely to die and more likely to survive for Ms. and Mrs.

Now, we can drop the 'Name' column from our dataset
"""

train.drop('Name', axis=1, inplace=True)
test.drop('Name', axis=1, inplace=True)

train.head()

test.head()

"""### **GENDER**

Like 'Name', we can give numerical values to other columns as well
"""

sex_mapping = {"male": 0, "female": 1}
for dataset in train_test_data:
    dataset['Sex'] = dataset['Sex'].map(sex_mapping)

bar_chart('Sex')

"""### **AGE**

Filling Missing Values

Now, the Age of some of the passengers is missing so we can fill the median age in place of the missing values
"""

train.head(10)

#fill missing age with median age for each title (Mr, Mrs, Miss, Others)
train["Age"].fillna(train.groupby("Title")["Age"].transform("median"), inplace=True)
test["Age"].fillna(test.groupby("Title")["Age"].transform("median"), inplace=True)

train.head(10)

"""Converting Numerical Age to Categorical Value for better results

child: 0
young: 1
adult: 2
mid-age: 3
senior: 4
"""

for dataset in train_test_data:
    dataset.loc[ dataset['Age'] <= 16, 'Age'] = 0
    dataset.loc[(dataset['Age'] > 16) & (dataset['Age'] <= 26), 'Age'] = 1
    dataset.loc[(dataset['Age'] > 26) & (dataset['Age'] <= 36), 'Age'] = 2
    dataset.loc[(dataset['Age'] > 36) & (dataset['Age'] <= 62), 'Age'] = 3
    dataset.loc[ dataset['Age'] > 62, 'Age'] = 4

train.head()

bar_chart('Age')

"""### **EMBARKED**

Two of the embarked values are missing in train data
"""

S_num = train[train['Embarked']=='S']['Embarked'].value_counts()
Q_num = train[train['Embarked']=='Q']['Embarked'].value_counts()
C_num = train[train['Embarked']=='C']['Embarked'].value_counts()
print(S_num, Q_num, C_num)

"""As, S has the most number of passengers and so adding two values won't affect the data"""

for dataset in train_test_data:
    dataset['Embarked'] = dataset['Embarked'].fillna('S')

"""Now, we need to change the string value of embarked into numerical value

S:0
C:1
Q:2
"""

embarked_mapping = {"S": 0, "C": 1, "Q": 2}
for dataset in train_test_data:
    dataset['Embarked'] = dataset['Embarked'].map(embarked_mapping)
train.head()

"""### **FARE**

One value of fare in the test data was missing so we need to fill it

We can assume that the same class had nearly same fares
"""

test.head()

# fill missing Fare with median fare for each Pclass
train["Fare"].fillna(train.groupby("Pclass")["Fare"].transform("median"), inplace=True)
test["Fare"].fillna(test.groupby("Pclass")["Fare"].transform("median"), inplace=True)
test.head()

train['Fare'].describe()

"""Using the above data, fares can be categorized into

0-17 : 0

17-30 : 1

30-100 : 2

100-513 : 3
"""

for dataset in train_test_data:
    dataset.loc[ dataset['Fare'] <= 17, 'Fare'] = 0
    dataset.loc[(dataset['Fare'] > 17) & (dataset['Fare'] <= 30), 'Fare'] = 1
    dataset.loc[(dataset['Fare'] > 30) & (dataset['Fare'] <= 100), 'Fare'] = 2
    dataset.loc[ dataset['Fare'] > 100, 'Fare'] = 3

train.head()

"""### **CABIN, TICKET AND PASSENGER ID**

More than half of the data do not contain the value of CABIN so we can drop it

Also, the ticket number and passenger id does not have any significance so we can drop it
"""

train.drop('Cabin', axis=1, inplace=True)
test.drop('Cabin', axis=1, inplace=True)
train.head()

train.drop('Ticket', axis=1, inplace=True)
test.drop('Ticket', axis=1, inplace=True)
train.head()

train.drop('PassengerId', axis=1, inplace=True)
train.head()

"""### **MODELLING**"""

# Importing Classifier Modules
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

import numpy as np

train.info()

"""Seperating input and expected output"""

train_data = train.drop('Survived', axis=1)
target = train['Survived']

train_data.shape, target.shape

train_data.head(10)

"""**Cross Validation (K-fold)**"""

from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
k_fold = KFold(n_splits=10, shuffle=True, random_state=0)

"""**1) kNN**"""

clf = KNeighborsClassifier(n_neighbors = 13)
scoring = 'accuracy'
score = cross_val_score(clf, train_data, target, cv=k_fold, n_jobs=1, scoring=scoring)
print(score)

round(np.mean(score)*100, 2)

"""**2) Decision Tree**"""

clf = DecisionTreeClassifier()
scoring = 'accuracy'
score = cross_val_score(clf, train_data, target, cv=k_fold, n_jobs=1, scoring=scoring)
print(score)

round(np.mean(score)*100, 2)

"""**3) Random Forest**"""

clf = RandomForestClassifier(n_estimators=13)
scoring = 'accuracy'
score = cross_val_score(clf, train_data, target, cv=k_fold, n_jobs=1, scoring=scoring)
round(np.mean(score)*100, 2)

"""**4) Naive Bayes**"""

clf = GaussianNB()
scoring = 'accuracy'
score = cross_val_score(clf, train_data, target, cv=k_fold, n_jobs=1, scoring=scoring)
round(np.mean(score)*100, 2)

"""**5) SVM**"""

clf = SVC()
scoring = 'accuracy'
score = cross_val_score(clf, train_data, target, cv=k_fold, n_jobs=1, scoring=scoring)
round(np.mean(score)*100, 2)

"""So, these are the accuracies obtained from various models

1) kNN :- 81.82

2) Decision Tree :- 80.47

3)Random Forest :- 80.25

4) Naive Bayes :- 79.91

5) SVM  :- 82.61


So, we will use SVM model for finding the test results

## **TESTING**
"""

clf = SVC()
clf.fit(train_data, target)
test_data = test.drop("PassengerId", axis=1).copy()
prediction = clf.predict(test_data)

test_data.head()

submission = pd.DataFrame({
        "PassengerId": test["PassengerId"],
        "Survived": prediction
    })
submission_csv = submission.to_csv("submission.csv",index = False, header = True)

from google.colab import files
files.download('submission.csv')