# Classification_using_SparkML

## Overview

This Jupyter notebook demonstrates how to perform classification using Apache Spark's Machine Learning library (SparkML). The workflow includes data loading, preprocessing, feature engineering, model training, and evaluation using a logistic regression classifier on the Dry Beans dataset.

## Purpose

The notebook is designed to:
- Show how to set up and use Spark in a Python environment.
- Guide users through the process of preparing data for machine learning with SparkML.
- Train a logistic regression model to classify dry bean types based on physical characteristics.
- Evaluate the model using metrics such as accuracy, precision, recall, and F1 score.

## Usage

1. **Install Dependencies**  
   The notebook installs `pyspark` and `findspark` to enable Spark functionality in Python.

2. **Suppress Warnings**  
   Warnings are suppressed for cleaner output.

3. **Initialize Spark**  
   Spark is initialized using `findspark` and a `SparkSession` is created.

4. **Data Download and Loading**  
   The Dry Beans dataset is downloaded and loaded into a Spark DataFrame.

5. **Data Exploration**  
   The schema and sample rows are displayed, and class distributions are analyzed.

6. **Data Preprocessing**  
   - The target column (`Class`) is indexed to a numeric label.
   - Features are assembled into a single vector.

7. **Train-Test Split**  
   The data is split into training (70%) and testing (30%) sets.

8. **Model Training**  
   A logistic regression model is trained on the training data.

9. **Model Evaluation**  
   The model is evaluated on the test set using accuracy, precision, recall, and F1 score.

10. **Cleanup**  
    The Spark session is stopped at the end.

## Requirements

- Python 3.x
- Jupyter Notebook
- Internet connection (for downloading the dataset)
- The notebook will automatically install required Python packages.

## Dataset

- [Dry Beans Dataset](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-BD0231EN-SkillsNetwork/datasets/drybeans.csv)

## Author

- Initial version created by Ramesh Sannareddy

---