# This is a code snippet of Static Prompt that uses LangChain to create a prompt UI for summarizing text.
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.header("LangChain Prompt UI")
st.subheader("Reasearch Tool")

user_input = st.text_input("Enter your prompt: ")

if st.button("Summarize"):
    # st.text("Some random text")
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7, max_tokens=1500)
    response = llm(user_input)
    st.write("Response:")
    st.text(response.content)