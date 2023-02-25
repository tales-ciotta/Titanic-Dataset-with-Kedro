"""
This is a boilerplate pipeline 'training'
generated using Kedro 0.18.5
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import(train_classification_model) #generate_training_metrics,)
from kedro.extras.datasets.text import TextDataSet

def create_pipeline(**kwargs) -> Pipeline:

    return pipeline(
        [
            node(
                func = train_classification_model,
                inputs = ["df_train_scaled", "df_test_scaled", "df_test"], 
                outputs = ["classification_model", "score", "prediction"],
                name = 'train_classification_model'),
            # node(
            #     func = generate_training_metrics,
            #     inputs = ["df_test_scaled", "classification_model"],
            #     outputs = ["model_performance_report_md"],
            #     name = 'generate_training_metrics'
            # ),
        ]
    )





