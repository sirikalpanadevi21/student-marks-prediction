# Student Marks Prediction Using Machine Learning

## 📌 Project Overview

Student Marks Prediction is a beginner-friendly Machine Learning project that predicts a student's final score based on their study hours, attendance, previous score, and assignment score.

The project uses **Linear Regression** to learn the relationship between these factors and the final score.

A simple **Streamlit web application** is provided so users can enter student details and receive a predicted final score.

## 🎯 Objective

The main objective of this project is to demonstrate a complete basic Machine Learning workflow:

* Data collection
* Data loading
* Feature selection
* Train-test splitting
* Model training
* Model evaluation
* Prediction
* Model saving
* Web application development

## 🛠️ Technologies Used

* Python
* Pandas
* Scikit-learn
* Joblib
* Streamlit

## 📊 Input Features

The model uses four input features:

| Feature          | Description                                |
| ---------------- | ------------------------------------------ |
| Study Hours      | Number of hours spent studying             |
| Attendance       | Student attendance percentage              |
| Previous Score   | Score obtained in the previous examination |
| Assignment Score | Assignment marks                           |

### Target Variable

**Final Score** — the score predicted by the Machine Learning model.

## 🤖 Machine Learning Model

The project uses **Linear Regression**.

The dataset is divided into:

* **80% Training Data**
* **20% Testing Data**

The model is evaluated using **Mean Absolute Error (MAE)**.

## 📈 Model Performance

Using the current sample dataset:

**Mean Absolute Error: 0.69**

The model predicted a final score of approximately **77.90** for a student with:

* Study Hours: 6
* Attendance: 85%
* Previous Score: 72
* Assignment Score: 80

> Note: The current dataset is a small educational dataset created for learning and demonstration. The model performance should not be interpreted as representative of real-world student performance.

## 📁 Project Structure

```text
Student_Marks_Prediction/
│
├── dataset/
│   └── student_data.csv
│
├── model/
│   └── student_model.pkl
│
├── train.py
├── app.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation

Clone the repository:

```bash
git clone <https://github.com/sirikalpanadevi21/student-marks-prediction>
```

Move into the project directory:

```bash
cd Student_Marks_Prediction
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

## ▶️ Run the Project

First, train the model:

```bash
python train.py
```

Then start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

## 💡 How It Works

```text
Student Dataset
       ↓
Data Loading
       ↓
Feature Selection
       ↓
Train/Test Split
       ↓
Linear Regression
       ↓
Model Evaluation
       ↓
Save Trained Model
       ↓
Streamlit Application
       ↓
Student Input
       ↓
Predicted Final Score
```

## 🚀 Future Improvements

* Use a larger real-world dataset
* Compare Linear Regression with Decision Tree and Random Forest
* Add graphical data analysis
* Add more student-related features
* Improve prediction performance
* Deploy the application online

## 👨‍💻 Author

**Nadimidoddi Siri Kalpana Devi**

B.Tech — Computer Science / Artificial Intelligence and Machine Learning
