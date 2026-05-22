import requests
import json


def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=headers)

    
    if response.status_code == 400:
        return {
            "anger": None,
            "fear" : None,
            "sadness": None,
            "joy": None,
            "disgust": None,
            "dominant_emotion": None
        }

    emotions = json.loads(response.text)['emotionPredictions'][0]["emotion"]

    emotions["dominant_emotion"] = "joy"

    for emotion, value in emotions.items():
        if emotion == "dominant_emotion":
            continue
        if value > emotions[emotions["dominant_emotion"]]:
            emotions["dominant_emotion"] = emotion

     
        
    return emotions


