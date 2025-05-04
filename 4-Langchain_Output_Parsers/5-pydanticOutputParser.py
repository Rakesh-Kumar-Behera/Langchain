from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field


load_dotenv()

# Correct usage for text-generation models
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task = "text-generation"
)


model = ChatHuggingFace(llm = llm)

class Person(BaseModel):
    name: str = Field(description="Name of the person")
    age: int = Field(gt=18, description="Age of the person")
    city: str = Field(description="City of the person belongs to")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="Give me the name, age, and city of a fictional {place} person \n {format_instruction}",
    input_variables=['place'],
    partial_variables= {'format_instruction': parser.get_format_instructions()}
)

# prompt = template.invoke({"place": "Indian"})
# result = model.invoke(prompt)

# final_result = parser.parse(result.content)
# print(final_result) # Print the result content to the console

# using chain
chain = template | model | parser
chain_result = chain.invoke({"place": "Italian"})
print(chain_result) # Print the result content to the console