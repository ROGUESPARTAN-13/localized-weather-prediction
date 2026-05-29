<<<<<<< HEAD
# 🌦 Weather Prediction Project

## 📌 Project Overview

The Weather Prediction Project is a Machine Learning application that predicts weather conditions based on weather-related features such as precipitation, temperature, wind speed, and date information.

The project uses the Seattle Weather Dataset and compares multiple machine learning algorithms to identify the best-performing model.

---

## 🎯 Objective

To build a machine learning model that can accurately predict weather conditions:

* Drizzle
* Fog
* Rain
* Snow
* Sun

---

## 📂 Dataset Information

**Dataset:** Seattle Weather Dataset

**Features:**

* Precipitation
* Maximum Temperature
* Minimum Temperature
* Wind Speed
* Date

**Target Variable:**

* Weather

Total Records: **1461**

---

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Streamlit
* Git & GitHub

---

## 📊 Exploratory Data Analysis (EDA)

Performed:

* Dataset Overview
* Missing Value Analysis
* Duplicate Record Analysis
* Weather Distribution Visualization
* Temperature Distribution Analysis
* Correlation Heatmap

---

## ⚙ Data Preprocessing

The following preprocessing steps were performed:

1. Checked Missing Values
2. Removed Duplicate Records
3. Converted Date Column into:

   * Year
   * Month
   * Day
4. Dropped Original Date Column
5. Applied Label Encoding on Weather Column

Weather Mapping:

* drizzle → 0
* fog → 1
* rain → 2
* snow → 3
* sun → 4

---

## 🤖 Machine Learning Models

### Decision Tree Classifier

Accuracy: **75.77%**

### Random Forest Classifier

Accuracy: **84.98%**

### K-Nearest Neighbors (KNN)

Accuracy: **70.31%**

---

## 🏆 Best Model

**Random Forest Classifier**

Accuracy Achieved: **84.98%**

The Random Forest model outperformed all other models and was selected as the final prediction model.

---

## 🌐 Streamlit Web Application

A Streamlit-based web application was developed where users can enter:

* Precipitation
* Maximum Temperature
* Minimum Temperature
* Wind Speed
* Year
* Month
* Day

The application predicts the weather condition using the trained Random Forest model.

---

## 📁 Project Structure

```text
WeatherPredictionProject
│
├── app
│   └── app.py
│
├── dataset
│   └── seattle-weather.csv
│
├── models
│   ├── weather_model.pkl
│   └── label_encoder.pkl
│
├── notebooks
│   ├── weather_prediction.ipynb
│   └── eda.py
│
├── screenshots
│
└── README.md
```

---

## 🚀 How to Run the Project

### Install Dependencies

```bash
pip install pandas numpy scikit-learn matplotlib seaborn streamlit
```

### Run Streamlit App

```bash
streamlit run app/app.py
```

---

## 📈 Results

| Model         | Accuracy |
| ------------- | -------- |
| Decision Tree | 75.77%   |
| Random Forest | 84.98%   |
| KNN           | 70.31%   |

---

## 👨‍💻 Author

**Nikkala Koteswara Rao**

Weather Prediction Project using Machine Learning and Streamlit.
=======
# 🌦 Weather Prediction Project

## 📌 Project Overview

The Weather Prediction Project is a Machine Learning application that predicts weather conditions based on weather-related features such as precipitation, temperature, wind speed, and date information.

The project uses the Seattle Weather Dataset and compares multiple machine learning algorithms to identify the best-performing model.

---

## 🎯 Objective

To build a machine learning model that can accurately predict weather conditions:

* Drizzle
* Fog
* Rain
* Snow
* Sun

---

## 📂 Dataset Information

**Dataset:** Seattle Weather Dataset

**Features:**

* Precipitation
* Maximum Temperature
* Minimum Temperature
* Wind Speed
* Date

**Target Variable:**

* Weather

Total Records: **1461**

---

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Streamlit
* Git & GitHub

---

## 📊 Exploratory Data Analysis (EDA)

Performed:

* Dataset Overview
* Missing Value Analysis
* Duplicate Record Analysis
* Weather Distribution Visualization
* Temperature Distribution Analysis
* Correlation Heatmap

---

## ⚙ Data Preprocessing

The following preprocessing steps were performed:

1. Checked Missing Values
2. Removed Duplicate Records
3. Converted Date Column into:

   * Year
   * Month
   * Day
4. Dropped Original Date Column
5. Applied Label Encoding on Weather Column

Weather Mapping:

* drizzle → 0
* fog → 1
* rain → 2
* snow → 3
* sun → 4

---

## 🤖 Machine Learning Models

### Decision Tree Classifier

Accuracy: **75.77%**

### Random Forest Classifier

Accuracy: **84.98%**

### K-Nearest Neighbors (KNN)

Accuracy: **70.31%**

---

## 🏆 Best Model

**Random Forest Classifier**

Accuracy Achieved: **84.98%**

The Random Forest model outperformed all other models and was selected as the final prediction model.

---

## 🌐 Streamlit Web Application

A Streamlit-based web application was developed where users can enter:

* Precipitation
* Maximum Temperature
* Minimum Temperature
* Wind Speed
* Year
* Month
* Day

The application predicts the weather condition using the trained Random Forest model.

---

## 📁 Project Structure

```text
WeatherPredictionProject
│
├── app
│   └── app.py
│
├── dataset
│   └── seattle-weather.csv
│
├── models
│   ├── weather_model.pkl
│   └── label_encoder.pkl
│
├── notebooks
│   ├── weather_prediction.ipynb
│   └── eda.py
│
├── screenshots
│
└── README.md
```

---

## 🚀 How to Run the Project

### Install Dependencies

```bash
pip install pandas numpy scikit-learn matplotlib seaborn streamlit
```

### Run Streamlit App

```bash
streamlit run app/app.py
```

---

## 📈 Results

| Model         | Accuracy |
| ------------- | -------- |
| Decision Tree | 75.77%   |
| Random Forest | 84.98%   |
| KNN           | 70.31%   |

---

## 👨‍💻 Author

**Nikkala Koteswara Rao**

Weather Prediction Project using Machine Learning and Streamlit.
>>>>>>> e51d6dcee7c40e6ada782a615db4b20be7074506
