# Sales Forecast (Machine Learning)

## Table of contents

- [Overview](#overview)
  - [Project Goal](#project-goal)
- [Process](#process)
  - [Technologies Used](#technologies-used)
  - [Directories Structure]()
  - [What I learned](#what-i-learned)
  - [Addtional Features](#additional-feature)
  - [How to Run the Project](#how-to-run-the-project)
- [Author](#author)

## Overview

### Project Goal

- The main goal of this project is to predict sales for a given period based on advertising spend across different channels. Specifically, we analyze investments in TV, Radio, and Newspaper ads, using machine learning models to create an accurate sales forecast.

### This project was originally developed in 2022 during the "Intensivão de Python" livestream by Hashtag Programação and is now in 2024 updated.
- Website: https://www.hashtagtreinamentos.com/
- Youtube channel: https://www.youtube.com/c/HashtagPrograma%C3%A7%C3%A3o
- Instagram: https://www.instagram.com/hashtagprogramacao/



## Process

### Technologies Used

- Python: Core language for data manipulation and model building.
- Pandas: For data analysis and manipulation.
- Seaborn: For data visualization and statistical graphics.
- Scikit-learn: To implement machine learning models.
- Matplotlib: For additional visualizations.

---

### Directories Structures

sales-forecast-project/
- data/                   # Folder containing datasets
  - advertising_budget_and_sales.csv

- notebooks/              # Jupyter notebooks used for development and testing
  - sales_forecast.ipynb

- src/                    # Source code for the machine learning model
  - init.py # Makes this directory a package
  - data_preprocessing.py # Data cleaning and preprocessing scripts
  - model_training.py # Scripts for training machine learning models 
  - feature_engineering.py # Scripts for feature engineering
  
- .gitignore              # Git ignore file for unnecessary files

- README.md               # Project documentation (this file)

- requirements.txt        # List of dependencies

- main.py                 # Main script to run the project

---

### What I learned

Throughout this project, I enhanced my understanding of:

- Data preprocessing techniques (handling missing values, feature engineering).
- Applying machine learning algorithms (Linear Regression, Random Forest) for regression tasks.
- Evaluating model performance with metrics like R-squared.
- The importance of ad budgeting strategies in predicting sales growth.

---

### Future Improvements

Additional data sources: Incorporate real-world online ad spend data to compare with traditional media.
Hyperparameter tuning: Apply more advanced techniques to fine-tune the machine learning models.
Model Deployment: Deploy the model using Flask or Streamlit for real-time sales predictions.

---

### Additional Feature

In addition to the original variables, I included an Internet Ad Budget feature to simulate the growing relevance of online advertising. This addition was primarily for learning purposes, as the original dataset did not account for digital marketing channels. However, this extra feature was implemented with real-world marketing challenges in mind, considering the increasing shift from traditional media to digital platforms.

Even though this was a study-based enhancement, the project as a whole was designed with real-life problem-solving in focus, emphasizing the importance of adapting machine learning models to modern business needs.

---

### How to Run the Project

#### Clone the repository:
- git clone [repo-url]

#### Navigate to the project directory:
- cd sales-forecast-project

#### Create and activate a virtual environment:
- python -m venv venv
- source venv/bin/activate  
- On Windows: venv\Scripts\activate

#### Install dependencies:
- pip install -r requirements.txt

#### Run the Jupyter notebook or Python script:
- jupyter notebook sales_forecast.ipynb

## Author

My name is Ana Vitória, and I began studying programming in 2021, primarily through self-taught methods. I am passionate about using data to solve business problems and continuously learning new skills to improve my professional expertise.

You can find me on [LinkedIn](https://www.linkedin.com/in/ana-vitoria-louro/).
