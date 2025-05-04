from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

prompt = PromptTemplate(
    template="Answer the following question \n {question} from the following text \n {text}",
    input_variables=["question", "text"]
)


url = "https://www.flipkart.com/apple-macbook-air-m4-16-gb-256-gb-ssd-macos-sequoia-mw0y3hn-a/p/itmad81d112ad068?pid=COMH9ZWQXZHDDRGZ&lid=LSTCOMH9ZWQXZHDDRGZAMRGTN&marketplace=FLIPKART&q=macbook%20air%20m4&sattr[]=color&sattr[]=system_memory&sattr[]=ssd_capacity&sattr[]=screen_size&st=screen_size&otracker=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na"

loader = WebBaseLoader(url)

docs = loader.load()  # Load the document from the URL

chain = prompt | model | parser

result = chain.invoke({"question": "What is the price of the product? and what are the exciting new features of the product", "text": docs[0].page_content})
print("Generated Answer: ", result)  # Print the result content to the console

# print(len(docs))

# print(docs[0].page_content)

# USER_AGENT environment variable not set, consider setting it to identify your requests.
# Generated Answer:  The price of the product is Rs. 89,990, with an original price of Rs. 99,900, giving a discount of 9%. 

# The exciting new features of the product are:
# - Stylish & Portable Thin and Light Laptop
# - 13.6 inch Liquid Retina Display with a Native Resolution at 224 Pixels Per Inch, 500 Nits Brightness, Wide color (P3)
# - Easy Payment Options including EMI starting from ₹3,164/month, Cash on Delivery, Net banking & Credit/ Debit/ ATM card
# - 16 GB RAM
# - 256 GB SSD
# - macOS Sequoia operating system
# - 30W USB-C Power Adapter
# - Wi-Fi 6E (802.11ax) connectivity
# - Backlit Magic Keyboard
# - Force Touch Trackpad
# - 12MP Center Stage Camera with Support for Desk View, 1080p HD Video Recording
# - 53.8 Whr Lithium Polymer Battery
# - 1 Year Limited Warranty