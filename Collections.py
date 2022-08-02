# data collections
## lists, tuples & dict

### lists
# what are lists? exam questions related to this
# very simple sometimes - examples below
# correct syntax []
# lists are mutable
# indexing same concept allies

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