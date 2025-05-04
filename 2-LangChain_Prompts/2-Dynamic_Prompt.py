from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
#for prompt template
from langchain_core.prompts import PromptTemplate

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

# if st.button("Summarize"):
#     # Construct the prompt dynamically based on user input
#     prompt = f"Explain the research paper '{selected_paper}' in a {selected_style} style with a {input_length}."
#     st.write("Prompt:")
#     st.write(prompt)
#     response = model(prompt)
#     st.write("Response:")
#     st.write(response.content)

template = PromptTemplate(
    template= """Please summarize the research paper titled "{selected_paper}" with the following 
specifications: 
Explanation Style: {selected_style} 
Explanation Length: {selected_input_length} 
1. Mathematical Details: 
- Include relevant mathematical equations if present in the paper. 
- Explain the mathematical concepts using simple, intuitive code snippets where applicable. 
2. Analogies: 
-Use relatable analogies to simplify complex ideas. 
If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing. 
Ensure the summary is clear, accurate, and aligned with the provided style and length.
""",
    input_variables=["selected_paper", "selected_style", "selected_input_length"],
    # validate_template=True, # Ensure the template is valid, or the variables are correctly set
)

prompt = template.invoke({
    'selected_paper':selected_paper, 
    'selected_style':selected_style, 
    'selected_input_length':selected_input_length
})

if st.button("Summarize"):
    response = model(prompt)
    st.write("Response:")
    st.write(response.content)