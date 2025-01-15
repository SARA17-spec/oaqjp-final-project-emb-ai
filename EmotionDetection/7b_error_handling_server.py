from flask import Flask, request, jsonify

app = Flask(__name__)

# Emotion detection function (for demonstration purposes)
def emotion_detector(text):
    if not text:
        # Returning a 400 error for missing or invalid text
        return jsonify({"error": "No text provided"}), 400
    # Simulate emotion detection (e.g., happy, sad)
    detected_emotion = "happy"
    return jsonify({"emotion": detected_emotion}), 200

@app.route('/detect_emotion', methods=['POST'])
def detect_emotion():
    # Get JSON data from the request body
    data = request.get_json()
    
    # Check if the 'text' field exists in the request data
    if 'text' not in data:
        return jsonify({"error": "Text field is required"}), 400  # Missing 'text' key
    
    text = data['text']
    
    # Call the emotion detection function
    return emotion_detector(text)

if __name__ == '__main__':
    app.run(debug=True)
