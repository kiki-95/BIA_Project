# BIA_Project🚀

Project Overview 🔭
Stellar Object Classification Using Spectral Characteristics

   ![galaxy](https://github.com/user-attachments/assets/3ad541a8-3013-497f-be75-6b9464bbc8b7)
Project Overview

This project focuses on classifying celestial objects—stars, galaxies, and quasars (luminous supermassive black holes)—based on their spectral characteristics. By leveraging machine learning, we aim to analyze spectral data to extract meaningful insights, enabling a deeper understanding of the universe's structure and evolution.

Table of Contents

Introduction

Dataset

Methodology

Results

Streamlit App

Setup and Usage

Contributing

License

Introduction

Astronomy involves studying objects beyond Earth's atmosphere, such as stars, galaxies, and quasars. Spectral classification is a crucial tool for understanding the properties of these objects, including their composition, temperature, and magnetic fields. This project uses machine learning models to classify celestial objects based on spectral data, contributing to a more profound comprehension of the cosmos.

Dataset

Source: [Insert Dataset Source Here, e.g., Sloan Digital Sky Survey (SDSS)]

Features:

Spectral data (e.g., flux, wavelength)

Object types (stars, galaxies, quasars)

Additional properties like redshift and magnitudes

Preprocessing Steps:

Cleaning missing or inconsistent values

Normalizing spectral features

Splitting the dataset into training and testing sets

Methodology

Data Preprocessing:

Handling missing values and outliers.

Normalizing spectral data for consistency.

Exploratory Data Analysis:

Visualizing spectral differences among stars, galaxies, and quasars.

Identifying key spectral features.

Modeling:

Algorithms used: Logistic Regression, Random Forest, and Support Vector Machines (SVM).

Evaluation metrics: Accuracy, Precision, Recall, F1-Score.

Deployment:

Streamlit app for interactive classification and visualization.

Results

Key Metrics:

Accuracy: XX%

Precision: XX%

Recall: XX%

Insights:

Stars exhibit distinct spectral patterns compared to galaxies and quasars.

Quasars have unique redshift and high luminosity features.

Streamlit App

An interactive web application has been developed using Streamlit to:

Upload spectral data for classification.

Visualize predictions with confidence scores.

To run the app locally:

Install dependencies from requirements.txt.

Run the command: streamlit run app/streamlit_app.py.

Setup and Usage

Prerequisites

Python 3.8 or higher

Libraries: pandas, numpy, scikit-learn, matplotlib, seaborn, streamlit

Installation

Clone the repository:

git clone https://github.com/your-username/stellar-object-classification.git

Navigate to the project directory:

cd stellar-object-classification

Install required libraries:

pip install -r requirements.txt

Usage

Preprocess the dataset using the data_preprocessing.ipynb notebook.

Train the model with model_training.ipynb.

Launch the Streamlit app for interactive classification.

Contributing

Contributions are welcome! To contribute:

Fork the repository.

Create a new branch for your feature:

git checkout -b feature-name

Commit your changes and push to your branch:

git push origin feature-name

Submit a pull request.

License

This project is licensed under the MIT License.





   

3. Dataset Overview 📊
   The dataset used in this project contains 100,000 observations of space captured by the Sloan Digital Sky Survey (SDSS). Each data point consists of 17 feature columns and 1 class column, which identifies the 
   object as either a star, galaxy, or quasar.

  Note: The SDSS data is publicly available. Please refer to the citation at the end for more information


  4. **📊 Models Used**
      The following machine learning models were implemented and compared:
       1. Decision Tree
       2. Random Forest
       3. K-Nearest Neighbors (KNN)
       4. Support Vector Machines (SVM)
       5. Gradient Boosting
       6. AdaBoost
       7.  XGBoost


XGBoost demonstrated superior performance in terms of accuracy, precision, and recall compared to other models.
