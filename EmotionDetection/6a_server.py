from flask import Flask, request, jsonify
from emotion_predictor import emotion_predictor

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the text from the POST request
        data = request.get_json()
        text = data['text']

        # Get the emotion prediction
        result = emotion_predictor(text)

        # Return the result as a JSON response
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
