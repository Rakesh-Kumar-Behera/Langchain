from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv # Load environment variables (secret keys) from .env file
# import os

load_dotenv() # Load environment variables from .env file
# os.environ['ANTHROPIC_API_KEY'] = 'your_anthropic_api_key' # Set the ANTHROPIC_API_KEY environment variable


model = ChatAnthropic(model = 'claude-3-5-sonnet-20241022') # temperature parameter indicates the creativity level of the model.
# Higher temperature means more creative and diverse responses, while lower temperature means more focused and deterministic responses.

result = model.invoke("Give me 5 names of indian food") # Invoke the model with a prompt
print(result.content)