import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("model/student_model.pkl")

# Page configuration
st.set_page_config(
    page_title="Student Marks Prediction",
    page_icon="🎓",
    layout="centered"
)

# Title
st.title("🎓 Student Marks Prediction")

st.write(
    "Enter the student's academic details to predict the final score."
)

st.divider()

# Input fields
study_hours = st.number_input(
    "📚 Study Hours",
    min_value=0.0,
    max_value=24.0,
    value=6.0,
    step=0.5
)

attendance = st.number_input(
    "📅 Attendance (%)",
    min_value=0.0,
    max_value=100.0,
    value=85.0,
    step=1.0
)

previous_score = st.number_input(
    "📝 Previous Score",
    min_value=0.0,
    max_value=100.0,
    value=72.0,
    step=1.0
)

assignment_score = st.number_input(
    "📖 Assignment Score",
    min_value=0.0,
    max_value=100.0,
    value=80.0,
    step=1.0
)

st.divider()

# Prediction
if st.button("🔮 Predict Final Score", use_container_width=True):

    new_student = pd.DataFrame(
        [[study_hours, attendance, previous_score, assignment_score]],
        columns=[
            "Study_Hours",
            "Attendance",
            "Previous_Score",
            "Assignment_Score"
        ]
    )

    prediction = model.predict(new_student)[0]

    st.success(
        f"🎯 Predicted Final Score: {prediction:.2f}"
    )

    # Simple interpretation
    if prediction >= 80:
        st.info("Excellent predicted performance!")
    elif prediction >= 60:
        st.info("Good predicted performance.")
    else:
        st.warning("The student may need additional preparation.")

st.divider()

st.caption(
    "Machine Learning Model: Linear Regression"
)