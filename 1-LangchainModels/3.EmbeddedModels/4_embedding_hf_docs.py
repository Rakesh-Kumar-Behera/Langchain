from langchain_huggingface import HuggingFaceEmbeddings 
from dotenv import load_dotenv

load_dotenv()

embedding = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")

document = {
    "Delhi is the capital of India",
    "Bhubaneswar is the capital of Odisha",
    "Paris is the capital of France"
}

vectors = embedding.embed_documents(document)
print(vectors)