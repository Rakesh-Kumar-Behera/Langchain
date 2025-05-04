from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int
    
new_person: Person = {
    'name': 'Alice',
    'age': 30
}

print(new_person)  # Output: {'name': 'Alice', 'age': 30}
# TypedDict is a way to define a dictionary with specific keys and value types. It is useful for creating structured data types in Python, especially when working with APIs or data serialization.