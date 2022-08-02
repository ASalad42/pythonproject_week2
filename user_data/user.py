#Inputs and tailored message

print("Please enter your first and last name")
first_name =input("first name"+" ")
last_name =input("last name"+" ")
full_name = first_name.capitalize() +  " " + last_name.capitalize() #methods
print("your full name is...")
print(full_name)
height_cm = int(input("height in cm"+" "))
print("your height in cm is...")
print(height_cm)
favourite_colour= input("colour"+" ")
print("your favourtie colour is")
print(favourite_colour)
secret_spirit_animal = input("animal"+" ")
print("your secret spirit animal is")
print(secret_spirit_animal)
print(secret_spirit_animal[0])
print(secret_spirit_animal[-1])
print(len(secret_spirit_animal))

#allow user to guess seceret animal and if correct print out "OMG how did you know"