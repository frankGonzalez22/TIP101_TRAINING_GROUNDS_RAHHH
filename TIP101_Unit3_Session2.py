
#1. Share 2 questions you would ask to help understand the question:
#How Can I convert a string to an int?
#How do iterate and convert at the same time?
#Understand
#Sum takes in a list of stirngs
#Returns an int of sums of items in string 
#2. Write out in plain English what you want to do: 
#EdgeCase: Empty list return 0 ,
#Loop trough each item in list 
#3. Translate each sub-problem into pseudocode:
#Declare empty var caled output 
#For each item convert into an int
#4. Translate each sub-problem into pseudocode:
#Add each item into an output 
#Return it 
#5. Translate the pseudocode into Python and share your final answer:
print("------------------Problem 1 --------------------")
def sum_of_number_strings(nums):
    output = 0
    if len(nums) == 0: return 0
    for number in nums:
        output += int(number)
    return output

nums = ["10", "20", "30"]
sum = sum_of_number_strings(nums)
print(sum)
print("------------------Problem 2 --------------------")

#1. Share 2 questions you would ask to help understand the question:
#Can I use a set since it cannot take any duplciates?
#If so what functin can I use?
##Understand
#Function takes in list that is SORTED
#Function returns list of non duplciates  

#2. Write out in plain English what you want to do: 
#Creat empty set 
#3. Translate each sub-problem into pseudocode:
#Loop each number
#4. Translate each sub-problem into pseudocode:
#Add number into empty set 
#5. Translate the pseudocode into Python and share your final answer:
def remove_duplicates(nums):
    emptySet = set()
    for number in nums:
        emptySet.add(number)
    return list(emptySet)

print(remove_duplicates([1,1,1,2,3,4,4,5,6,6]))

print("------------------Problem 3 --------------------")

#1. Share 2 questions you would ask to help understand the question:
#Can this only be done with a for loop or under 1 for loop?
#Is it Ideal if I use an array to store my convert and convert it to string?
#Understand
#Function takes in string
#Function reverse string
#Function maintain same order of characters while we reveerrse  


#2. Write out in plain English what you want to do: 
#Create empty array with defined length   called ouput 
#As I loop through first letter of 's' I want to 
#Keep track of first and last letter  - calls for enumuerate ngl or 2 pointer tbh
#3. Translate each sub-problem into pseudocode:
#let first pointer keep track of first letter
#let last pointer point last letter 
#as we go to one chracter at a time
#4. Translate each sub-problem into pseudocode:
#if character add it to its current index 
#swap placement of first and last index
#Convert list into string 
#5. Translate the pseudocode into Python and share your final answer:
def reverse_only_letters(s):
    reverseArr = [None]*len(s)
    for firstLetter, lastLetter in enumerate(range(len(s)-1, -1, -1)):
        if s[firstLetter] != "-" and s[lastLetter] != "-":
            temp = s[lastLetter]
            s[firstLetter] = s[lastLetter]
            s[lastLetter] = temp 
    return ''.join(reverseArr)
s = "a-bC-dEf-ghIj"
#reversed_s = reverse_only_letters(s)
#print(reversed_s)
print("------------------Problem 4 --------------------")

#1. Share 2 questions you would ask to help understand the question:
#How can function return 1 as a longest string?
#Do we use a max function for this problem can we do max(dict)?
#Understand
#Function takes in string 
#Function is case senstive and will count the longest string
#Function will return an int 
#2. Write out in plain English what you want to do: 
#Create empty dict 
#Loop through entire string 
#3. Translate each sub-problem into pseudocode:
#Return max value of dict
#4. Translate each sub-problem into pseudocode:
#5. Translate the pseudocode into Python and share your final answer:#1. Share 2 questions you would ask to help understand the question:
def longest_uniform_substring(s):
    emptDict = {}
    for letters in s:
        if letters not in emptDict: 
            emptDict[letters] = 1
        else:
            emptDict[letters]+= 1 
    return max(emptDict.values())
s1 = "aabbbbCdAA"
l1 = longest_uniform_substring(s1)
print(l1)

s2 = "abcdef"
l2 = longest_uniform_substring(s2)
print(l2)
print("------------------Problem 5 --------------------")

#1. Share 2 questions you would ask to help understand the question:
#Understand

#2. Write out in plain English what you want to do: 
#3. Translate each sub-problem into pseudocode:
#4. Translate each sub-problem into pseudocode:
#5. Translate the pseudocode into Python and share your final answer:#1. Share 2 questions you would ask to help understand the question:
