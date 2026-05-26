"""
Dictionary methods in Python with short comments and examples.
"""

student = {
	"name": "Asha",
	"age": 20,
	"city": "Pune",
	"courses": ["math", "cs"],
}

# get(key, default) -> safely read a key, default used if missing
print("get name:", student.get("name"))
print("get missing:", student.get("grade", "N/A"))

# keys(), values(), items() -> views for keys/values/pairs
print("keys:", list(student.keys()))
print("values:", list(student.values()))
print("items:", list(student.items()))

# copy() -> shallow copy
student_copy = student.copy()
student_copy["city"] = "Mumbai"
print("original city:", student["city"], "copy city:", student_copy["city"])

# update() -> merge another dict or key-value pairs
student.update({"age": 21, "grade": "A"})  # update existing and add new
student.update(city="Delhi")  # update single key using kwargs
print("after update:", student)

extra = {"city": "Jaipur", "club": "music"}
student.update(extra)  # merge another dict object
print("after update with dict:", student)

# setdefault(key, default) -> get or insert if missing
student.setdefault("club", "robotics")
print("after setdefault:", student)

# pop(key, default) -> remove and return a value
removed_age = student.pop("age")
print("popped age:", removed_age)
print("after pop:", student)

# popitem() -> remove and return the last inserted pair (Python 3.7+)
last_pair = student.popitem()
print("popitem:", last_pair)
print("after popitem:", student)

# fromkeys(iterable, value) -> create a new dict from keys
empty_scores = dict.fromkeys(["math", "cs", "english"], 0)
print("fromkeys:", empty_scores)

# clear() -> remove all items
student.clear()
print("after clear:", student)
