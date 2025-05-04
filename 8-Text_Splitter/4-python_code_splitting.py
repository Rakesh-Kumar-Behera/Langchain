from langchain.text_splitter import RecursiveCharacterTextSplitter,Language

text = """
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # Grade is assumed to be on a 10.0 scale

    def get_details(self):
        return self.name

    def has_passed(self):
        return self.grade > 6.0


# Create an object of the Student class
student1 = Student("Anjali", 19, 7.5)

# Use get_details method
name = student1.get_details()
print(f"Student Name: {name}")

# Use has_passed method with if-else
if student1.has_passed():
    print(f"{name} has passed.")
else:
    print(f"{name} has failed.")
"""

# Initialize the text splitter
splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=300,
    chunk_overlap=0
)

chunks = splitter.split_text(text)

print(len(chunks))  # Print the number of chunks created
print(chunks[0])  # Print the result content to the console
# output the first chunk
# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade  # Grade is assumed to be on a 10.0 scale

#     def get_details(self):
#         return self.name

#     def has_passed(self):
#         return self.grade > 6.0