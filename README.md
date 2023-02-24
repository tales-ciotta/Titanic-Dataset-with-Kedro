# Titanic Classification Problem with Kedro

## Overview

The objective of this project is to implement a machine learning pipeline with Kedro to predict to predict the survival of passengers using the  [Titanic dataset](https://www.kaggle.com/competitions/titanic/data) available on Kaggle.

Take a look at the [Kedro documentation](https://kedro.readthedocs.io) to get started.

## How to install dependencies

Declare any dependencies in `src/requirements.txt` for `pip` installation and `src/environment.yml` for `conda` installation.

To install them, run:

```
pip install -r src/requirements.txt
```

## You can run the Kedro project with:

```
kedro run
```

The final output, a txt file with the accuracy score of the model and the prediction.csv will be available in the folder 'data/07_model_output'.
## Rules and guidelines

## How to test the project

 You can run the unit tests with the following command:
```
kedro test
```
Only unit tests for the data_preprocessing pipeline were created as a demonstration.

## Project dependencies

To generate or update the dependency requirements of this project:

```
kedro build-reqs
```

This will `pip-compile` the contents of `src/requirements.txt` into a new file `src/requirements.lock`. You can see the output of the resolution by opening `src/requirements.lock`.

After this, if you'd like to update your project requirements, please update `src/requirements.txt` and re-run `kedro build-reqs`.
