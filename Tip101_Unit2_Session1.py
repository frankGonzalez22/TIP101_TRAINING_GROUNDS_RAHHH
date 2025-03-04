print("-------------------------------------------Problem 1:---------------------------------------------------")

#PROBLEM 1 
# Template Questions
#1. Share 2 questions you would ask to help understand the question:
#What does the word  adjacent  mean in the context of this question?
#Adjacenent means neighboring, in this case the lst subsequence does not have to be neighboring 
#What is a subsequence and an example of one?
#A subsequence is a list of #s that is a subset of another list 
#2. Write out in plain English what you want to do: 
    #Function takes in 2 lst inputs and return True if subsequence
    #Declare function header 
    #loop through the 'sequence' list. 
    #check if all items in 'sequence' existn not in 'lst' reture False 
    #Else Return true if otherwise 
def is_subsequence(lst, sequence):
    for nums in sequence:
        if nums not in lst: 
            return False
    return True 
lst = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(is_subsequence(lst, sequence))
print("-------------------------------------------Problem 2:---------------------------------------------------")

#-------------------------------------------Problem 2 -------------------------------------------
#1. Share 2 questions you would ask to help understand the question:
#Can we assume both keys and value list are equal lengths?
#Is there another way of doing this without a dobule for loop?
#2. 
#Declare empty dict 
#loop through keys list 
#within loop have an index to locate items in key list
#populate emptyDict's key with the actual value from keylst
#assign EmptyDicts key with values from value lst 
#pair each key and value to empty list 
# Template Questions
def create_dictionary(keys,values):
    emptyDict = {}
    for i in range(len(keys)):
        emptyDict[keys[i]] = values[i]
    return emptyDict
keys = ["peanut", "dragon", "star", "pop", "space"]
values = ["butter", "fly", "fish", "corn", "ship"]
print(create_dictionary(keys,values))
print("-------------------------------------------Problem 3:---------------------------------------------------")

#-------------------------------------------Problem 3:---------------------------------------------------

#1. Share 2 questions you would ask to help understand the question:

    #What kind of existing dictionary functions should I use?
    #How can I write out a logic that looks at both key and key value pair?

#2. Write out in plain English what you want to do: 
    #check if key value exist 
    #if DNE print pairprint  does not exist 
    #if do exist print out key, key value 

#5. Translate the pseudocode into Python and share your final answer:
dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}

    
def print_pair(dictionary, target):
    if target in dictionary:
        print("Keys: ", target)
        print("Value: ", dictionary[target])
    else:
        print("That pair does not exist!")
    
print_pair(dictionary, "patrick")
print_pair(dictionary, "plankton")
print_pair(dictionary, "spongebob")

print("-------------------------------------------Problem 4:---------------------------------------------------")
#1. Share 2 questions you would ask to help understand the question:
# How can I use for loop once in this question
# Can I declare 2 var in 1 line and solve it that way?
#2. 
#Declare two empty variables 'var1','var2'
#lopp through dictionary
#var1 will take in the sum of key
#var2 will take in sum of val
#if val>key return val
#if val<key return keys
#return balance
#
def keys_v_values(dictionary):
    var1 = 0
    var2 = 0
    for keys, val in dictionary.items():
        var1 += keys
        var2 += val
    if var1 > var2:
        return "Keys"
    elif var1 < var2:
        return "Values"
    else:
        return "Balanced"
dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
greater_sum = keys_v_values(dictionary1)
print(greater_sum)

dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
greater_sum = keys_v_values(dictionary2)
print(greater_sum)




print("-------------------------------------------Problem 5:---------------------------------------------------")

#-------------------------------------------Problem 5:---------------------------------------------------

#1. Share 2 questions you would ask to help understand the question:
    #How can I add new key into dictionary?
    #How can I update current key without carring about the order
  
#2. Write out in plain English what you want to do: 
    #loop to check if restock list is in invenory
#3. Translate each sub-problem into pseudocode:
    #if not in inventory add it with current stock
#4. Translate each sub-problem into pseudocode:
    #if in inveotry add additional iten to current stock

#5. Translate the pseudocode into Python and share your final answer:
def restock_inventory(current_inventory, restock_list):
     for item, quantity in restock_list.items():
        if item in current_inventory:
            current_inventory[item] += quantity
        else:
            current_inventory[item] = quantity
        return current_inventory
current_inventory = {
    "apples": 30,
    "bananas": 15,
    "oranges": 10
}

restock_list = {
    "oranges": 20,
    "apples": 10,
    "pears": 5
}
print(restock_inventory(current_inventory,restock_list))