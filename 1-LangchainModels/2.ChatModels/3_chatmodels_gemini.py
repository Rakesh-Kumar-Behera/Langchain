from langchain_google_genai import ChatGoogleGenAI
from dotenv import load_dotenv # Load environment variables (secret keys) from .env file

load_dotenv() # Load environment variables from .env file

model = ChatGoogleGenAI(model = 'gemini-1.5-pro') # temperature parameter indicates the creativity level of the model.

result = model.invoke("What is the capital of India") # Invoke the model with a prompt
print(result.content) # Print the result content to the console