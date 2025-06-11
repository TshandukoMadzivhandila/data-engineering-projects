# Connecting to Spark Cluster using Skills Network Labs

This project demonstrates how to connect to an Apache Spark cluster using Skills Network Labs. It provides step-by-step instructions and sample code to help you get started with Spark, load datasets, and perform basic data analysis using PySpark.

## Features

- Installation of required packages (`pyspark`, `findspark`)
- Initialization of SparkSession
- Loading and inspecting datasets (mpg and diamonds)
- Basic data exploration using Spark DataFrames

## Getting Started

1. **Install Dependencies**  
   The notebook installs the necessary Python packages:
   ```python
   !pip install pyspark==3.1.2 -q
   !pip install findspark -q