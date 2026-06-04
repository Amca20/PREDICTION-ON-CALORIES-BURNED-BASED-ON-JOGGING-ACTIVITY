# 🏃‍♂️ Calories Burned Prediction Based on Jogging Activity

A machine learning-based analytics application designed to predict energy expenditure by leveraging personalized physiological features and jogging telemetry data. By integrating multi-model regression frameworks, this system replaces traditional, static calorie formulas with custom, data-driven health insights.

---

## 📌 Project Overview & Engineering Objectives

Traditional fitness tracking tools rely heavily on static look-up charts or generalized metabolic formulas that completely ignore individual physiological variances. This project implements a fully automated machine learning pipeline to process localized fitness data collected via digital forms at Universiti Teknikal Malaysia Melaka (UTeM), optimizing predictive accuracy for dynamic user profiles.

### 🎯 Core Objectives:
* **High-Precision Prediction:** Leverage distinct user physiological vectors (Age, Weight, Height, Gender, and calculated BMI) alongside specific workout limits (Duration) to compute highly accurate active calorie dissipation.
* **Algorithmic Benchmarking:** Systematically evaluate complex machine learning architectures against baseline models to find the perfect balance between low variance and high explanatory power ($R^2$).
* **Modular Pipeline Design:** Build an end-to-end reproducible script architecture—ranging from descriptive data ingestion to production-ready regression suites.

---

## 🛠️ Proposed Solution & System Flowchart

The system routes data dynamically through explicit cleaning bounds, categorical encodings, feature extractions, and model evaluations.

### 🔄 Data & Execution Pipeline Diagram
Here is the concrete operational logic flowchart designed and implemented for this machine learning pipeline:

![System Architecture Flowchart](image_4f4ba6.png)

*The workflow ensures that all features are properly scaled, transformed into numeric matrices, and isolated via Recursive Feature Elimination (RFE) before entering the model array.*

---

## 📊 Exploratory Data Analysis & Experimental Setup

### 📈 Baseline Statistical Profiling (RStudio Environment)
Prior to training machine learning models, fundamental statistical data profiling was executed within the RStudio platform to evaluate target density, measurement distribution metrics, and central tendencies across the jogging dataset:
* **Mean Energy Expenditure:** `318.17 kcal`
* **Median Energy Expenditure:** `289.10 kcal`
* **Variance Matrices:** Evaluated using Quantile distributions ($Q_1$ and $Q_3$) alongside variance analysis (`var()`) to pinpoint dataset spread anomalies.

### 🧠 Machine Learning Model Evaluation Matrix
The data matrix was benchmarked across seven predictive regression models using **5-Fold Cross-Validation** to guarantee reliable generalization performance and eliminate overfitting loops.

| Regressor Model Architecture | Technical Characteristics & System Insights | Performance Metrics ($R^2$ / MAE) |
| :--- | :--- | :--- |
| **K-Nearest Neighbors (KNN)** | Relies on local geometry and spatial coordinate distance averages; highly sensitive to feature distance scaling but bounds localized prediction steps safely. | $R^2 = 0.26$ <br> **MAE = 68.40** *(Lower absolute error variance)* |
| **XGBoost Regressor** *(Optimized)* | High-performance gradient tree-boosting suite that builds sequential correction estimators to resolve highly non-linear feature interactions. | **$R^2 = 0.69$** *(Superior Explanatory Power)* <br> MAE = 92.74 |
| **Ensemble Regressors** | Multiple Linear Regression (MLR), Support Vector Regression (SVR), Random Forest (RFR), Gradient Boosting (GBR), Stacking, and Voting Regressors. | *Hyperparameters optimized using multi-grid evaluation loops.* |

> 💡 **Engineering Insight:** Although the baseline **KNN Regressor** delivers a narrower individual margin of error on average (lower Mean Absolute Error), the optimized **XGBoost Regressor** exhibits vastly superior structural capability—successfully capturing **69% of the variance** ($R^2 = 0.69$) across all target activities.

---

## 💻 Tech Stack & Ecosystem Dependencies
* **Programming Languages:** Python 3.x Engine & RStudio Environment (Descriptive analytics suite)
* **Machine Learning Frameworks:** `scikit-learn`, `XGBoost`, `SciPy (scipy.stats)`, `pandas`, `numpy`
* **Visual Data Plotting:** `matplotlib`, `seaborn`
* **Data Origin:** Localized jogging dataset compiled through targeted digital user telemetry surveys.

---

## 👥 Our Team (Project Contributors)

This research, mathematical modeling, and software pipeline was engineered and benchmarked by:
* **Iman Muzakkir**
* **Muhammad Nur Irfan Izdiyat**
* **Muhammad Danish Farhan**
* **Ammar Zaim**
* **Muhammad Amsyar Bin Hazalan**
* **Muhammad Hafizuddin**
* **Mohd Haziq Zhafri**

---

## 🗂️ Project Repository Artifacts & Materials
* `ML Report (1).pdf` — Definitive technical project paper outlining full validation folds, mathematical proofs, and data analysis logs.
* `Calorie.csv` — Raw dataset matrix tracking physical metrics and jogging parameters.
