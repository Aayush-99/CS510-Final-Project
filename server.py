# from flask import Flask, request, jsonify
# from flask_cors import CORS, cross_origin
# import subprocess

# app = Flask(__name__)
# CORS(app)  # Enable CORS for all routes

# @app.route('/process', methods=['POST'])
# @cross_origin()  # Specific route CORS enablement
# def process_data():
#     try:
#         content = request.json['content']
#         print("Received content:", content)
#         response = call_llm(content)
#         print("Response:", response)
#         return jsonify({'label': response})
#     except Exception as e:
#         print("Error handling request:", str(e))
#         return jsonify({'error': str(e)}), 500
#     # content = request.json['content']
#     # response = call_llm(content)
#     # return jsonify({'label': 'test'})

# def call_llm(content):
#     return "Processed: " + content

# if __name__ == '__main__':
#     app.run(debug=True)

# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

import nltk 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 

import os
from litellm import completion
import json


app = Flask(__name__)
CORS(app, resources={r"/process": {"origins": "*"}})  # Explicitly setting CORS for the process route

@app.route('/')
def hello_world():
	return 'Hello World'


@app.route('/process', methods=['POST']) # Specific route CORS enablement
def process_data():
    # content = request.json['content']
    # print("Received content:", content)

    try:
        # Extract content sent from the client
        content = request.json['content']
		
        if len(content) == 22:
            print("empty string : --->",content)
        else:
            print("Received content:",len(content))  # Log the received content

        # Process the content using a simulated LLM function
        if len(content)!=22:
            response = call_llm(content)
            with open("example.txt", "w") as file:
                file.write(response)
        # print(label_history)
        # print(len(content))
        elif len(content) == 22:
            print('inside')
            # response = label_history[0]
            with open("example.txt", "r") as file:
                file_contents = file.read()
            print(file_contents)
            response = file_contents
            with open("example.txt", "w") as file:
                file.write("")
				
        print("Response from LLM:", response)  # Log the LLM response
        # response = "Worked!"
        # Return the processed response as JSON
        return jsonify({'label': response})

    except Exception as e:
        print("Error handling request:", str(e))  # Log any errors
        return jsonify({'error': str(e)}), 500

    # try:
    #     content = request.json['content']
    #     print(content) 
    #     response = "Sample"
    #     return jsonify({'label': response}), 200, {'Access-Control-Allow-Origin': '*'}
    # except Exception as e:
    #     return jsonify({'error': str(e)}), 500, {'Access-Control-Allow-Origin': '*'}


def summarize(text):
# Tokenizing the text 
	stopWords = set(stopwords.words("english")) 
	words = word_tokenize(text) 

	# Creating a frequency table to keep the 
	# score of each word 

	freqTable = dict() 
	for word in words: 
		word = word.lower() 
		if word in stopWords: 
			continue
		if word in freqTable: 
			freqTable[word] += 1
		else: 
			freqTable[word] = 1

	# Creating a dictionary to keep the score 
	# of each sentence 
	sentences = sent_tokenize(text) 
	sentenceValue = dict() 

	for sentence in sentences: 
		for word, freq in freqTable.items(): 
			if word in sentence.lower(): 
				if sentence in sentenceValue: 
					sentenceValue[sentence] += freq 
				else: 
					sentenceValue[sentence] = freq 



	sumValues = 0
	for sentence in sentenceValue: 
		sumValues += sentenceValue[sentence] 

	# Average value of a sentence from the original text 

	average = int(sumValues / len(sentenceValue)) 

	# Storing sentences into our summary. 
	summary = '' 
	for sentence in sentences: 
		if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)): 
			summary += " " + sentence 
	# print(summary)
	return summary

def call_llm(content):
    # Simulated LLM processing
    website_cleaned_data = summarize(content)
	
    # print(website_cleaned_data)
	
    ## set ENV variables
    os.environ["COHERE_API_KEY"] = "nc8lMiK9Sw6sb5JDy14W1rCYGmKV1eN7wCbC0Iah"

    # raw_data = ""
    # summarize website data here :

    # website_cleaned_data = "Speaking of RCB's innings, they seemed to be heading towards self-destruction halfway through. However, a spectacular fifty by captain Faf propelled them to a four-wicket victory over GT. Du Plessis scored 64 off 23 balls with 10 fours and 3 sixes while Virat Kohli scored 42 off 27 balls with 2 fours and 4 sixes. They both added 92 runs in just 35 balls for the opening wicket. Moreover, RCB skipper and former South African batter Faf Du Plessis also completed 10,000 runs in T20 cricket, becoming the 14th player to do so. In 369 games, Du Plessis has scored 10,039 runs at an average of 32.27, with five centuries and 67 fifties. His best score is 120*."

    category_list =['Adult', 'Business/Corporate', 'Computers and Technology', 'E-Commerce',
        'Education', 'Food', 'Forums', 'Games', 'Health and Fitness',
        'Law and Government', 'News', 'Photography',
        'Social Networking and Messaging', 'Sports', 'Streaming Services',
        'Travel', 'Sciences','Education' ]

    text = f'''"Can you go over this text : {website_cleaned_data} \
        Can you categorize this into these following categories : {category_list} . Answer only within these options. Answer only in 1 word - category name"'''

    # print(text)

    # cohere call
    response = completion(
        model="command-r", 
        messages = [{ "content": text,"role": "user"}]
    )
    # print('``````````````````````````````````````````````````````````')
    ans = response['choices'][0]['message']['content']
    # print(ans)
	# ans --> category (1 word ans)
	
    return ans

if __name__ == '__main__':
	app.run(debug=True, port=5001)
