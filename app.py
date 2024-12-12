from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

# Load the saved model and vectorizer
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"success": False, "error": "Invalid input."}), 400

    text = data["text"]
    if len(text.strip()) == 0:
        return jsonify({"success": False, "error": "Empty text provided."}), 400

    # Vectorize the input text
    X = vectorizer.transform([text])

    # Predict using the trained model
    prediction = model.predict(X)[0]

    return jsonify({"success": True, "prediction": prediction})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
