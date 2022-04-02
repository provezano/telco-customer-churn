
import pickle
from flask import Flask, request, jsonify


def predict_single(customer, dv, model): 
    X = dv.transform([customer]) 
    y_pred = model.predict_proba(X)[:, 1] 
    return y_pred[0]

app = Flask('churn')

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()
    
    with open('churn-model.bin', 'rb') as f_in: 
        dv, model = pickle.load(f_in)
    
    prediction = predict_single(customer, dv, model)
    churn = prediction >= 0.5
    
    result = {'churn_probability': float(prediction), 'churn': bool(churn),}
    return jsonify(result)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
