import pandas as pd
import yfinance as yf
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

print("Downloading stock data...")

# Download Apple stock data
data = yf.download("AAPL", start="2015-01-01", end="2024-01-01")

print("Data Loaded")
print(data.head())

# Feature engineering
data["Return"] = data["Close"].pct_change()
data["MA10"] = data["Close"].rolling(10).mean()
data["MA50"] = data["Close"].rolling(50).mean()

data = data.dropna()

# Target variable
data["Target"] = (data["Return"].shift(-1) > 0).astype(int)

X = data[["Return", "MA10", "MA50"]]
y = data["Target"]

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, shuffle=False, test_size=0.2
)

print("Training model...")

model = RandomForestClassifier()
model.fit(X_train, y_train)

pred = model.predict(X_test)

print("Model Evaluation:")
print(classification_report(y_test, pred))

import matplotlib.pyplot as plt

data["Close"].plot(title="Apple Stock Price Trend")
plt.show()