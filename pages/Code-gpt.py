
import streamlit as st
import google.generativeai as genai


def generate_response(question):
    genai.configure(api_key="AIzaSyBCjsa0d1qUbfgvIRJQZc4VM2FPEh4leK0")

    # Create the model
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
    )

    chat_session = model.start_chat(
    history=[
    ]
    )

    response = chat_session.send_message(f'''You are a professional coder and can provide efficient coding solutions to any coding
                                         problem. Genarate code for the given question : {question}. Strictly ensure that 
                                         you provide only the code. dont send any additional information or text or quotes.
                                         Just provide code only.''')

    yield response.text


st.title("Welcome to Code-gpt")

data = st.chat_input("Enter prompt")
user = "user"
bot = "assistant"
chats = "chats"

if chats not in st.session_state:
    st.session_state[chats] = ["Hi! How can I help you ?"]

for i,chat in enumerate(st.session_state[chats]):
    if i%2 == 0:
        st.chat_message(bot).write(chat)
    else:
        st.chat_message(user).write(chat)

if(data):
    st.session_state[chats].append(data)
    st.chat_message(user).write(data)
    reply = generate_response(data)
    st.session_state[chats].append(reply)
    st.chat_message(bot).write_stream(reply)

