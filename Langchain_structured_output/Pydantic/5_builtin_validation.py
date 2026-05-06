from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = "sennsay"
    age: Optional[int] = None
    email : EmailStr
    cgpa: float = Field(gt=0, le=10, default=5, description="CGPA should be between 0 and 10")

new_student = {'age':32, 'email':'abc@gmail.com', 'cgpa':9}
# if 'email':'abc' -> this throw error. You have to write @gmail.com (built in validation)

student = Student(**new_student) #pydantic object

#pydantic object convert into dict

print(dict(student))

student_json = student.model_dump_json()

print(student)