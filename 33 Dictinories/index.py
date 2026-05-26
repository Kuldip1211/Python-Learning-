#Dictinory 
example = {
    "car" : "maruti suziki",
    "setting" : "4"
}

print(example)
print(example["car"]) # if key is not presant then retuen error 
print(example.get("car")) # if key is not presant then return none


# for print all keys 
print(example.keys())

#for print all values 
print(example.values())

#for print key value pairs
print(example.items())

#iterate 
for key,value in example.items():
    print(f"{key} : {value}")