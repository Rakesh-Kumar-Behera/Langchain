from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough, RunnableSequence, RunnableParallel

load_dotenv()


prompt1 = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=["topic"]
)

model = ChatOpenAI()

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template="Explain the following joke - {text}",
    input_variables=["text"]
)

joke_generator_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explanation': RunnableSequence(prompt2, model, parser)}
)

final_chain = RunnableSequence(joke_generator_chain, parallel_chain)
result = final_chain.invoke({"topic": "cricket"})

# print(result)  # Print the result content to the console as a dictionary
print("Generated Joke: ", result['joke'])  # Print the result content to the console
print("Joke Explanation: ", result['explanation'])  # Print the result content to the console   
















# passthrough = RunnablePassthrough()

# print(passthrough.invoke("Hello World!"))  # Print the result content to the console
# jo usse input milta hai as it is output deta hai
# print(passthrough.invoke({"topic": "cats"}))  # Print the result content to the console