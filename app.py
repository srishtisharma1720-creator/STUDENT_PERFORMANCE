from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load model + preprocessor
model = pickle.load(open("model.pkl", "rb"))
preprocessor = pickle.load(open("preprocessor.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html", form_data=None)


@app.route("/predict", methods=["POST"])
def predict():
    try:
        input_data = request.form.to_dict()

        # Convert numeric fields
        numeric_fields = [
            "age", "study_hours", "attendance_percentage",
            "math_score", "science_score", "english_score"
        ]

        for field in numeric_fields:
            input_data[field] = float(input_data[field])

        # Convert to DataFrame
        input_df = pd.DataFrame([input_data])

        # Apply SAME preprocessing used during training
        input_processed = preprocessor.transform(input_df)

        prediction = model.predict(input_processed)[0]

        return render_template(
            "index.html",
            prediction_text=f"🎯 Predicted Final Score: Grade{prediction}",
            form_data=request.form
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction_text=f"Error: {str(e)}",
            form_data=request.form
        )


if __name__ == "__main__":
    app.run(debug=True)
