from langchain.text_splitter import RecursiveCharacterTextSplitter,Language

text  = """
# # Markdown Text Example
# My Learning Plan

## 🧠 Topics to Study
Here are the key areas I want to focus on:

- **Python Programming**
  - Data types
  - Functions
  - Object-Oriented Programming
- **Data Science**
  - Pandas
  - NumPy
  - Data Visualization
- **Machine Learning**
  - Supervised Learning
  - Unsupervised Learning

## ✅ Resources I Use

- [W3Schools - Python](https://www.w3schools.com/python/)
- [Kaggle - Learn Data Science](https://www.kaggle.com/learn)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)
- [LangChain Documentation](https://docs.langchain.com/)

## 📅 Weekly Goals

- [x] Complete Python basics
- [ ] Practice 3 Data Science projects
- [ ] Finish 5 chapters of Machine Learning

## 💡 Quote

> “The expert in anything was once a beginner.” – Helen Hayes

 """


# Initialize the text splitter
splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN,
    chunk_size=400,
    chunk_overlap=0
)

chunks = splitter.split_text(text)

print(len(chunks))  # Print the number of chunks created
print('chunk1',chunks[0])  # Print the result content to the console
print('chunk2',chunks[1])  # Print the result content to the console