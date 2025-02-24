

#-----------------------------Problem 1-----------------------------------------

### U - Understand
#1. Share 2 questions you would ask to help understand the question:
#What data type can this list hold?
#What how can I print each element in a new line
### P - Plan
#2. Write out in plain English what you want to do:
#iterate through list using a for loop and print out each element within list
#Create the list and pass the lst into the function param

#Implement 
#3. Translate the pseudocode into Python and share your final answer:
def print_list(lst):
    for item in lst:
        print(item)
lst = ["squirtle", "gengar", "charizard", "pikachu"]
print_list(lst)
#-----------------------------Problem 2-----------------------------------------
### U - Understand
#1. Share 2 questions you would ask to help understand the question:
#How can change the value of each item in our list?
#What happens if there is nothing in our list?
### P - Plan
#2. Write out in plain English what you want to do:
#Create empty list to store new values that are multipled by 2 
#iterate through list using a for loop and for each item we X2 and append item to empty list 
#return my empty list 

#Implement 
#3. Translate the pseudocode into Python and share your final answer:
def doubled(lst):
    empty_lst = []
    for item in lst:
        empty_lst.append(item*2)
    return empty_lst
lst = [1,2,3]
new_lst = doubled(lst)
print(new_lst)
#-----------------------------Problem 4-----------------------------------------
### U - Understand
#1. Share 2 questions you would ask to help understand the question:
#Does this problem also require a empty list? 
#
### P - Plan
#2. Write out in plain English what you want to do:
#Create empty list to store new values that are multipled by -1
#iterate through list using a for loop and for each item we X-1 and append item to empty list 
#return my empty list 

#Implement 
#3. Translate the pseudocode into Python and share your final answer:
lst = [1,-2,-3,4]
def flip_sign(lst):
    empty_lst = []
    for item in lst:
        empty_lst.append(item*-1)
    return empty_lst

flipped_lst = flip_sign(lst)
print(flipped_lst)
#-----------------------------Problem 4-----------------------------------------
### U - Understand
#1. Share 2 questions you would ask to help understand the question:
#can we solve this without using min  or max function?

### P - Plan
#2. Write out in plain English what you want to do:
#use min and max function to find min and max value in list 
#
#return my difference 

#Implement 
#3. Translate the pseudocode into Python and share your final answer:
def max_difference(lst):
    return max(lst) - min(lst)
lst = [5,22,8,10,2]
max_diff = max_difference(lst)
print(max_diff)