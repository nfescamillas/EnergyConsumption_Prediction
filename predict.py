import pickle
from flask import Flask 
from flask import request
from flask import jsonify 
import pandas as pd


with open("scaler.bin",'rb') as f_in1:
    scaler = pickle.load(f_in1)

with open("model.bin",'rb') as f_in2:
    model = pickle.load(f_in2)


app = Flask('Energy_Prediction')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    try:
        print("Received data:", data)  # Debugging step

        # Convert input data to a DataFrame
        X = pd.DataFrame([data])

        # Ensure consistency with training features
        missing_cols = set(scaler.feature_names_in_) - set(X.columns)
        for col in missing_cols:
            X[col] = 0  # Add missing columns with default values

        X = X[scaler.feature_names_in_]  # Reorder columns to match scaler

        # Scale input
        X_scaled = scaler.transform(X)

        # Predict
        y_pred = model.predict(X_scaled)

        # Prepare and send response
        result = {
            'predicted energy (kwh)': float(y_pred[0])
        }
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)