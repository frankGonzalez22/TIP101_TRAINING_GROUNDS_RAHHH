
#-------------------------------------------Problem 1:---------------------------------------------------

#1. Share 2 questions you would ask to help understand the question:
#How can I determine if candidate exist in dictionary?
#How can I add a new key into a existing dictionary?
#Understand
#Function takes in exisiting Dictionary and string
#Returns a newly modified dictionary 
#Dictionary has strings as keys and ints as key values 
#The function can add new voter to existing dictionary
#The function can update the key value in dictioanry  
#
#2. Write out in plain English what you want to do: 
#if the dictionary is empty, populate it
#if the name does not exist spefciy key DNE with a true or false var 'flag' 
#flag wil determing if we add new key to dict and assign key as 1 or not 
#3. Translate each sub-problem into pseudocode:
#Add +1 to key-value if name exist 
#Add new namae to candidate if name exist 
#4. Translate each sub-problem into pseudocode:
#return the new dictionary 
#5. Translate the pseudocode into Python and share your final answer:

def cast_vote(votes, candidate):
    flag = votes.get(candidate, "DNE")
    if flag != "DNE":
        votes[candidate] =  votes[candidate]+ 1
    else:
        votes[candidate] = 1
votes = {"Alice": 5, "Bob": 3}
cast_vote(votes, "Alice")
print(votes)
cast_vote(votes, "Gina")
print(votes)
#-------------------------------------------Problem 2:---------------------------------------------------
#1. Share 2 questions you would ask to help understand the question:
#What makes the 2 dictionaries common? Same key value or pairs?
#What functions can we use to solve this problem?
#Understand
#Function takes in 2 dicitonaries and reutrns a list of commonkeys 
#For dictionaries to be common, keys have to exist in both dicitonaries 
#Keys could possibly have the same value to be in common
#Plan
#Check if keys exist in both dictionaries
#Check if both dictionaries both have similar key-values 
#3. Translate each sub-problem into pseudocode:

#4. Translate each sub-problem into pseudocode:

#5. Translate the pseudocode into Python and share your final answer:
#-------------------------------------------Problem 3:---------------------------------------------------

#1. Share 2 questions you would ask to help understand the question:
    #What function is best use for this question?
    #Do it use the get method or loop through dictionary in this function?
    #Understand
    #Function takes in dictionary 
    #Function returns/prints task with highest value 
#PLAN
#2. Write out in plain English what you want to do: 
#Identify tasks with the max high value 
#3. Translate each sub-problem into pseudocode:

    #To find max val
    #Store key-values in a lsit 
    #Locate max value of key-value list 
    #loop through dictionary that has that max value 
    #4. Translate each sub-problem into pseudocode:
    #Remove task with max high value
    #Return removed task

#5. Translate the pseudocode into Python and share your final answer:
def get_highest_priority_task(tasks):
    keyValues = tasks.values()
    maxVal = max(keyValues)
    output =""
    for keys, keyVals in tasks.items():
        if keyVals==maxVal:
            output = keys
            tasks.pop(keys)
            return output
    
    return output
print("-------------------------------------------Problem 3:---------------------------------------------------")
tasks = {"task1": 8, "task2": 10, "task3": 9, "task4": 10, "task5": 7}
perform_task = (get_highest_priority_task(tasks))
print(perform_task)
perform_task = (get_highest_priority_task(tasks))
print(perform_task)
perform_task = (get_highest_priority_task(tasks))
print(perform_task)

print(tasks)
#-------------------------------------------Problem 4:---------------------------------------------------

#1. Share 2 questions you would ask to help understand the question:

    #How can I solve this only using 1 for loop?
    #What function can I use in this question?

    #Understand:
        #This function takes in a integer list
        #Function returns a dictionary of each integer with each occurance

    #Plan: 
        #2. Write out in plain English what you want to do:
        #if nums list have no numbers return empty dict
        #Create empty dictionary called 'output'
        #Determine if number exist in dictionary

#3. Translate each sub-problem into pseudocode:

    #obtain number by getting it from lst 
    #-1 indicates if # DNE, then add that number into dictionary 

#4. Translate each sub-problem into pseudocode:
    
    # incrment occurance by +1 
    
#5. Translate the pseudocode into Python and share your final answer:
print("-------------------------------------------Problem 4:---------------------------------------------------")
def count_occurrences(nums):
    output = {}
    if len(nums) == output:
        return output
    else: 
        for numbers in nums:
            if output.get(numbers,-1) > 0:
                output[numbers] = output[numbers] + 1
            else:
                output[numbers] = 1 
    return output
            
nums = [1, 2, 2, 3, 3,1, 3, 4]
print(count_occurrences(nums))
#-------------------------------------------Problem 5:---------------------------------------------------
print("-------------------------------------------Problem 5:---------------------------------------------------")

#1. Share 2 questions you would ask to help understand the question:
    #How can I solve this without the get function?
    #How can I do this with 1 forloop?
#Understand
#   This function takes in a lst 
#   Function returns element that is found majority in elemnt that is >n/2
  
#2. Write out in plain English what you want to do: 
#Plan 
    #Store length of lst 'elements' in var called 'lstlen'
    #Create dict called  'dict'
    #for each number in lst 'elements'
    #see if number is in dict elements 
    #if in dict add by 1
    #if not in dict add it 
    

#3. Translate each sub-problem into pseudocode:
    #let solution below be helper function called findMaxVal(dict)
    #loop through dict
    #determine max occurance
#4. Translate each sub-problem into pseudocode:
    # if max occur > n/2 return num
    #else return none 
#5. Translate the pseudocode into Python and share your final answer:
def findMaxVal(dict):
    maxVal = max(tasks.values())
    output = 0
    for keys, keyVals in tasks.items():
        if keyVals==maxVal:
            output = keys
            return  int(output)
    return int(output)

def find_majority_element(elements):
    lstlen = len(elements)
    dict = {}
    for num in elements:
        if num in dict:
            dict[num]+=1 
        else:
            dict[num] = num
    print("Num ",findMaxVal(dict))
    if findMaxVal(dict) >lstlen/2:
        return findMaxVal(dict)
    else:
        return None
elements = [2, 2, 1, 1, 1, 2, 2]
print(find_majority_element(elements))
