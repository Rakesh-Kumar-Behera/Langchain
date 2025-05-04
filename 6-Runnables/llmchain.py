from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

# load the LLM (GPT-3.5)
llm = OpenAI(model="gpt-3.5-turbo", temperature=0.7)



# create a Prompt template
prompt = PromptTemplate(
    template="Suggest a catchy blog title about {topic}",
    input_variables=["topic"]
)

# create an LLMChain
chain = LLMChain(llm=llm, prompt=prompt)

# Run the chain with a specific topic
topic = input("Enter a topic: ")
result = chain.run(topic=topic)
print("Generated Blog Title: ",result)  # Print the result content to the console
