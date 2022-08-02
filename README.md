### Data types and oprators

### 2 tpes of operators

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

#### strings concatenation costing

- strings indexing
- `Hello World!`
- index in python starts with 0

````python
#print(len(greeting))
#print(greeting[-5])
#print(greeting[:5])

#print only world using slicing

print(greeting[6:])
print(greeting[3])
print(greeting[-9])
print(greeting[6])


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

# data collections
## lists, tuples & dict

### lists
# what are lists? exam questions related to this
# very simple sometimes - examples below
# correct syntax []
# lists are mutable
# indexing same concept allies

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