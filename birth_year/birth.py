# calculate year of birth

name = input("what is your name"+" ")
age =int(input("age"+" "))
print("OMG, you are" +" "+str(age)+" "+ "years old and was born in the year...")
year_born = 2022 - age
print(year_born)


# account for if persons birthday has already happened this year or not


# look into library time and print out hours this person has lived for

#IMPORT DATE TIME MODULE

import datetime

x=datetime.datetime(year_born,int(input("month born"+ " ")),int(input("day born"+" ")))

print(x)

# at this point we know there birthday - has it gone by this year

import datetime

y= datetime.datetime.now()

