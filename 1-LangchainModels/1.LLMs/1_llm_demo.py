from langchain_openai import OpenAI
from dotenv import load_dotenv # Load environment variables (secret keys) from .env file

load_dotenv() # Load environment variables from .env file

llm = OpenAI(model = 'gpt-3.5-turbo-instruct') 

result = llm.invoke("What is the capital of France?")
# Output: 'Paris'   

print(result) # Print the result to the console
# Output: 'Paris'

# LLMs takes string as an input and returns string as output.
# LLMs are used for text generation, text completion, and other tasks that require understanding and generating human-like text.
# now days LLMs are kind of depricated, it was used previously but now everyone prefers chatModels.