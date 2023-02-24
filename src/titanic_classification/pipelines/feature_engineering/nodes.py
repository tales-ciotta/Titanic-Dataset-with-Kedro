"""
This is a boilerplate pipeline 'feature_engineering'
generated using Kedro 0.18.5
"""

import pandas as pd
from typing import Dict
from sklearn.preprocessing import OrdinalEncoder, StandardScaler

def create_features(df_train, df_test):

    ## The names have titles attached
    ## From the information collected in the EDA, creating a list of rare titles
    ## Extract titles from 'Name' column

    df_train['Title'] = df_train['Name'].apply(lambda x: x.split(',')[1].split('.')[0].strip())
    df_test['Title'] = df_test['Name'].apply(lambda x: x.split(',')[1].split('.')[0].strip())

    rare_titles = ['Dr', 'Rev', 'Major', 'Col', 'Capt', 'Jonkheer', 'Sir', 'Lady', 'Don', 'Dona', 'the Countess']
    ## Replace rare_titles with a unified title caled "Rare" for both train and test dataset
    df_train['Title'] = df_train['Title'].replace(rare_titles, 'Rare')
    df_test['Title'] = df_test['Title'].replace(rare_titles, 'Rare')

    ## Group rare women's titles for train and test datasets
    df_train['Title'] = df_train['Title'].replace(['Mlle', 'Ms'], 'Miss')
    df_train['Title'] = df_train['Title'].replace('Mme', 'Mrs')
    df_test['Title'] = df_test['Title'].replace(['Ms'], 'Miss')

    ## The "Name" column won't be useful after "Title" was created using it
    ## Drop "Name" to simplify the encoding process in a later node
    df_train = df_train.drop('Name', axis=1)
    df_test = df_test.drop('Name', axis=1)

    ## Parch = number of parents/children aboard
    ## SibSp = Number of siblings/spouses aboard
    ## With this data we create a feature of the size of the family aboard

    ## Get total number of family members
    df_train['Family_size'] = df_train['SibSp'] + df_train['Parch'] + 1
    df_test['Family_size'] = df_test['SibSp'] + df_test['Parch'] + 1

    ## Discretize family size for the train dataset
    df_train.loc[df_train['Family_size'] == 1, 'Family_size_discretized'] = 'Alone'
    df_train.loc[df_train['Family_size'].between(2, 4), 'Family_size_discretized'] = 'Small'
    df_train.loc[df_train['Family_size'] >= 5, 'Family_size_discretized'] = 'Large'

    ## Discretize family size for the test dataset
    df_test.loc[df_test['Family_size'] == 1, 'Family_size_discretized'] = 'Alone'
    df_test.loc[df_test['Family_size'].between(2, 4), 'Family_size_discretized'] = 'Small'
    df_test.loc[df_test['Family_size'] >= 5, 'Family_size_discretized'] = 'Large'


    return df_train, df_test

def ordinal_encoder_str_columns(df_train_encoded, df_test_encoded):
    """This method encode all str columns in df
    Str columns: 
        'Sex', 'Embarked', 'Title', 
        'Family_size_discretized'
        
    Args:
        df_train_encoded (pd.DataFrame): df_train with str columns
        df_tesst_enriched (pd.DataFrame): df_test with str columns
        
    Returns:
        Dict[pd.DataFrame, OrdinalEncoder]: df encoded and ordinal encoder transformer
    """
    columns_to_transform = [
        'Sex', 'Embarked', 'Title', 
        'Family_size_discretized'
        ]
    
    oe_transformer = OrdinalEncoder()
    
    df_train_encoded[columns_to_transform] = oe_transformer.fit_transform(df_train_encoded[columns_to_transform])
    df_test_encoded[columns_to_transform] = oe_transformer.fit_transform(df_test_encoded[columns_to_transform])

    return df_train_encoded, df_test_encoded, oe_transformer

def standard_scaler(df_train, df_test):
    """This method uses a scaler (Standard Scaler)  in the continuos columns in df
    Continuous columns: 
        'Age', 'Fare'
        
    Args:
        df_train_encoded (pd.DataFrame): df_train encoded using an ordinal encoder
        df_tesst_enriched (pd.DataFrame): df_test encoded using an ordinal encoder
        
    Returns:
        Dict[pd.DataFrame, OrdinalEncoder]: df encoded and ordinal encoder transformer
    """
    # Feature Scaling is important because age and Fare have a lot of variations
    # Without a scaler the predictive algorithm might interpret age and fare values as having a higher weight 
    st_scale = StandardScaler()
    continuous_cols = ['Age', 'Fare']
    ## transforming "train"
    df_train[continuous_cols] = st_scale.fit_transform(df_train[continuous_cols])
    ## transforming "test_x"
    df_test[continuous_cols] = st_scale.transform(df_test[continuous_cols])

    return df_train, df_test, st_scale






