
# 🏠 Boston Housing Price Prediction

This project predicts housing prices in the Boston area using machine learning. It uses a dataset with various features such as crime rate, number of rooms, property tax rate, and more to estimate median home prices. The project includes data preprocessing, feature analysis, model training, and evaluation.

---
## Dataset Link
https://www.kaggle.com/datasets/heptapod/uci-ml-datasets 

## Features

* Loads and cleans housing data
* Handles missing values with median imputation
* Visualizes feature correlations with a heatmap
* Splits data into training and testing sets
* Scales features using `StandardScaler`
* Trains a Linear Regression model
* Evaluates performance using:

  * Mean Squared Error (MSE)
  * Mean Absolute Error (MAE)
  * R² Score
* Saves and loads the trained model using `pickle`
* Supports predictions for individual inputs

---

## Technologies Used

* **Python**
* **Pandas** – Data manipulation
* **NumPy** – Numerical operations
* **Matplotlib & Seaborn** – Data visualization
* **Scikit-learn** – Machine learning algorithms and metrics
* **Pickle** – Model serialization
* **Google Colab** – Cloud-based notebook execution

---

## Project Structure

```
boston_housing_project/
├── boston_housing_project.ipynb   # Main notebook
├── HousingData.csv                # Dataset (hosted on Google Drive)
├── model.pkl                      # Trained Linear Regression model
└── README.md                      # Project documentation
```

---

## Sample Results

*Example output (R² Score):* `0.73`
*Mean Absolute Error:* `3.2`
*Model: Linear Regression*

---

## Future Improvements

* Add more models like Random Forest or XGBoost
* Implement hyperparameter tuning
* Build a web UI using Streamlit for easier input
* Explore feature selection techniques

---
