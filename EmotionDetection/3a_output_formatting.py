from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EmotionOptions

def emotion_predictor(text):
    # Initialize Watson NLU with your API credentials
    nlu = NaturalLanguageUnderstandingV1(
        version='2022-03-20',
        iam_apikey='YOUR_API_KEY',  # Replace with your actual API key
        url='YOUR_SERVICE_URL'      # Replace with your service URL
    )

    # Get the emotion analysis result
    response = nlu.analyze(
        text=text,
        features=Features(emotion=EmotionOptions())
    ).get_result()

    # Extract emotions from the response
    emotions = response['emotion']['document']['emotion']

    # Format the output to match the desired structure
    formatted_emotions = {
        'joy': f"{emotions['joy']*100:.2f}%",
        'anger': f"{emotions['anger']*100:.2f}%",
        'fear': f"{emotions['fear']*100:.2f}%",
        'sadness': f"{emotions['sadness']*100:.2f}%",
        'disgust': f"{emotions['disgust']*100:.2f}%"
    }

    return formatted_emotions

# Example test
if __name__ == "__main__":
    test_text = "I feel so happy and full of energy today!"
    result = emotion_predictor(test_text)
    print(result)
