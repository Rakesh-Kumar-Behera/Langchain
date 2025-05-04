# fetching the prompt template from the Prompt Generator file
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
#for prompt template
from langchain_core.prompts import PromptTemplate, load_prompt
# from prompt_generator import template

load_dotenv()

# Streamlit UI
st.header("LangChain Dynamic Prompt UI")
st.subheader("Research Tool")

# Dropdown for selecting a research paper
paper_options = [
    "Select ....",
    "Attention is all you need",
    "BERT: pre-training of Deep Bidirectional Transformers",
    "GPT-3: Language Models are Few Shot Learners",
    "Diffusion Models beat GANs on Image Synthesis"
]
selected_paper = st.selectbox("Select a Research Paper:", paper_options)

# Dropdown for selecting explanation style
style_options = [
    "Beginner_friendly",
    "Technical",
    "Mathematical",
    "Code-Oriented"
]
selected_style = st.selectbox("Select the Explanation Style:", style_options)

input_length = [
    "Short (1-2 paragraphs)",
    "Medium (3-5 paragraphs)",
    "Long (detailed explanation)",
]
selected_input_length = st.selectbox("Select the Explanation Length:", input_length)



model = ChatOpenAI()

template = load_prompt("prompt_template.json") # Load the prompt template from the file

prompt = template.invoke({
    'selected_paper':selected_paper, 
    'selected_style':selected_style, 
    'selected_input_length':selected_input_length
})

if st.button("Summarize"):
    response = model.invoke(prompt)
    st.write("Response:")
    st.write(response.content)