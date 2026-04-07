import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression

# Load data
data = pd.read_csv("salary.csv")

# Keep only required columns
data = data[['Experience', 'Salary']]

# Remove missing values safely
data = data.dropna()

# Features & target
X = data[['Experience']]
y = data['Salary']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("✅ Model trained successfully!")