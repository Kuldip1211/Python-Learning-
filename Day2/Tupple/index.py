# A tuple is a collection which is ordered and unchangeable.

# Create a Tuple:
thistuple = ("apple", "banana", "cherry")
print (thistuple);

#Tuple items are ordered, unchangeable, and allow duplicate values.

# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

# To determine how many items a tuple has, use the len() function:
print(len(thistuple))

# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

# type <class 'tuple'>

# It is also possible to use the tuple() constructor to make a tuple.

thistuple2 = tuple(("apple", "banana", "cherry"))

# To join two or more tuples you can use the + operator:
tupple3 = thistuple + thistuple2;
print(tupple3);

# tuple3 = tuple1 + tuple2


