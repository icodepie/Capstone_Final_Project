# Capstone_Final_Project









## **Project Overview:**

The goal of this project was to create a machine learning model that could accurately predict a user's credit score rating into three categories, “Poor”,”Standard”, and “Good”, based on features provided by the dataset from [Kaggle](https://www.kaggle.com/datasets/parisrohan/credit-score-classification). 


## **Business Problem:**

Often people are unsure what affects credit score as it is something not formally taught. Companies such as Credit Karma have paved the way to give users insight on the different factors that can affect a person's credit score. As of today credit karma has a very basic simulator tool that can show a person how their credit score can change based on a couple different features. 



The goal is instead of providing customers with a basic tool that generates a score to provide credit karma with a tool that gives the user a credit category based on many more features so that users have a wide range of ideas on how they can improve their credit.


## **Data Understanding:**

The data comes from an old competition dataset from [Kaggel](https://www.kaggle.com/datasets/parisrohan/credit-score-classification). The data is in csv form and there are 27 features with 100,000 rows and the features used are described clearly. 


## **Data Preparation:**

With this dataset there was a good amount of cleaning to be done. All of this is included in the Data_Clean.ipynb notebook. The overall outline of the data prep process was :



* Dropping feature columns deemed unnecessary for the model
* Removing special characters
* Filtering out extreme outliers 

This left me with approximately 45,000 rows to work with.


## **Modeling :**

The modeling process consisted of doing a test train split with 20% of the data being the test set. After doing the split I created subprocess pipelines that included:



* Filling null values using sklearns simple imputer
    * For numerical type columns I used mean values since outliers were taken care of 
    * For object columns I used most frequent values
* Standard Scaling all numerical values 
* Onehot encoding all object values

The next steps I took was making pipelines that ran several different types of multiclass models.

The best performing untuned models using smote to balance the data were XGB and RFC. From this point after tuning both types of models the best performing model without extreme overfitting was XGB.


## **Evaluation :**

After all the tuning the final xgb model came out with an accuracy score of .73 with a weighted f1 score of .74. Being that the model is only a simulator of the user’s potential credit score category it performs decently well but has room for improvement. This can be achieved by feeding the model more data to train on as there was a decent sized imbalance in the categories.

 

	
