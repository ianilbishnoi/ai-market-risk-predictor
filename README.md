# AI Market Risk Predictor

## Overview

The **AI Market Risk Predictor** is a machine learning project designed to analyze historical stock market data and predict the **next-day price movement** of a stock.
The system uses financial indicators and a machine learning classification model to determine whether the stock price is likely to **increase or decrease**.

This project demonstrates how machine learning can be applied to **financial market analysis and risk prediction**.

---

## Key Features

* Automatic download of historical stock data
* Feature engineering using financial indicators
* Machine learning based prediction of market direction
* Visualization of stock trends
* Model evaluation using classification metrics

---

## Technologies Used

* Python
* Pandas
* Scikit-learn
* Matplotlib
* yfinance

---

## How It Works

### 1. Data Collection

Historical stock price data is downloaded using the `yfinance` library.

### 2. Feature Engineering

The following financial indicators are created:

* Daily Return
* 10-Day Moving Average (MA10)
* 50-Day Moving Average (MA50)

### 3. Machine Learning Model

A **Random Forest Classifier** is trained on historical data to predict whether the stock price will move **up or down the next day**.

### 4. Model Evaluation

The model is evaluated using:

* Precision
* Recall
* F1 Score
* Accuracy

---

## Project Structure

ai-market-risk-predictor/

market_predictor.py → Main machine learning script
README.md → Project documentation

---

## Installation

Clone the repository:

```
git clone https://github.com/ianilbishnoi/ai-market-risk-predictor.git
```

Navigate to the project folder:

```
cd ai-market-risk-predictor
```

Install required dependencies:

```
pip install pandas scikit-learn yfinance matplotlib
```

---

## Running the Project

Run the script:

```
python market_predictor.py
```

The program will:

1. Download historical stock data
2. Train the machine learning model
3. Evaluate prediction performance
4. Display a stock price trend graph

---

## Example Output

The program prints classification metrics such as:

Precision
Recall
F1 Score
Accuracy

These metrics help evaluate how well the model predicts stock market movement.

---

## Applications

This type of system can be used in:

* Financial risk analysis
* Algorithmic trading research
* Market trend prediction
* Quantitative finance experimentation

---

## Future Improvements

* Add more technical indicators
* Use advanced models such as XGBoost or Neural Networks
* Implement real-time stock prediction
* Build a web dashboard for visualization

---

## Author

Anil
