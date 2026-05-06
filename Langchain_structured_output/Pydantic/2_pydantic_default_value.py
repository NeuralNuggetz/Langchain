from pydantic import BaseModel

class Student(BaseModel):
    name: str = "sennsay"

# Creating an instance of the Student class
new_student = {} 

student = Student(**new_student)

print(student)

