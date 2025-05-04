from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv # Load environment variables (secret keys) from .env file
import os

os.environ['HF_HOME'] = 'D:/huggingface_cache' # Set the HF_HOME environment variable to the desired path
#to store the model in D drive

llm = HuggingFacePipeline.from_model_id(
    model_id= "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    model_kwargs={
        "temperature": 0.5, 
        "max_length": 100
        }
)
model = ChatHuggingFace(llm = llm)

result = model.invoke("What is the capital of India?") # Invoke the model with a prompt
print(result.content) # Print the result content to the console 