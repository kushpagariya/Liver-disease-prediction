from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load model and encoder
model = joblib.load('liver_disease_model.pkl')
le = joblib.load('label_encoder.pkl')

# IMPORTANT: Update these based on your CSV columns
FEATURE_COLUMNS = [
    'Age', 'Gender', 'Total_Bilirubin', 'Direct_Bilirubin', 
    'Alkaline_Phosphatase', 'Alamine_Aminotransferase', 
    'Aspartate_Aminotransferase', 'Total_Protiens', 
    'Albumin', 'Albumin_and_Globulin_Ratio'
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_page')
def predict_page():
    return render_template('predict.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        
        # Create DataFrame with correct column order
        input_df = pd.DataFrame([data])
        
        # Encode Gender
        input_df['Gender'] = le.transform(input_df['Gender'])
        
        # Predict
        prediction = model.predict(input_df)[0]
        proba = model.predict_proba(input_df)[0]
        
        # Get probability for class 1 (Disease)
        disease_prob = proba[1] if len(proba) > 1 else proba[0]
        
        result = "Liver Disease Detected" if prediction == 1 else "No Liver Disease"
        
        return jsonify({
            'result': result,
            'probability': f"{disease_prob * 100:.2f}%",
            'is_disease': int(prediction)
        })
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)