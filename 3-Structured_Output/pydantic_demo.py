from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional

class Student(BaseModel):
    name: str = "John Doe"  # Default value
    age: int = Field(gt=0, lt=25)  # Field with a constraint (greater than 0 and less than 25)
    blood_groop: Optional[str] = None  # Optional field with default value None
    # You can also add validation methods if needed
    grade: float = Field(gt=0, lt=10, default= 5.0, description= "A decimal value representing the cgpa of the student")  # Field with a constraint (greater than 0 and less than 10)
    email: EmailStr  # Example of a field with a specific type (email), automatically validated
    # phone: Optional[str] = Field(regex=r'^\+?[1-9]\d{1,14}$')  # Example of a field with a regex pattern for phone numbers
    # Example of a custom validator

# new_student = {'name':'Alice', 'age':20, 'grade':8.8}
student1 = Student(name='Alice', age=20, grade=8.8,email= "xyz@email.com")

student = Student(**student1) # ** unpacks the dictionary into keyword arguments

# student_dict = student.dict()  # Convert the Pydantic model to a dictionary
student_dict = student.model_dump()

student_json= student.model_dump_json()

print(student_dict)  # Output: {'name': 'Alice', 'age': 20, 'blood_groop': None, 'grade': 8.8, 'email': '
# print(student)  # Output: name='Alice' age=20 grade=8.8

# print(type(student))  # Output: <class '__main__.Student'>


    
