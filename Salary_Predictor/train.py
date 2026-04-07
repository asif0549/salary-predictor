import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression

data = pd.read_csv("salary.csv")

data = data[['Experience', 'Salary']]

data = data.dropna()

X = data[['Experience']]
y = data['Salary']

model = LinearRegression()
model.fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))

print("✅ Model trained successfully!")
