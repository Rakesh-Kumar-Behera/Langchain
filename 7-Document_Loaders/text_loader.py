from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

prompt = PromptTemplate(
    template="Write a summary of the following topic \n {topic}",
    input_variables=["topic"]
)



loader = TextLoader("sample.txt", encoding="utf-8")
# loader = TextLoader("sample.txt", encoding="utf-8", metadata={"source": "sample.txt"})    

documents = loader.load()

# print(documents)  # Print the loaded documents 
# print(type(documents))  # Print the type of the loaded documents # list type
# print(len(documents))  # Print the number of loaded documents 
# print(documents[0])  # Print the first loaded document # Document object
# print(type(documents[0]))  # Print the type of the first loaded document  # document

print(documents[0].page_content)  # Print the content of the first loaded document to the console
print(documents[0].metadata)  # Print the metadata of the first loaded document to the console

chain = prompt | model | parser

result = chain.invoke({"topic": documents[0].page_content})
print("Generated Summary: ", result)  # Print the result content to the console