# Initial_ETL_Pipeline
📦 Initial ETL Pipeline Project
This project is a simple Extract-Transform-Load (ETL) pipeline built in Python to demonstrate core data engineering concepts.

🔧 Technologies Used
Python

Pandas

SQLAlchemy

PyMySQL

MySQL

📌 Project Workflow
Extract
Reads a .csv dataset using pandas.read_csv().

Transform
Cleans the dataset by:

Removing missing values

Standardizing column names (lowercase, underscores)

Load
Loads the cleaned data into a MySQL database table using SQLAlchemy’s to_sql() method.
