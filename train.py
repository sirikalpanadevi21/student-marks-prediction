import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Load dataset
data = pd.read_csv("dataset/student_data.csv")

# Input features
X = data[["Study_Hours", "Attendance", "Previous_Score", "Assignment_Score"]]

# Target
Y = data["Final_Score"]

# Split dataset
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, Y_train)

# Save model
joblib.dump(model, "model/student_model.pkl")

print("Model saved successfully!")

# Predict test data
Y_pred = model.predict(X_test)

# Evaluate model
mae = mean_absolute_error(Y_test, Y_pred)

print("Mean Absolute Error:", mae)

# Predict a new student
new_student = pd.DataFrame(
    [[6, 85, 72, 80]],
    columns=["Study_Hours", "Attendance", "Previous_Score", "Assignment_Score"]
)

prediction = model.predict(new_student)

print("Predicted Final Score:", prediction[0])