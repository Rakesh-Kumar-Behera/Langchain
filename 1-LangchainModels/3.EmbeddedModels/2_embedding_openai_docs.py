from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv # Load environment variables (secret keys) from .env file

load_dotenv()

embedding = OpenAIEmbeddings(model= 'text-embedding-3-large', dimensions = 32)

document = {
    "Delhi is the capital of India",
    "Bhubaneswar is the capital of Odisha",
    "Paris is the capital of France"
}
result = embedding.embed_documents(document)
print(str(result)) # Print the result content to the console