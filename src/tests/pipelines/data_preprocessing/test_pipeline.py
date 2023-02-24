import pandas as pd
from titanic_classification.pipelines.data_preprocessing.nodes import prepare_data
import pytest

def test_prepare_data():
    # create sample data with null values
    df_train = pd.DataFrame({
        'Age': [20, 30, None],
        'Embarked': ['S', 'C', None],
        'Fare': [10.0, 10, 20.0],
        'Pclass': [1, 2, 3],
        'Survived': [0, 1, 1],
        'Cabin': [1,2,3],
        'Ticket': [1,2,3],
        'PassengerId': [1,2,3],
    })
    df_test = pd.DataFrame({
        'Age': [25, 35, None],
        'Embarked': ['S', 'S', 'C'],
        'Pclass': [1, 3, 2],
        'Fare': [15.0, 25.0, 1],
        'Cabin': [1,2,3],
        'Ticket': [1,2,3],
        'PassengerId': [1,4,1]
    })

    # call prepare_data function
    df_train_processed, df_test_processed = prepare_data(df_train, df_test)

    # assert that there are no null values in the processed dataframes
    assert not df_train_processed.isnull().values.any()
    assert not df_test_processed.isnull().values.any()
    
    # assert that dropped columns are not in the processed dataframes
    assert 'Cabin' not in df_train_processed.columns
    assert 'PassengerId' not in df_train_processed.columns
    assert 'Ticket' not in df_train_processed.columns
    
    assert 'Cabin' not in df_test_processed.columns
    assert 'PassengerId' not in df_test_processed.columns
    assert 'Ticket' not in df_test_processed.columns
