"""
This is a boilerplate pipeline 'feature_engineering'
generated using Kedro 0.18.5
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import(create_features, ordinal_encoder_str_columns,standard_scaler)


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func = create_features, 
                inputs = ["df_train_clean", "df_test_clean"], 
                outputs = ["df_train_enriched", "df_test_enriched"],
                name = 'create_features'
            ),
            node(
                func = ordinal_encoder_str_columns,
                inputs = ["df_train_enriched", "df_test_enriched"],
                outputs = ["df_train_encoded", "df_test_encoded", "oe_transformer"],
                name = 'ordinal_encoder_str_columns'
            ),
            node(
                func = standard_scaler,
                inputs = ["df_train_encoded", "df_test_encoded"],
                outputs = ["df_train_scaled", "df_test_scaled", "st_scaler"],
                name = 'standard_scaler'
            ),
        ]
    )