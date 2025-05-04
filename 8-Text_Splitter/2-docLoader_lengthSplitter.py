from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("..//7-Document_Loaders/Data Science Interview Questions-3.pdf")

docs = loader.load()  # Load the document from the PDF file

splitter = CharacterTextSplitter(
    separator="",
    chunk_size=100,
    chunk_overlap=0 
)

result = splitter.split_documents(docs)

print(len(result))  # Print the number of chunks created

# print(result)  # Print the result content to the console

# print tht first chunk
print(result[0].page_content)  # Print the content of the first loaded document to the console


