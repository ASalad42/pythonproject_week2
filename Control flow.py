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

for keys, values in dic1.items():
    print(keys," ", values) #prints the key with its corresponding value
    print(dic1.keys()) #prints only keys
    print(dic1.values()) #prints only values