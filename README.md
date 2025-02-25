## 🌌 Stellar Object Classification Project


This project focuses on classifying celestial objects—stars, galaxies, and quasars—based on their spectral characteristics. By leveraging machine learning, we analyze spectral data to extract meaningful insights.

## 📋 Table of Contents

- [Introduction](#introduction)
- [Dataset](#dataset)
- [Methodology](#methodology)
- [Results](#results)
- [Streamlit App](#streamlit-app)
- [Setup and Usage](#setup-and-usage)
- [Contributing](#contributing)
- [License](#license)

---

## 🌠 Introduction

Astronomy involves studying objects beyond Earth's atmosphere, such as stars, galaxies, and quasars. Spectral classification is a crucial tool for understanding the properties of these objects, including their composition, temperature, and magnetic fields. 


## 🗂 Dataset

- **Source**: Sloan Digital Sky Survey (SDSS)  
- **Features**:
  - Spectral data (flux, wavelength)
  - Object types (stars, galaxies, quasars)
  - Additional properties like redshift and magnitudes  
- **Preprocessing Steps**:
  - Cleaning missing or inconsistent values
  - Normalizing spectral features
  - Splitting the dataset into training and testing sets  
- **Dataset Overview**:
  - **100,000 observations**
  - **17 feature columns** + 1 class column (object type)

---
🛠️ Technologies Used
---------------------

-   **Python**
-   **Streamlit**
-   **Scikit-Learn**
-   **XGBoost**
-   **Pandas, NumPy**
-   **Matplotlib, Seaborn**

* * * * *


## Methodology

### Data Preprocessing
- Handle missing values and outliers
- Normalize spectral data for consistency

### Exploratory Data Analysis
- Visualize spectral differences between stars, galaxies, and quasars
- Identify key spectral features

### Machine Learning Models
- **Algorithms Used**: 
  - Logistic Regression, Random Forest, Support Vector Machines (SVM)
  - Decision Tree, K-Nearest Neighbors (KNN), Gradient Boosting
  - XGBoost (best performer)
- **Evaluation Metrics**: 
  - Accuracy, Precision, Recall, F1-Score

### Deployment
- **Interactive Streamlit App** for classification and visualization
- ## 🌐 Streamlit App
  Local URL: http://localhost:8501
  Network URL: http://192.168.1.9:8501

---

## 📊 Results


The table below compares the performance of the models:

| Model | Accuracy | Precision | Recall |F1 Score |
| --- | --- | --- | --- | --- |
| Decision Tree | 95% | 95% | 95% | 95% |
| Random Forest | 95% | 95% | 95% | 95% |
| KNN | 89% | 89% | 89% | 89% |
| SVM | 93% | 93% | 93% | 92% |
| **Gradient Boosting** | 96% | 96% | 96% | 96% |
| AdaBoost | 85% | 80% | 85% | 82% |
| **XGBoost** | **97%** | **97%** | **97%** | **97%** |

* * * * *

- **Insights**:
  - Stars exhibit distinct spectral patterns compared to galaxies and quasars
  - Quasars are unique due to their high redshift and luminosity
- **Best Model**: XGBoost outperformed other models in accuracy, precision, and recall

---
👩‍💻 Author
------------

**Khyathi Kotian**

##🌌 Acknowledgments

The dataset is sourced from the Sloan Digital Sky Survey (SDSS), which provides publicly available astronomical data. Please refer to their official website for citation details.
