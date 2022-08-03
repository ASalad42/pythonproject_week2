# what is a function
# why do we need it
# DRY -DO NOT REPEAT YOURSELF (PROCEDURAL PROGRAMMING OR OOP)

# 1 def function (): correct > test example question checking syntax
# first example iteration
#def greet_user():
    #print("Welcome")
# we must call the function otherwise it will not give you the ooutput
#greet_user()

#def greet_user(name): # if you give it an argument you must later call using this
   # print("welcome dear"+" " +name)

#greet_user("ayan") # you have to add the argument

# create a function that takes two arguments as int

#def add(a,b):
    #return (a+b)
#print(add(10,15)) #R>L printing the funcion we call with arguments we want to investigate
# or
#answer = add(10,15)
#print(answer)

# basiccalc

a=10
b=5

def add(a,b):
    return(a+b)
def subtracrt (a,b):
    return(a-b)
def multiply(a,b):
    return(a*b)
def divide(a,b):
    return(a/b)

print(add(a,b))
print(subtracrt(a,b))
print(multiply(a,b))
print(divide(a,b))