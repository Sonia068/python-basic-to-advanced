#------ Variables -------
x = 5
name = "Alex"  
print(x)
print(type(x))
print(name)
print(type(name))

#Deleting a Variable
x = 10
del x
print(x)

#Assigning Values to Variables:
#1. Basic Assignment: Variables are assigned values using the = operator.
x = 5
y = 3.14
z = "Hi"
print(type(x))
print(type(y))
print(type(z))


#2. Dynamic Typing: Python is dynamically typed, so the same variable can store different data types during execution.
x = 10
x = "Now a string"
print(x)

# 3. Assigning Same Value: same value can be assigned to multiple variables in a single line.
a = b = c = 100
print(a, b, c)


# 4. Assigning Different Values: Multiple variables can also be assigned different values in a single line.
x, y, z = 1, 2.5, "Python"
print(x, y, z)  


# Below listed variable names are valid:
age = 21
_colour = "lilac"
total_score = 90

#  Below listed variables names are invalid:
1name = "Error"  # Starts with a digit
class = 10       # class is a reserved keyword
user-name = "Doe"  # Contains a hyphen


#  Swapping Two Variables:
a, b = 5, 10
a, b = b, a
print(a, b)


# Counting Characters in a String:
word = "Python"
length = len(word)
print("Length of the word:", length)








"""
->  Variables are used to store data that can be referenced and manipulated during program execution. A variable is essentially a name that is assigned to a value.
->  Python variables do not require explicit declaration of type.
-> Type of the variable is inferred based on the value assigned.


#  Rules for Naming Variables: 
1) Names can contain letters, digits and underscores (_).
2) The first character cannot be a digit.
3) Names are case-sensitive, so myVar and myvar are treated differently.
4) Keywords such as if, else and for cannot be used as variable names.


->    Python variables store references to objects, not the actual values themselves. When a variable is reassigned, it starts referencing a new object while the old unreferenced object becomes eligible for garbage collection.

x=10
y=x
x="Computer"



->  the type() function return when called with a variable  --   
The type of the variable as a class type object.


->  del removes the variable definition from memory


"""