from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

# while True:
#     user_input = input("You: ")
#     if user_input.lower() == 'exit':
#         break
#     response = model.invoke(user_input)
#     print("AI: ",response.content)  # this codes doesnt save the chat history, so it will not be able to remember the previous conversation. So if you want to ask any question related to the previous conversation, it will not be able to answer that.
# for example: you: which number is greater 2 or 7
# AI: 7 is greater than 2
# you: now multiply the greater number with 10
# AI: lets say the greater number is x, so x*10 =  10x

chat_history = []
# # This will be used to store the chat history and pass it to the model for context.
# # This will help the model to remember the previous conversation and answer the questions related to that.

while True:
    user_input = input("You: ")
    chat_history.append(user_input)  # Append the user input to the chat history
    if user_input.lower() == 'exit':
        break
    response = model.invoke(chat_history)
    # Pass the chat history to the model for context
    chat_history.append(response.content)  # Append the model response to the chat history
    print("AI: ",response.content)

print("Chat History:",chat_history)


# You: hi
# AI:  Hello! How can I assist you today?
# You: which number is greater 5 or 9
# AI:  9 is greater than 5.
# You: now give me the square of greater value
# AI:  The square of 9 is 81.
# You: what is the cube of smaller value
# AI:  The cube of 5 is 125.
# You: exit

# Chat History:
# hi
# Hello! How can I assist you today?
# which number is greater 5 or 9
# 9 is greater than 5.
# now give me the square of greater value
# The square of 9 is 81.
# what is the cube of smaller value
# The cube of 5 is 125.
# exit

# Notes:
# so if we look at the chat history,we can see that it has all the messages in the chat history. but it is not in the format of a conversation. 
# so as the length of the conversation increases, it will be difficult to read the chat history.and the model will not able to distinguish between the user input and the model response.
# and this will create a problem in the future if we want to save the chat history in a file or database.
# so we need to save the chat history in a better format. so we can use a dictionary to save the chat history in a better format.