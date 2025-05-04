from langchain.schema.runnable import RunnableLambda, RunnablePassthrough, RunnableSequence, RunnableParallel
from langchain_openai import ChatOpenAI

def word_counter(text: str) -> int:
    """Count the number of words in a text."""
    return len(text.split())

runnable_word_counter = RunnableLambda(word_counter)

print(runnable_word_counter.invoke("This is a test sentence."))  # Print the result content to the console