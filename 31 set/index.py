# A set stores only unique values.
# Even though 2 is written twice, it will appear only once in the set.
s = {2, 4, 2, 6}

# Print the set.
print(s)

# A dictionary stores data as key-value pairs.
# Here, each key is a string and each value is some related information.
s = {
    "car": "maruti suziki",
    "milage": 45,
    "4 wheel": bool(1)
}

# Print the dictionary.
print(s)

# Iterate through the dictionary using .items().
# .items() returns both the key and the value for each pair.
for key, value in s.items():
    print(key)
    print(value)