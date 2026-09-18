s = {
    "hi":"Kajal",
    "age":22
}
if s.get("name")is not None:
    print("key exist")
else:
    print("false")
print(s["age"])
print(s.get("name"))
