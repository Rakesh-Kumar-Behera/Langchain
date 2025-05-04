# ChatModel using Hugging Face api
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv # Load environment variables (secret keys) from .env file

load_dotenv() # Load environment variables from .env file

# HuggingFaceEndpoint
llm = HuggingFaceEndpoint(
    repo_id= "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)

model = ChatHuggingFace(llm = llm)

result = model.invoke("What is the capital of India?") # Invoke the model with a prompt
print(result.content) # Print the result content to the console