from langchain_openai import ChatOpenAI
from dotenv import load_dotenv # Load environment variables (secret keys) from .env file

load_dotenv() # Load environment variables from .env file

model = ChatOpenAI(model = 'gpt-4', temperature = 1.2, max_completion_tokens= 20) # temperature parameter indicates the creativity level of the model. 
# Higher temperature means more creative and diverse responses, while lower temperature means more focused and deterministic responses.

result = model.invoke("Give me 5 names of indian food") # Invoke the model with a prompt
# print(result) # Print the result to the console, with other metadata
print(result.content) # Print the result content to the console