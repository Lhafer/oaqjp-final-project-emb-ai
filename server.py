from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector



app = Flask("Emotion Detection App")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/emotionDetector")
def detect():
    text_to_analyze = request.args.get('textToAnalyze') or ""
    emotions = emotion_detector(text_to_analyze)
    


    return    f"""For the given statement, the system response is 
    'anger': {emotions["anger"]}
    , 'disgust': {emotions["disgust"]}
    , 'fear': {emotions["fear"]}
    , 'sadness': {emotions["sadness"]}
    , 'joy': {emotions["joy"]}. 
    The dominant emotion is 
    {emotions["dominant_emotion"]}"""



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

print(emotion_detector("I'm so happy I could explode"))