import requests
import json
import sys
import time
# pip install SpeechRecognition
# on mac, you need to install the following
#xcode-select --install
#brew install portaudio
#pip install pyaudio
import speech_recognition as sr


url_post = "http://localhost:8181/translate"  # Replace this with the actual API endpoint URL for sending data
url_get = "http://localhost:8181/results"  # Replace this with the actual API endpoint URL for getting results

recognizer = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        print("Please speak a sentence:")
        audio = recognizer.listen(source)
        
        # Record the time before sending the request to Google API
        API_start_time = time.time()

        try:
            input_text = recognizer.recognize_google(audio)
            print(f"Recognized sentence: {input_text}")
            
            # Calculate the roundtrip delay for Google's speech recognition API
            API_roundtrip_delay = time.time() - API_start_time
            print(f"Google API roundtrip delay: {API_roundtrip_delay:.2f} seconds")
            
        except sr.UnknownValueError:
            print("Could not understand the audio. Please try again.")
            continue
        except sr.RequestError as e:
            print(f"Error: {e}")
            continue

        # Define the input data in JSON format
        input_data = {
            "input_text": input_text,
        }

        # Record the time before sending the request
        start_time = time.time()

        # Send a POST request to the API endpoint with the input data as the payload
        response = requests.post(url_post, json=input_data)

        # Check if the request was successful
        if response.status_code != 200:
            print("Error: Request failed with status code", response.status_code)
            continue

        # Get the response data in JSON format
        try:
            output_data = response.json()
        except ValueError:
            print("Error: Invalid JSON response from server")
            continue

        # Check if the translation was started successfully
        if output_data['status'] == 'success':
            # Send a GET request to the API endpoint to get the translated text
            response = requests.get(url_get)

            # Get the response data in JSON format
            output_data = response.json()

            # Calculate the roundtrip delay
            roundtrip_delay = time.time() - start_time

            # Check if the translation was successful
            if output_data['status'] == 'success':
                # Print the input text and translation results with timestamps
                print(f"Input timestamp: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))}")
                print("Input text:")
                print(input_text+'\n')

                print(f"Output timestamp: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))}")
                print("Translation results:")
                print(output_data['output_text'])

                # Print the roundtrip delay
                print(f"Roundtrip delay: {roundtrip_delay:.2f} seconds\n")

            else:
                print("Translation failed.")
        else:
            print("Failed to start translation.")

        # Wait for 2 seconds before sending the next sentence
        #time.sleep(2)