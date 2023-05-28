
student = {"name": "Jose", "age": 22, "courses": ["math", "Robotics"]}
#student.update({"name":"Angel", "age":22, "courses": ["math", "physics"], "phone": "555-555555"})
#del student["age"]
#age = student.pop("age")

#print(student.items())
#print(age)

for key, value in student.items():
    print(key+":", value)