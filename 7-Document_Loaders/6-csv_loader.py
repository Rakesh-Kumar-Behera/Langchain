from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(
    file_path="insurance.csv",
)

data = loader.load()

print(len(data))  # Print the number of loaded documents
print(data[0])  # Print the loaded documents

# CSVLoader is used to load CSV files and convert them into a list of documents.
# CSVLoader har row ke liye ek document create karta hai.
# CSVLoader ko use karne ke liye aapko file_path dena hota hai jahan par aapka CSV file hai.