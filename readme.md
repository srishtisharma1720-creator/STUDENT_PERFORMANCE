🎓 STUDENT PERFORMANCE PREDICTION USING MACHINE LEARNING

End-to-end Machine Learning project to predict student academic performance (Grade) using demographic, academic, and lifestyle factors.
Includes EDA, preprocessing, model training, evaluation, and deployment using Flask.

The objective is to build a reliable prediction model by performing data analysis, preprocessing, model training, evaluation, and finally deploying it as an interactive web application.

📌 PROBLEM STATEMENT

Student academic performance depends on multiple factors such as study habits, attendance, parental education, and lifestyle.

Early prediction of academic performance helps:

Identify at-risk students

Provide academic support

Improve overall institutional outcomes

This project applies Machine Learning to predict student grades based on various input features.

📊 DATASET
🔹 Input Features

Age

Gender

School Type

Parent Education

Study Hours

Attendance Percentage

Internet Access

Travel Time

Extra Activities

Study Method

Math Score

Science Score

English Score

🎯 Target Variable

Final Grade:

Grade A

Grade B

Grade C

Grade D

🔍 EXPLORATORY DATA ANALYSIS (EDA)

Distribution analysis of numerical features

Study hours vs performance comparison

Attendance impact analysis

Correlation heatmap

Subject score relationship analysis

Feature importance understanding

EDA helped identify key academic patterns affecting student performance.

🧠 MODEL USED

✔ Random Forest Regressor / Classifier

Why Random Forest?

Handles non-linear relationships

Performs well on tabular structured data

Reduces overfitting

High stability and accuracy

Works well with mixed numerical & categorical features

Selected as final model due to strong predictive performance.

🏗 MACHINE LEARNING PIPELINE

Data Cleaning

Handling missing values

Categorical feature encoding

Train-Test Split

Model Training

Model Evaluation

Model Saving (pickle)

Flask Deployment Integration

🧪 EVALUATION METRICS

Accuracy (for classification)

Mean Squared Error (if regression used)

R² Score

Confusion Matrix

Feature Importance

Model performance was evaluated to ensure reliability before deployment.

🏆 FINAL MODEL

Random Forest Model

Reason

Strong predictive performance

Robust with real-world academic data

Handles feature interactions efficiently

Stable predictions

💻 WEB APPLICATION

Built using Flask

Features

Modern glassmorphism UI

Responsive design

Form-based student input

Color-coded grade output

Real-time prediction

Clean result display

Prediction Output

🎯 Predicted Final Grade: A / B / C / D

Styled grade box with color indication

🛠 TECH STACK

Python

Pandas

NumPy

Scikit-learn

Matplotlib

Seaborn

Flask

HTML & CSS

Git & GitHub


▶️ RUN LOCALLY
pip install -r requirements.txt
python app.py


Open in browser:

http://127.0.0.1:5000/

🚀 FUTURE WORK

Add multiple ML models comparison

Hyperparameter tuning

Deploy on Render / Railway

Add performance visualization dashboard

Add downloadable report

Add database integration

🎓 LEARNING OUTCOMES

Data preprocessing & feature engineering

Supervised ML modeling

Model evaluation techniques

ML model deployment

Flask backend integration

Frontend & Backend integration

Git & GitHub project management

📌 About

Student Performance Prediction System using Machine Learning & Flask Deployment.
