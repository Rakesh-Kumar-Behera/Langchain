from langchain_community.document_loaders import WebBaseLoader

url = "https://www.flipkart.com/apple-macbook-air-m4-16-gb-256-gb-ssd-macos-sequoia-mw0y3hn-a/p/itmad81d112ad068?pid=COMH9ZWQXZHDDRGZ&lid=LSTCOMH9ZWQXZHDDRGZAMRGTN&marketplace=FLIPKART&q=macbook%20air%20m4&sattr[]=color&sattr[]=system_memory&sattr[]=ssd_capacity&sattr[]=screen_size&st=screen_size&otracker=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na"

loader = WebBaseLoader(url)

docs = loader.load()  # Load the document from the URL

print(len(docs))

print(docs[0].page_content)  # Print the content of the first loaded document to the console    

# returns only 1 document for one url
# we can pass multiple urls in the list to load multiple documents at once
# loader = WebBaseLoader([url1, url2, url3])
# it will return a list of documents for each url