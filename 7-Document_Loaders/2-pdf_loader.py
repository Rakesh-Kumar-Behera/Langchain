## Using PyPDF Loader
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

loader = PyPDFLoader("Data Science Interview Questions-3.pdf")

docs = loader.load()

print(docs)  # Print the loaded documents
print(type(docs))  # Print the type of the loaded documents # list type
print(len(docs))  # Print the number of loaded documents

print(docs[0].page_content)
print(docs[1].metadata)  # Print the metadata of the first loaded document to the console