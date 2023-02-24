"""
This is a boilerplate pipeline 'data_preprocessing'
generated using Kedro 0.18.5
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import (prepare_data)

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func = prepare_data, 
            inputs = ["df_train", "df_test"], 
            outputs = ["df_train_clean", "df_test_clean"],
            name = 'prepare_data'
        )
    ])