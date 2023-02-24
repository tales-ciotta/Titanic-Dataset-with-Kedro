"""
This is a boilerplate pipeline 'data_preprocessing'
generated using Kedro 0.18.5
"""
import pandas as pd

def prepare_data(df_train, df_test):
    
    ## df_train has null values in the columns "Cabin", "Age, "Fare"
    ## df_test has null values in the columns "Cabin", "Age, "Fare"

    ## Fill missing age values with the median bc data is slightly skewed
    ## Check "age-graphs.png" on data/08_reporting
    ## Filling missing ages in the train dataset
    df_train['Age'].fillna(df_train['Age'].median(), inplace=True)
    ## Filling missing ages in the test dataset
    df_test['Age'].fillna(df_test['Age'].median(), inplace=True)

    ## Only two "Embarked" values are missing, fill with most frequent value
    df_train["Embarked"].fillna(df_train["Embarked"].mode()[0], inplace=True)

    ## Fill missing "Fare" value with the mean for the "PClass" of the passenger
    ## Calculate mean for each "PClass"
    class_fares = df_test.groupby('Pclass')['Fare'].mean()
    ## Fill null value
    df_test['Fare'] = df_test.apply(lambda x: class_fares[x['Pclass']] if pd.isnull(x['Fare']) else x['Fare'], axis=1)

    ## Drop cabin column because we cannot to fill it with certainty.
    ## Check EDA in the notebooks directory for more information
    #Drop Cabin column

    df_train.drop('Cabin', axis=1, inplace=True)
    df_test.drop('Cabin', axis=1, inplace=True)

    ## Ticket column does not add any valuable information, since class is known and we don't have enough data to determine the position in the ship
    df_train.drop('Ticket', axis=1, inplace=True)
    df_test.drop('Ticket', axis=1, inplace=True)

    ## Passenger Id is merely an index
    df_train.drop('PassengerId', axis=1, inplace=True)
    df_test.drop('PassengerId', axis=1, inplace=True)

    return df_train, df_test