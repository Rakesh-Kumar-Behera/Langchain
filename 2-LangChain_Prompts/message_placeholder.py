from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage


# chat template
chat_template = ChatPromptTemplate([
    ('system', "You are a helpful customer support agent."),
    MessagesPlaceholder(variable_name = 'chat_history'),  # Placeholder for chat history
    ('human', "{query}"),
  
    # MessagePlaceholder('assistant_message')  # Placeholder for assistant message
])

chat_history = []
# load chat history
with open('chat_history.txt') as file:
    chat_history.extend(file.readlines())
print(chat_history)

# create prompt 
prompt = chat_template.invoke({'query': 'What is the status of my order?', 'chat_history': chat_history})
print(prompt)