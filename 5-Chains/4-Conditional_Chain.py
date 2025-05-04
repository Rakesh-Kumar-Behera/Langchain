from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda # RunnableParallel is used to run multiple chains in parallel
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal


load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(description="Sentiment of the feedback")
    
parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template = "Classify the sentiment of the following feedback text into positive or negative \n {feedback} \n {format_instruction}",
    input_variables = ["feedback"],
    partial_variables= {'format_instruction': parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
    template= 'write an appropriate response to this positive feedback \n {feedback}',
    input_variables = ["feedback"]
)

prompt3 = PromptTemplate(
    template= 'write an appropriate response to this negative feedback \n {feedback}',
    input_variables = ["feedback"]
)

branch_chain = RunnableBranch(
    (lambda x: x.sentiment == "positive", prompt2 | model | parser),
    (lambda x: x.sentiment == "negative", prompt3 | model | parser),
    RunnableLambda(lambda x: "Could not find sentiment") # RunnableLambda converts a lambda function into a runnable chain
)


chain = classifier_chain | branch_chain # Combine the classifier chain and the branch chain

result = chain.invoke({"feedback": "This is a wonderful smartphone"}) # Invoke the chain with feedback text

print(result) # Print the result content to the console

chain.get_graph().print_ascii() # Print the chain graph to the console

# result = classifier_chain.invoke({"feedback": "This is a terrible smartphone"}).sentiment # Invoke the classifier chain with feedback text

# print(result) # Print the result content to the console

# branch_chain = RunnableBranch(
#     (condition1, chain1),
#     (condition2, chain2),
#     default chain)

# negative Feedback - I'm sorry to hear that you had a negative experience. We strive to provide exceptional service and we value your feedback. Please let us know how we can improve and make things right for you. Thank you for bringing this to our attention.