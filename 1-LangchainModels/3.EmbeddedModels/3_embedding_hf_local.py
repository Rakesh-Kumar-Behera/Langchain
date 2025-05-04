from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv # Load environment variables (secret keys) from .env file


embedding = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")

text = "Delhi is the capital of India"

vector = embedding.embed_query(text)# Invoke the model with a prompt
print(str(vector)) # Print the result content to the console 