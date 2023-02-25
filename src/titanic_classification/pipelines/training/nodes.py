"""
This is a boilerplate pipeline 'training'
generated using Kedro 0.18.5
"""
"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.3
"""
import pandas as pd
from typing import Dict
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier


def train_classification_model(df_train, df_test_scaled,df_test):
    ## Separate features and target columns
    features = ['Pclass','Sex','Age','SibSp','Parch', 'Fare', 'Embarked', 'Title', 'Family_size','Family_size_discretized']
    target = ['Survived']
    X, y = df_train[features], df_train[target]
    ## Split the df_train into train and test data to fit the model
    X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                            test_size = 0.33,
                                                            random_state = 5,
                                                            stratify = y)
    ## Train the model
    classification_model = XGBClassifier()
    classification_model.fit(X_train, y_train)
    ## Calculate accuracy score                                                   
    score_value = classification_model.score(X_test, y_test)
    ## Convert accuracy score to string so it can be saved ina txt file for monitoring
    score_str = str(score_value)
    ## Predict Survival for the test.csv in data/01_raw 
    y_pred = classification_model.predict(df_test_scaled)
    ## Add back PassengerId column
    prediction = pd.concat([df_test.PassengerId, pd.DataFrame(y_pred)], axis = 'columns')

    return classification_model, score_str, prediction
