# Conditionals and Branching
a = 33
b = 200
if b > a:
  print("b is greater than a")

#The Elif Keyword
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#The else statement 
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

  #The pass statement is a null operation - nothing happens when it executes. It serves as a placeholder.
  a = 33
  b = 200

if b > a:
  pass
else :
  print("Pass")

#Why Use pass?
# When you're creating code structure but haven't implemented the logic yet
# When a statement is required syntactically but no action is needed
# As a placeholder for future code during development
# In empty functions or classes that you plan to implement later

# A comment is ignored by Python, but pass is an actual statement that gets executed (though it does nothing). You need pass where Python expects a statement, not just a comment.


