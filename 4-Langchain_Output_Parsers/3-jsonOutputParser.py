# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

# # Initialize the Hugging Face endpoint
# llm = HuggingFaceEndpoint(
#     repo_id="google/gemma-2-2b-it",  # reliable open-source LLM
#     task="text-generation"     # Correct task for text generation
# )


# model = ChatHuggingFace(llm = llm)
model = ChatOpenAI()

parser = JsonOutputParser()


template = PromptTemplate(
    template = "Give me the name, age, and city of a fictional person \n {format_instruction}",
    input_variables = [],
    partial_variables= {'format_instruction': parser.get_format_instructions()}
)

# prompt = template.format()

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

# using chain
chain = template | model | parser
chain_result = chain.invoke({})

print(chain_result) # Print the result content to the console