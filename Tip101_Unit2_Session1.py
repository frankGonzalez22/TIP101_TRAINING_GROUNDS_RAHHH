
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
 
    if dictionary.get(target,True):
        print("That pair does not exist!")
    else:
        print("Key: ", dictionary[target])
    
print_pair(dictionary, "patrick")
print_pair(dictionary, "plankton")
print_pair(dictionary, "spongebob")









#-------------------------------------------Problem 5:---------------------------------------------------

#1. Share 2 questions you would ask to help understand the question:
  
#2. Write out in plain English what you want to do: 

#3. Translate each sub-problem into pseudocode:

#4. Translate each sub-problem into pseudocode:

#5. Translate the pseudocode into Python and share your final answer:
