# from dotenv import load_dotenv
# load_dotenv()

import streamlit as st
from langchain.chat_models import ChatOpenAI

chat_model = ChatOpenAI()

st.title('Frequent Word Generator')

# User inputs
letter = st.text_input('Enter a letter', max_chars=1)
count = st.slider('Number of words', min_value=1, max_value=50, value=10)

def get_frequent_words(letter, count):
    """Return frequently used words starting with a given letter using langchain."""
    # This is a mock-up. You'll need to replace this with an actual method call to langchain.
    response = chat_model.predict(f"Give me {count} frequently used words starting with the letter {letter}")
    # Assuming the response is a list of words, otherwise you might need to process it
    return response

if len(letter) == 1:
    if st.button('Generate Words'):
        with st.spinner('Fetching words...'):
            words = get_frequent_words(letter, count)
            st.write(words)
else:
    st.write("Please input a single letter.")
