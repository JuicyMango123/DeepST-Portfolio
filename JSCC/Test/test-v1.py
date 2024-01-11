import requests
import json
import sys
import time
# pip install SpeechRecognition
import speech_recognition as sr


filename = "input_sentences.txt"
url_post = "http://localhost:8181/translate"  # Replace this with the actual API endpoint URL for sending data
url_get = "http://localhost:8181/results"  # Replace this with the actual API endpoint URL for getting results

with open(filename, "r") as file:
    for line in file:
        input_text = line.strip()

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
        time.sleep(2)