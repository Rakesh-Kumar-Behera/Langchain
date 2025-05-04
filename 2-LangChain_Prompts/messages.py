from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="What is Langchain"),
]

response = model.invoke(messages)
messages.append(AIMessage(content=response.content))

print(messages)

# System message is a special type of message that is used to set the behavior of the assistant. It is usually used to provide context or instructions to the assistant.
# It is not a part of the conversation and is not meant to be seen by the user. It is used to set the tone and style of the conversation.
# The system message is usually passed in as the first of a sequence of input messages.

# Human Message is a message that is sent by the user. It is the input message that the assistant will respond to. It is usually the last message in a sequence of input messages.
# It is the message that the user wants the assistant to respond to. It is usually a question or a request for information.

# AI Message is a message that is sent by the assistant. It is the output message that the assistant will respond to. It is usually the last message in a sequence of input messages.
# It is the message that the assistant will respond to. It is usually a response to a question or a request for information.