import os
from dotenv import load_dotenv
import google.generativeai as gen_ai

# Load environment variables
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Set up Google Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')


# Function to start a chat session
def start_chat():
  chat_session = model.start_chat(history=[])
  return chat_session


# Function to process user input and get response
def get_response(user_prompt, chat_session):
  # Send user's message to Gemini-Pro and get the response
  gemini_response = chat_session.send_message(user_prompt)
  return gemini_response.text


# Initialize chat session
chat_session = start_chat()

# Main loop for conversation
while True:
  # Get user input
  user_prompt = input("You: ")

  # Get response from Gemini-Pro
  response = get_response(user_prompt, chat_session)

  # Print Gemini-Pro's response
  print(f"Gemini-Pro: {response}")

  # Exit loop on specific command (optional)
  if user_prompt.lower() == "quit":
    break
