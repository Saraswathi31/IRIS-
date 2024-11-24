from flask import Flask, render_template, request, jsonify
import joblib

# Create the Flask app
app = Flask(__name__)

# Load the pre-trained model
model = joblib.load('iris_model.pkl')

# Define the home route to render the HTML page
@app.route('/')
def home():
    return render_template('index.html')

# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = data['features']
    prediction = model.predict([features])
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
