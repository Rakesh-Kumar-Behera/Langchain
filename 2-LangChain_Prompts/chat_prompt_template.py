# Prompt template for Dynamic Message where the user sends a list of messages as input
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

chat_template = ChatPromptTemplate([
    ('system', "You are a helpful {domain} expert."),
    ('human', "Explain in simple terms, What is {topic}"),
    
])

prompt = chat_template.invoke({'domain': 'Cricket', 'topic': 'DRS'})

print(prompt)

# Message Placeholder
# A Message Placeholder is a special type of placeholder that can be used to represent a message in a prompt template.
# It allows you to specify the type of message (e.g., system, user, assistant) and the content of the message. 
# This is useful when you want to create a prompt template that includes multiple messages or when you want to customize the content of a message based on user input.
# In LangChain, you can create a Message Placeholder using the MessagePlaceholder class. This class allows you to define the type of message and its content, and it can be used in conjunction with other prompt templates to create complex prompts.