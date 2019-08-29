
import math

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



def vol(rad):
    return 4*math.pi*rad**3/3

print(vol(3))

def ran_check(num,low,high):
    if low<num<high:
        return print("Det är i spannet")
    else:
        return print("NEJ!")

ran_check(4,1,4)

def ran_bool(num,low,high):
    return low<num<high

print(ran_bool(3,1,6))


strang= "HHHHeeeeLLLLsss"




def up_low(s):
    x = 0
    y = 0
    for c in s:
        if c == c.lower():
            x=x+1
        else:
            y=y+1
    return print(f"Number of uppercase = {y}, number of lowercase = {x}")


up_low(strang)

lest=["e","e","d","e","t"]

def unique_list(l):
    return print(list(set(l)))

unique_list(lest)

numse= [-1,22,10]

def multiply(numbs):
    total=1
    for num in numbs:
        total*=num
    return print(total)

multiply(numse)

def palindrome(s):
    return print(s==s[::-1])
