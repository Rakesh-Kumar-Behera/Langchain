from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel

load_dotenv()

prompt1 = PromptTemplate(
    template="Generate a tweet about {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Generate a Linkedin post about {topic}",
    input_variables=["topic"]
)

parser = StrOutputParser()

model = ChatOpenAI()

parallel_chain = RunnableParallel({
    'tweet':RunnableSequence(prompt1, model, parser),
    'linkedin':RunnableSequence(prompt2, model, parser)}
)

result = parallel_chain.invoke({"topic": "AI"})

print(result)

# tweet
print("Tweet: ", result['tweet'])  # Print the result content to the console
# linkedin
print("Linkedin: ", result['linkedin'])  # Print the result content to the console