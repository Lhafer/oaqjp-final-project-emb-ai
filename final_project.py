from flask import Flask, render_template
from emotion_detection import emotion_detector

app = Flask("Emotion Detection App")

print(emotion_detector("I'm so happy I could explode"))