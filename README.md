# Python 
## Learning so far
### Data types and oprators

### 2 types of operators

#### arthmetic operators

- '+' '-' '*' '/'
- adds two oeprators
- subtract
- multiply
- divide

#### comparison operators

- '>' greater than
- '<' less than
- equal to
- '! ='
- '>='
- '<='

##### Builtin methods

```

#function methods builtin in python

greeting = 'hello world'

print(greeting)
#if we wanted to check if letters are in string

print(greeting.isalpha()) #true or false

#is it in lower case or uppercase
print(greeting.islower())
print(greeting.isdigit())
print(greeting.endswith("!"))
print(greeting.startswith("H"))
```

#### strings concatenation and casting


### Indexing example - will be in test!
- strings indexing
- `Hello World!`
-  index in python starts with 0
1. how to slice it 
2. how to divide it 
3. how pick specific character 
4. 2/3 questions related to i

````python
print(len(greeting))
print(greeting[-5])
print(greeting[:5])

#print only world using slicing

print(greeting[6:])
print(greeting[3])
print(greeting[-9])
print(greeting[6])

````
### More on strings 
```python 
example_string = "jane"
print(example_string)
print(len(example_string))
# strip()

print(len(example_string.strip()))
#welcome user with their name and welcome message - name and message must start with capital
example_text = "Heres Some text with lots of text"
print(example_text.count("text"))

#find a method to bring the statment in captial letter
print(example_text.capitalize())
print(example_text.lower())

````

# Data collections

## lists, tuples & dictionaries

### Lists

- what are lists? exam questions related to this
- very simple sometimes - examples below
- correct syntax []
- lists are mutable
- indexing same concept allies

```python
shopping_list = ["bat", "milk", "bread"]
            #      0        1       2
#print(shopping_list)

print(type(shopping_list))
print(len(shopping_list))

# how to add to our shopping list

shopping_list.append("oreos ") # append() adds an item at the end of the list
print(shopping_list)

# how to delete an item from our shopping list

shopping_list.remove("milk")
print(shopping_list)

# find out how to replace an item from the list and replace bat with milk
shopping_list[0] = "milk"
print(shopping_list)

#list can contain different data types
mixed_list = [1,2,3, "one","two","three"]
print(mixed_list)

#print 2&3 from the above list
print(mixed_list[1]) #outcome would print 3
print(mixed_list[2]) #outcome would print 2
print(mixed_list[1:3]) #outcome would be 2,3 - CORRECT ANS
print(mixed_list[-1:]) #outcome is three

```

### Tuples

- why do we need tuple 
- lists [] are mutable vs tuples () are immutable 
- syntax for tuple ()
- what are the use cases? date of birth will never change 

````python
essential = ("city", "DOB", "place of birth")
print (essential)
print (type(essential))

print (essential[1])  #indexing concept still applies and stays the same for both list and tuple

essential[0] = "town" #immutable - cant change city because we said earlier is unchangeable
just tried to change index 0 in tuple and we were not allowed
store this value (town) in index 0 for tuple (essential) > cant do that!
````
- essential (a,b,c) tuples 
- essential [a,b,c] list
- essential {} Dic

### Dictionary

- what is a dic {}? 
- Dictionary can have all types of data collections - 
- dict work as "KEY": "VALUE" pair

````python
devops_student1 = {
    "key": "value",
    "name":"james",
    "stream":"tech",
    "completed_lessons":3, #int
    "completed_lessons_name":["lists","operations","builtin methods"] # adding list

}
print(devops_student1)
# print(devops_student1.keys()) #only see keys
# print(devops_student1.values()) #only see values
# print(devops_student1["name"]) #to find the name of student 1 use key for him which is name

# find out how to delete in item from dic and delete operations
devops_student1["completed_lessons_name"].remove("operations")
# find out how to change completed lessons from 3 to 2
devops_student1["completed_lessons"] =2
print(devops_student1)
````

### Control Flow

- if, elif, else statments - conditional statments

````python
weather = "sunny" # True or False
if weather == "sunny":
    print("lets do bbq") # execute this line if sunny

elif weather == "dry":
    print("getting there") # if line 88 has "dry" then this will be executed

else:
    print("hope for the best") # this is said if it isnt sunny

# if elif else
# loops -for and while loops
#not to repeat yourself
#loops help us ITERATE through data collections - DATA
#lets create a list to use for loop to iterate

shopping_list = ["fruits","milk","cream","bread"]

print(shopping_list[0])
print(shopping_list[1])
print(shopping_list[2])
print(shopping_list[-1])

#all the above code is simplified by the following loop
#the data collection above could have been dictionaries too

for item in shopping_list:
   print(item)
    #does the list have milk - customer question
    #if milk is found in list stop the program
   if item == "milk":
       break


dic1 = {
    "key": "value",
    "name":"james",
    "age":"30",
    "height_cm":"178",
    "weight_kg":"75",
    "gender":"male"
}

for keys, values in dic1.items(): #print both key and value
    print(keys," ", values) #prints the key with its corresponding value

for keys in dic1.keys(): # prints only keys - iterate through keys
    print(keys)

for values in dic1.values(): #prints only values - iterate through values
    print(values)

# use case of multiple conditions
#create a list with int values 1-4
data_list = [1,2,3,4]
#iterate through the list using for loop
for element in data_list:
 #find 3 and print if found
    if element == 3:
        print("found 3")
 #or else list number greater than 3 print "gone too far"
    elif element > 3:
        print("gone too far")
 #otherwise print too soon
    else:
        print("too soon")

# while loop
# while loops are mostly used as a monitor rather than handling items

number = 0
# iterate while number is less than 10
while number < 10:

     # print the number with message stating its working
    print(f"it is working - -> {number}")

# add +1 in each iteration
    number += 1

age = input("please enter your age"+" ")
#print a message stating your age is whatever the input user entered
print(f"your age is {age}")

user_prompt = True
while user_prompt:
    age = input("Please enter your age ")
    if age.isdigit() and int(age) < 177:
        user_prompt = False #stops prompting the user
    else:
        print("please enter numbers only and max age of 177 years old")
print(f"your age is {age}")

#using the above use case also check if user age is less than 117 years   

````

sudo coding - human readable 

### Functions

````python
# what is a function
# why do we need it
# DRY -DO NOT REPEAT YOURSELF (PROCEDURAL PROGRAMMING OR OOP)

# 1 def function (): correct > test example question checking syntax
# first example iteration
def greet_user():
    print("Welcome")
# we must call the function otherwise it will not give you the output
greet_user()

def greet_user(name): # if you give it an argument you must later call using this
    print("welcome dear"+" " +name)

greet_user("ayan") # you have to add the argument

# create a function that takes two arguments as int

def add(a,b):
    return (a+b)

answer = add(10,15)
print(answer)




````