# welcome to sparta program - concatination & interpolation

# version 1 - with concatenation
name = "this is an example"
firstname = "ayan".capitalize()
lastname= "bob".capitalize()
fullname= firstname +" " +lastname
print("welcome"+" "+fullname.strip()) # strip() removes whitespaces

#version 2 - with interpolation
full_name = "this is a random string"
first_name =input("first name"+" ")
last_name =input("last name"+" ")
full_name = first_name.capitalize() +  " " + last_name.capitalize()
print(f'Hello {full_name.capitalize()}! Welcome')