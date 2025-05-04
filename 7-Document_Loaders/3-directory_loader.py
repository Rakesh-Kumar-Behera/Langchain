from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader

loader = DirectoryLoader(
    path="books",
    glob="*.pdf",
    loader_cls=PyPDFLoader,
)

docs = loader.load()

print(len(docs))  # Print the number of loaded documents

# for first pdf ka first page
print(docs[0].page_content)  # Print the content of the first loaded document to the console
print(docs[0].metadata)  # Print the metadata of the first loaded document to the console

# load vs lazy_load
# docs = loader.lazy_load() #` lazy_load() returns a generator object`, it is used when the document size is large and you want to load the documents one by one instead of loading all the documents at once.
# docs = loader.load() #` load() returns a list of documents`, it is used when the document size is small and you want to load all the documents at once.