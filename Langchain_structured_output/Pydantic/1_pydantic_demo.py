from pydantic import BaseModel

class Student(BaseModel):
    name: str

# Creating an instance of the Student class
new_student = {'name':"Sennsay"} #Here you can not pass any other type "only string" because in class name defined as str.

student = Student(**new_student)

print(student)

