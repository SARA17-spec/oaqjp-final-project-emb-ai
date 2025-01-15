from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated emotion detection function
def emotion_detector(text):
    # Here you'd normally interact with Watson NLP or another service
    if not text:
        return jsonify({"error": "No text provided"}), 400  # 400 error for invalid input
    
    # Assuming this part works if text is valid
    detected_emotion = "happy"  # Simulate detected emotion
    return jsonify({"emotion": detected_emotion}), 200  # 200 OK status for valid request

@app.route('/detect_emotion', methods=['POST'])
def detect_emotion():
    # Get data from POST request
    data = request.get_json()
    
    if 'text' not in data:
        return jsonify({"error": "Text field is required"}), 400  # 400 error if 'text' is missing

    text = data['text']
    return emotion_detector(text)

if __name__ == "__main__":
    app.run(debug=True)
