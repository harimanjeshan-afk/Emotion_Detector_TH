import requests # Import the requests library to handle HTTP requests
import json # Import Jason
def emotion_detector(text_to_analyse): 
	# Define a function named Emotion Detector that takes a string input (text_to_analyse) 
	   
	# URL of the sentiment analysis service 
	url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' 

	# Create a dictionary with the text to be analyzed
	myobj = { "raw_document": { "text": text_to_analyse } } 
    
	# Set the headers required for the API request
	header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} 
		     
	# Send a POST request to the API with the text and headers 
	response = requests.post(url, json = myobj, headers=header) 
	# Parsing the JSON response from the API 
	formatted_response = json.loads(response.text)
	#Extracting emotion dictionary from the response 
	emotion = formatted_response['emotionPredictions'][0]['emotion'] 
	# Find dominant emotion
	dominant_emotion = max(emotion, key=emotion.get)
	    
	# Append to same dictionary
	emotion["dominant_emotion"] = dominant_emotion
	# Return the response text from the API
	return emotion
