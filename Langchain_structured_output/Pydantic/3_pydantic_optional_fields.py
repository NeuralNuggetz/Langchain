from pydantic import BaseModel
from typing import Optional

class Student(BaseModel):
    name: str = "sennsay"
    age: Optional[int] = None #Here you can pass any other type "only int" because in class age defined as Optional[int] = None.

# Creating an instance of the Student class
new_student = {'age':32}

student = Student(**new_student)

print(student)

