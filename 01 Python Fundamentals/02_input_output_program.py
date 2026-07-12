name=input("Enter your name:")     #input
print("Hello, " + name +"! Welcome to the program.")    #output  ---(string Concatenation)
print("Hello,", name, "! Welcome!")                   #output -- (multiple arguments)


s = "Brad"
print(s)
 

s = "Anjelina"
age = 25
city = "New York"
print(s, age, city)



# the default return type of the input() function in Python is string
name = input("Enter your name:")   
print(name)
print(type(name))

#convert a string input to an integer in Python
age = int(input("Enter your age: "))
print(age)
print(type(age))    

# multiple inputs from the user in one line
first_name, last_name, country = map(str, input("Enter details: ").split())

print(first_name)
print(last_name)
print(country)

# input() returns strings, use map(int, ...) to convert them to integers.
a, b = map(int, input("Enter two numbers: ").split())
print(a + b)


# valid way to print output in Python
"""
1) print("Hello, World!")
2) print(f"Hello, World!")   # Here, the f means it's an f-string (formatted string).   Since there are no variables inside {}, the f is unnecessary.
Eg :  name = "Alice"
      print(f"Hello, {name}!")

3) import sys
   sys.stdout.write("Hello, World!")

   -> Notice that it does not automatically move to the next line.
        import sys
        
        sys.stdout.write("Hello")
        sys.stdout.write("World")
        
        
        -> add a new line, include \n:
        import sys
        
        sys.stdout.write("Hello\n")
        sys.stdout.write("World")
        


"""
