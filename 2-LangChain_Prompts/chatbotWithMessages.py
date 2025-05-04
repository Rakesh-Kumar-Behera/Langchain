from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

model = ChatOpenAI()

chat_history = [
    SystemMessage(content="You are a helpful assistant.")
]

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    chat_history.append(HumanMessage(content=user_input))  # Append the user input to the chat history
    response = model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))  # Append the model response to the chat history
    print("AI: ", response.content)

print(chat_history)