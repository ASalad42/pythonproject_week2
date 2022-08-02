
#function methods builtin in python

greeting = 'hello world!'

#print(greeting)
#if we wanted to check if letters are in string

#print(greeting.isalpha()) #true or false

#is it in lower case or uppercase
#print(greeting.islower())
#print(greeting.isdigit())
#print(greeting.endswith("!"))
#print(greeting.startswith("H"))




#print(len(greeting))
#print(greeting[-5])
#print(greeting[:5])

#print only world using slicing

print(greeting[6:])
print(greeting[3])
print(greeting[-9])
# print(greeting[6])
#
# example_string = "jane"
# print(example_string)
# print(len(example_string))
# # strip()
#
# print(len(example_string.strip()))
# #welcome user with their name and welcome message - name and message must start with capital
# example_text = "Heres Some text with lots of text"
# print(example_text.count("text"))
#
# #find a method to bring the statment in captial letter
# print(example_text.capitalize())
# print(example_text.lower())


first_name = "james"
mid_name = "bond"
last_name = "007"
age = 47
address = 33
postcode = ""
print(str(age)) #int to string
print(first_name+" "+mid_name+" "+last_name+" "+str(age)) #simple example of concatenation
#print(int())