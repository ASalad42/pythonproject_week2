# if elif else

# loops -for amd while loops

#not to repeat yourself
#loops help us ITERATE through data collections - DATA
#lets create a list to use for loop to iterate

shopping_list = ["fruits","milk","cream","bread"]

#print(shopping_list[0])
#print(shopping_list[1])
#print(shopping_list[2])
#print(shopping_list[-1])

#all the above code is simplified by the following loop
#the data collection above could have been dictionaries too

#for item in shopping_list:
   # print(item)
    #does the list have milk - customer question
    #if milk is found in list stop the program
  #  if item == "milk":
       # break


dic1 = {
    "key": "value",
    "name":"james",
    "age":"30",
    "height_cm":"178",
    "weight_kg":"75",
    "gender":"male"
}

#for keys, values in dic1.items(): #print both key and value
   # print(keys," ", values) #prints the key with its corresponding value

#for keys in dic1.keys(): # prints only keys - iterate through keys
   # print(keys)

#for values in dic1.values(): #prints only values - iterate through values
   # print(values)

# use case of multiple conditions
#create a list with int values 1-4
data_list = [1,2,3,4]
#iterate through the list using for loop
#for element in data_list:
 #find 3 and print if found
   # if element == 3:
       # print("found 3")
 #or else list number greater than 3 print "gone too far"
    #elif element > 3:
      #  print("gone too far")
 #otherwise print too soon
    #else:
      #  print("too soon")

# while loop
# while loops are mostly used as a monitor rather than handling items

number = 0
# iterate while number is less than 10
#while number < 10:

    # print the number with message stating its working
    #print(f"it is working - -> {number}")

# add +1 in each iteration
   # number += 1

#age = input("please enter your age"+" ")
#print a message stating your age is whatever the input user entered
#print(f"your age is {age}")

user_prompt = True
while user_prompt:
    age = input("Please enter your age ")
    if age.isdigit() and int(age) < 177:
        user_prompt = False #stops prompting the user
    else:
        print("please enter numbers only and max age of 177 years old")
print(f"your age is {age}")

#using the above use case also check if user age is less than 117 years