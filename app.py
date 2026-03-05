from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
import os

app = Flask(__name__)
app.template_folder = '.'
CORS(app)

# Load model and encoder
model = joblib.load('liver_disease_model.pkl')
le = joblib.load('label_encoder.pkl')

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

# Health check endpoint for deployment
@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'service': 'LiverPredict AI'})

# API info endpoint
@app.route('/api')
def api_info():
    return jsonify({
        'name': 'LiverPredict AI API',
        'version': '1.0.0',
        'endpoints': {
            '/predict': 'POST - Make a prediction',
            '/health': 'GET - Health check'
        }
    })

# API for prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['Age', 'Gender', 'Total_Bilirubin', 'Direct_Bilirubin', 
                          'Alkaline_Phosphatase', 'Alamine_Aminotransferase', 
                          'Aspartate_Aminotransferase', 'Total_Protiens', 
                          'Albumin', 'Albumin_and_Globulin_Ratio']
        
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({'error': f'Missing required fields: {", ".join(missing_fields)}'}), 400

        # Create input DataFrame
        input_df = pd.DataFrame([data])

        # Encode gender
        if data['Gender'] in le.classes_:
            input_df['Gender'] = le.transform([data['Gender']])[0]
        else:
            return jsonify({'error': 'Invalid gender value. Use Male or Female'}), 400

        # Make prediction
        prediction = model.predict(input_df)[0]
        proba = model.predict_proba(input_df)[0]

        disease_prob = proba[1] if len(proba) > 1 else proba[0]

        result = "Liver Disease Detected" if prediction == 1 else "No Liver Disease"

        return jsonify({
            'result': result,
            'probability': f"{disease_prob * 100:.2f}%",
            'is_disease': int(prediction)
        })

    except ValueError as e:
        return jsonify({'error': f'Invalid input value: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': f'Prediction error: {str(e)}'}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
