from langchain.text_splitter import CharacterTextSplitter

text = """Large language models (LLMs) have revolutionized natural language processing (NLP), enabling various applications, from conversational assistants to content generation and analysis. However, working with LLMs can be challenging, requiring developers to navigate complex prompting, data integration, and memory management tasks. This is where LangChain comes into play, a powerful open-source Python framework designed to simplify the development of LLM-powered applications.

LangChain addresses the difficulties of building sophisticated LLM applications by providing modular, easy-to-use components for connecting language models with external data sources and services. It abstracts away the complexities of LLM integration, enabling developers to focus on building impactful applications that leverage the full potential of these advanced language models.

As the importance of LLMs continues to grow in various domains, LangChain plays a crucial role in democratizing their use and empowering developers to create innovative solutions that can transform industries.
"""

splitter = CharacterTextSplitter(
    separator="",
    chunk_size=100,
    chunk_overlap=0
)

result = splitter.split_text(text)

print(len(result))  # Print the number of chunks created
print(result)  # Print the result content to the console