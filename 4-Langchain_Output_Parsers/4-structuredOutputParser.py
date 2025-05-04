# from langchain_huggingface import HuggingFaceHub
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

# Correct usage for text-generation models
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task = "text-generation"
)


model = ChatHuggingFace(llm = llm)

schema = [
    ResponseSchema(name='fact_1', description='Fact 1 about the topic'),
    ResponseSchema(name='fact_2', description='Fact 2 about the topic'),
    ResponseSchema(name='fact_3', description='Fact 3 about the topic'),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template="Give me 3 facts about {topic} \n{format_instruction}",
    input_variables=["topic"],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

# prompt = template.invoke({"topic": "Black hole"})
# result = model.invoke(prompt)
# final_result = parser.parse(result.content)
# print(final_result)

# using chain
chain = template | model | parser
chain_result = chain.invoke({"topic": "Black hole"})
print(chain_result) # Print the result content to the console






# Option 2: Use Chat-optimized Model Instead
# If you must use ChatHuggingFace, choose a model that supports chat APIs — such as:

# meta-llama/Meta-Llama-3-8B-Instruct

# tiiuae/falcon-7b-instruct

# HuggingFaceH4/zephyr-7b-beta