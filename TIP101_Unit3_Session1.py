#1. Share 2 questions you would ask to help understand the question:
#What does this function do?
#WHat syntax allows us to modify the string when we output them?
#Understand
#This function takes in a number and incrment number & concatenate it with string
#2. Write out in plain English what you want to do: 
#3. Translate each sub-problem into pseudocode:
#Loop through from 1 to limit
#Print number wit missibi
#4. Translate each sub-problem into pseudocode:
#5. Translate the pseudocode into Python and share your final answer:
print("----------------------Question 1----------------------")
def count_mississippi(limit):
    for num in range(1, limit):
	    print( f"{num} mississippi")
count_mississippi(5)
#1. Share 2 questions you would ask to help understand the question:
#Understand
#Function takes in string function
#Function returns swap letters of first and last string 
#2. Write out in plain English what you want to do: 
#If function is less than 2 characters return string as is
#3. Translate each sub-problem into pseudocode:
#Declare function called 'output'
#Have variable store first character
#Have vatriable store first character + 1 and last character -1 
#4. Translate each sub-problem into pseudocode:
#CReate new word by adding last char + midle char + first char 
#5. Translate the pseudocode into Python and share your final answer:print("----------------------Question 1----------------------")
print("----------------------Question 2----------------------")

def swap_ends(my_str):
      if len(my_str) <2:
            return my_str
      output = ""
      firsChar = my_str[0]
      midChar = my_str[1:len(my_str)-1]
      lastChar = my_str[-1:]
      output += lastChar + midChar + firsChar
      return output
    # One line approach: Return  myStr[-1:] + mtstr[1:-1] + myStr[:-1]
my_str = "boat"
swapped = swap_ends(my_str)
print(swapped)



#1. Share 2 questions you would ask to help understand the question:
#Understand
#Function takes in string function
#Function returns swap letters of first and last string 
#2. Write out in plain English what you want to do: 
#Convert string into lower-case
#Have of letters
#3. Translate each sub-problem into pseudocode:
#For each letter if not in list return False 
#4. Translate each sub-problem into pseudocode:
#Return true  if otherwise 
#5. Translate the pseudocode into Python and share your final answer:
def is_pangram(my_str):
      lowerCaseStr = "abcdefghijklmnopqrstuvwxyz"
      for let in lowerCaseStr:
            if let not in my_str.lower():
                return False
      return True
print("----------------------Question 3----------------------")
my_str = "The quick brown fox jumps over the lazy dog"
print(is_pangram(my_str))

str2 = "The dog jumped"
print(is_pangram(str2))

#1. Share 2 questions you would ask to help understand the question:
#Understand
#Function takes in string function
#Function returns string reverse 
#2. Write out in plain English what you want to do: 
#Declare variable called output

#3. Translate each sub-problem into pseudocode:
#loop from the end charcater add to outout
#4. Translate each sub-problem into pseudocode:
#Stop at the first character
#Return  output

#5. Translate the pseudocode into Python and share your final answer:
def reverse_string(my_str):
    output  = ""
    for i  in range(len(my_str)-1, -1, -1):
        output += my_str[i]
    return output
#Alternative Method
#Return mystr[::-1]
#myStr[start, end, step] 
#We are stepping -1 or from the 
#ALternative Method:
#For loop
# char + emptystring
#Adds first letter in

    
my_str = "live"
print("----------------------Question 4----------------------")
print(reverse_string(my_str))    


#1. Share 2 questions you would ask to help understand the question:
#How can I take a string and keep count of its occurance?
#When do I stop when I find non repeating character
#Take in string as aparmaeter ?
#Understand:
#Take in string 
#Return  first occurence index  that is not returning 
#2. Write out in plain English what you want to do: 
#Create an empty dictionary 
#For each letter, assign letter as a index as a key and +1 as a value 
#3. Translate each sub-problem into pseudocode:
#loop through dictionary, if keyval is 1, return index 
#4. Translate each sub-problem into pseudocode:
#Return -1 if otherwiase 

#5. Translate the pseudocode into Python and share your final answer:
def first_unique_char(my_str):
    emptyDict = {}
    for i in range(len(my_str)):
        if my_str[i] not in emptyDict:
            emptyDict[i] = 1
        else:
             emptyDict[i] += 1
    for index in emptyDict:
         if emptyDict[index] ==  1:
              return index
    return -1
print("----------------------Question 5----------------------")

my_str = "leetcode"
print(first_unique_char(my_str))

str2 = "loveleetcode"
print(first_unique_char(str2))

str3 = "aabb"
print(first_unique_char(str3))
       
             
         




#1. Share 2 questions you would ask to help understand the question:
#Understand

#2. Write out in plain English what you want to do: 
#3. Translate each sub-problem into pseudocode:
#4. Translate each sub-problem into pseudocode:
#5. Translate the pseudocode into Python and share your final answer:#1. Share 2 questions you would ask to help understand the question:
#Understand

#2. Write out in plain English what you want to do: 
#3. Translate each sub-problem into pseudocode:
#4. Translate each sub-problem into pseudocode:
#5. Translate the pseudocode into Python and share your final answer: