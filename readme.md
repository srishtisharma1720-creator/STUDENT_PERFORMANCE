# 🎓 Student Performance Prediction Using Machine Learning

An end-to-end Machine Learning project to predict student academic performance (Grade) using demographic, academic, and lifestyle factors.

This project includes:
- Exploratory Data Analysis (EDA)
- Data preprocessing
- Model training & evaluation
- Deployment using Flask

---

## 📌 Problem Statement

Student academic performance depends on multiple factors such as:
- Study habits
- Attendance
- Parental education
- Lifestyle

Early prediction of academic performance helps:
- Identify at-risk students
- Provide academic support
- Improve institutional outcomes

This project applies Machine Learning to predict student grades based on various input features.

---

## 📊 Dataset

### 🔹 Input Features
- Age
- Gender
- School Type
- Parent Education
- Study Hours
- Attendance Percentage
- Internet Access
- Travel Time
- Extra Activities
- Study Method
- Math Score
- Science Score
- English Score

### 🎯 Target Variable
Final Grade:
- Grade A
- Grade B
- Grade C
- Grade D

---

## 🔍 Exploratory Data Analysis (EDA)

- Distribution analysis of numerical features  
- Study hours vs performance comparison  
- Attendance impact analysis  
- Correlation heatmap  
- Subject score relationship analysis  
- Feature importance understanding  

EDA helped identify key academic patterns affecting student performance.

---

## 🧠 Model Used

**Random Forest Regressor / Classifier**

### Why Random Forest?
- Handles non-linear relationships  
- Performs well on tabular data  
- Reduces overfitting  
- High stability and accuracy  
- Works well with mixed data types  

Selected as the final model due to strong predictive performance.

---

## 🏗 Machine Learning Pipeline

- Data Cleaning  
- Handling missing values  
- Categorical feature encoding  
- Train-Test Split  
- Model Training  
- Model Evaluation  
- Model Saving (pickle)  
- Flask Deployment Integration  

---

## 🧪 Evaluation Metrics

- Accuracy (for classification)  
- Mean Squared Error (for regression)  
- R² Score  
- Confusion Matrix  
- Feature Importance  

Model performance was evaluated to ensure reliability before deployment.

---

## 🏆 Final Model

**Random Forest Model**

### Reason
- Strong predictive performance  
- Robust with real-world data  
- Handles feature interactions efficiently  
- Provides stable predictions  

---

## 💻 Web Application

Built using Flask.

### Features
- Modern glassmorphism UI  
- Responsive design  
- Form-based student input  
- Color-coded grade output  
- Real-time prediction  
- Clean result display  

### Prediction Output
- Predicted Final Grade: **A / B / C / D**  
- Styled grade box with color indication  

---

## 🛠 Tech Stack

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Matplotlib  
- Seaborn  
- Flask  
- HTML & CSS  
- Git & GitHub  

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
python app.py
```

## Open in browser
```bash
http://127.0.0.1:5000/
```


## 🚀 Future Work
- Add multiple ML model comparisons
- Hyperparameter tuning
- Deploy on Render / Railway
- Add performance visualization dashboard
- Add downloadable report
- Add database integration



## 🎓 Learning Outcomes

- Data preprocessing & feature engineering
- Supervised Machine Learning modeling
- Model evaluation techniques
- ML model deployment
- Flask backend integration
- Frontend & Backend integration
- Git & GitHub project management
