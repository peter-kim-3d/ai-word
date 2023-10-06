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
    response = chat_model.predict(f"Give me {count} frequently used words starting with the letter {letter}")
    return response

def get_word_definition(word):
    """Fetch the definition of a word using langchain."""
    # Mock-up; replace with actual method call
    response = chat_model.predict(f"What is the definition of {word}?")
    return response

if len(letter) == 1:
    if st.button('Generate Words'):
        with st.spinner('Fetching words...'):
            words = get_frequent_words(letter, count)
            
            for word in words:
                col1, col2 = st.beta_columns(2)
                col1.write(word)
                if col2.button(f"Meaning of {word}"):
                    definition = get_word_definition(word)
                    st.write(f"Definition of {word}: {definition}")
else:
    st.write("Please input a single letter.")

