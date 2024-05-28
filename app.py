import google.generativeai as genai
import os
from flask import Flask, Response,request,jsonify

app = Flask(__name__)

# Initialize Gemini model and chat

genai.configure(api_key="AIzaSyDLcu2dQoNJB18Vx8J_N8xBGbss05Rxblw")
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

# Function to get Gemini's response


def get_gemini_response(question):
    global chat
    response = chat.send_message(question)
    return response.text

# Function to handle user input and display Gemini's response


@app.route('/convo', methods=['GET','POST'])
def initialize():
    if request.method == 'GET':

        print("Gemini LLM Application")
        print("======================")
        chat.send_message("""
                        Act like a paragraph summarizer for news given below
                        """)
       
        return "ready"

    if request.method == 'POST':
        user_message = request.json['input_question']
        print(user_message)
        response = get_gemini_response(user_message)
        output = jsonify(response)
        return output


if __name__ == "__main__":
    app.run(debug=True)
