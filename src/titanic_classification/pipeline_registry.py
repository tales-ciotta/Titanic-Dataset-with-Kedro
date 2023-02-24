"""Project pipelines."""
from typing import Dict
from kedro.pipeline import Pipeline
from titanic_classification.pipelines import (
    data_preprocessing,
    feature_engineering,
    training,
)

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    data_preprocessing_pipeline = data_preprocessing.create_pipeline()
    feature_engineering_pipeline = feature_engineering.create_pipeline()
    training_pipeline = training.create_pipeline()

    return {
        "data_preprocessing": data_preprocessing_pipeline,
        "feature_engineering": feature_engineering_pipeline,
        "training": training_pipeline,
        "__default__": (
            data_preprocessing_pipeline
            + feature_engineering_pipeline
            + training_pipeline
        ),
    }

