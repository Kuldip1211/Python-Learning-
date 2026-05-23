# foor loop 

n = 4
for i in range ( 0 , n):
    print(i)

#else in for loop 

print("ELse in loop")
for i in range(0,6):
    print(i)
else:
    print("loop is end");


#loop in array
print("Loop is end")
a = [ "banana" , "apple" , "chery"]

for i in range(len(a)):
    print(a[i]);
else:
    print("loop is end")

#loop using statrt oparameter
print("using Start parameter ")

for i in range (2,6):
    print(i);
else :
    print("loop is end")

# increment with sequnece with int 
print("Increment the sequence with 3 (default is 1):");

for x in range (2,30,3):
    print(x);
else:
    print("loop is end")

# just like auther u also use the break statement to break the loop 

#pass statment 

#foor loop can not be empty be in coding for some reasone you put empty you can use the pass statment 

for x in range(3):
    pass
else:
    print("Loop end nusing pass")