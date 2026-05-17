# Randomforest-Regressor

# Airbnb Price Prediction using Decision Tree Regressor

This project is a Machine Learning web application built using Streamlit and Decision Tree Regressor.

The application predicts Airbnb rental prices based on location and booking details.

---

## Features Used

- Latitude
- Longitude
- Minimum Nights
- Reviews Per Month
- Availability 365

---

## Machine Learning Algorithm

- Decision Tree Regressor

---

## Technologies Used

- Python
- Streamlit
- Scikit-learn
- NumPy
- Pandas
- Joblib

---

## Project Structure

```text
AirbnbPricePrediction/
│
├── regapp.py
├── model.joblib
├── requirements.txt
└── README.md
```

---

## Installation

Install required libraries using:

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
streamlit run regapp.py
```

---

## Input Features

| Feature | Description |
|---|---|
| Latitude | Property latitude |
| Longitude | Property longitude |
| Minimum Nights | Minimum booking nights |
| Reviews Per Month | Monthly review count |
| Availability 365 | Available days in a year |

---

## Output

The application predicts:

```text
Estimated Airbnb Price
```

Example:

```text
Predicted Airbnb Price: $145.50
```

---

## Model Description

The model is trained using:

- Airbnb NYC Dataset
- Decision Tree Regressor
- Location and booking feature analysis

---

## Author

Machine Learning Mini Project
