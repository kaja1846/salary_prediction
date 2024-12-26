import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Sample data
data = {
    "experience": [1, 3, 5, 7, 10],
    "degree": ["Bachelors", "Bachelors", "Masters", "Masters", "PhD"],
    "current_salary": [30000, 40000, 50000, 60000, 80000],
    "salary_hike_percentage": [10, 15, 20, 25, 30],
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Encode categorical column 'degree'
df["degree_encoded"] = df["degree"].map({"Bachelors": 1, "Masters": 2, "PhD": 3})

# Define features (X) and target (y)
X = df[["experience", "degree_encoded", "current_salary"]]
y = df["salary_hike_percentage"]

# Initialize and train the model
model = LinearRegression()
model.fit(X, y)

# Save the model using joblib
joblib.dump(model, 'salary_prediction_model.pkl')
