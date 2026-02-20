"""
Flask server module for the Emotion Detection web application.

This module handles routing, integrates the emotion detection
logic, and formats responses for the user interface.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def home():
    """
    Render the main index page of the application.

    Returns:
        HTML template for the home page.
    """
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Process emotion detection requests from the web interface.

    Retrieves user input text from query parameters,
    calls the emotion detection function, and returns
    a formatted response string.

    Returns:
        str: Formatted emotion analysis result or error message.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        "For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    