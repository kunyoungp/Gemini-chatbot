import os
from dotenv import load_dotenv, find_dotenv
import google.generativeai as genai

#load env
_ = load_dotenv(find_dotenv())

#insert your GEMINI_API_KEY in .env
genai.configure(api_key = os.environ.get('GEMINI_API_KEY'))

gen_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048
}

model = genai.GenerativeModel(model_name = "gemini-1.0-pro",
                              generation_config = gen_config)

#call gemini response
def chat_with_bot(prompt):
    convo = model.start_chat(history=[])
    convo.send_message(prompt)

    return convo.last

#image describe gemini response
def describe_image(data, prompt):

    response = model.generate_content([data, prompt])

    return response