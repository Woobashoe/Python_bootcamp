print("Hello!")
print("GODDAGELLE")

def square(num):
    return num**2

my_nums = [1,2,3,4,5]

for item in map(square,my_nums):
    print(item)

# or;

print(list(map(square,my_nums)))

# returnar Första bokstaven i ett namn om namnet är udda, och "EVEN" om namnet är jämnt
def splicer(mystring):
    if len(mystring)%2 == 0:
        return "EVEN"
    else:
        return mystring[0]

namn= ["Henke","Annasara","Karl","GJ"]

print(list(map(splicer,namn)))

# Checks if a number is even
def check_even(num):
    return num%2 == 0

mynums = [1,2,3,4,5,6]

for n in filter(check_even,mynums):
    print(n)

#lamdba expression to take a number to the power of 2
square = lambda num: num ** 2

print(square(28))

# map takes a function and an interable object, a lambda expression is a function, and therefore we can write:

print(list(map(lambda num:num**2,mynums)))

# Making the "check_even"function to a lambda function

print(list(filter(lambda num:num % 2 == 0,mynums)))

# Making a lambda function

print(list(map(lambda name:name[0],namn)))

# NESTED STATEMENTS AND SCOPE

x = 25

def printer():
    x = 50
    return x
print(x)
print(printer())



# LEGB Rule:
#   L: Local - In a function
#   E: Enclosing function locals - Also in functions, will use the closest name, if the variable is in both a function
    # and globaly, the variable in the function will be selected
#   G: Global - names assigned at the top-level of a module file
#   B: Built in - names preassigned in the built-in names module: open, range, etc..

# Global
name = "GLOBAL"

def greet():
    #Enclosing
    name = "Enclosing"

    def hello():
        #Local
        name = "Local"

        print("Hello "+name)
    hello()

greet()















