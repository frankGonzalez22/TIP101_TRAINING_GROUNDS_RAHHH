
#1. Share 2 questions you would ask to help understand the question:
#Can we make sure our item is not divisible by 1 or itself?
#How can we stop the loop 
#Understand
#Function takes in int and return T or F when user  takes 
#in fucntion 
#2. Write out in plain English what you want to do: 
#Have a counter
#If number is divisible by itself and divisible by 1 
#set counter to 2
#decrement n by 1 
# if n is divissible by n-1 

#
#3. Translate each sub-problem into pseudocode:
#increment counter by 1 
#4. Translate each sub-problem into pseudocode:
#iof coutner  more than > 2 return  true 

#5. Translate the pseudocode into Python and share your final answer:#1. Share 2 questions you would ask to help understand the question:

def is_prime(n):
   
    while(n != 1):
        copy = n 
        if  copy %n == 0:
            n=-1
        
#1. Share 2 questions you would ask to help understand the question:
#Understand
#Function takesin a list 
#Returns the list in reverse 
#2. Write out in plain English what you want to do: 
#Have two pointers point to first and last index 
#Create temp variable 
# #create new list  
#3. Translate each sub-problem into pseudocode:
#Swap values   
#4. Translate each sub-problem into pseudocode:
#Store values into empy array 
#5. Translate the pseudocode into Python and share your final answer:#1. Share 2 questions you would ask to help understand the question:

def reverse_list(lst):
    pointer1 = 0
    pointer2 = len(lst)-1
    temp = 0 
    while pointer1 < pointer2: 
        temp = lst[pointer2]
        lst[pointer2] = lst[pointer1]
        lst[pointer1]  = temp
        
        pointer1+=1
        pointer2-=1
    return lst

lst = [1,2,3,4,5]
print(reverse_list(lst))


#1. Share 2 questions you would ask to help understand the question:
#Understand
#What is Big O notation?
#What function can I use to print the time it takes for fucntion to complete
#what happens if both sides are odd? do e
#Function takesin a list 
#2. Write out in plain English what you want to do: 

#print out the time when the function finish exectute 
#print out the space 

#3. Translate each sub-problem into pseudocode:
# values   
#4. Translate each sub-problem into pseudocode:
#Store values into empy array 
#5. Translate the pseudocode into Python and share your final answer:#1. Share 2 questions you would ask to help understand the question:



#1. Share 2 questions you would ask to help understand the question:
#Understand
#How can I solve this using the 2 pointer method?
#How can I take care of any edge case
#Function takes in a array
#splits even to left hand
#Splits odd to right hand 
#2. Write out in plain English what you want to do: 
#Declare 2 pointers pointer1 and pointer2
#left points to first letter
#right  points to last letter 
#Declare an array called output 

#What if both are even?
#Move  right by -1
#Leave left side as is 
#What if both are odd? 
#Move left by +1 
#What if left is odd and right is even 
#Swap 
#Store swap values to output

#What if left is even and right is odd
#Leave alone 
#incrrment left by 1 
#Decrement right by 1 
#Increment outside to ensure while loop terminates 
#Loop until the next loop will take care of it 
#5. Translate the pseudocode into Python and share your final answer:#1. Share 2 questions you would ask to help understand the question:

def sort_array_by_parity(nums):
   
    left = 0
    right = len(nums)-1
    while ( left < right):
        if nums[left]%2 == 0 and nums[right]%2 == 0:
            right=-1
        elif nums[left]%2 != 0 and nums[right]%2 != 0:
            left+=1 
        #    ODD                        EVEN
        elif nums[left]%2 != 0 and nums[right]%2 == 0:
           
            leftIndexVal = nums[left]
            nums[left] = nums[right]     
            nums[right] = leftIndexVal 
        else:
            #If left is even and right i odd
            left +=1 
            right -=1
            
      
    return nums
        
print("--------------------------Problem 4----------------------------------")
nums = [3,1,2,4]
nums2 = [0]
print(sort_array_by_parity(nums))
print(sort_array_by_parity(nums2))






#1. Share 2 questions you would ask to help understand the question:
#Understand
#How can I check each letter of a string?
#How can  I use 2 pointer for a string?
#2. Write out in plain English what you want to do: 
#Determine if its a palindrome
    #Create 2 pointers left and right
    #if the length of the word is 0 or 1  return false 
    #if both letters are the same increment unitl left and right intersect
    # if both letters are not the same return false immetidlety 
    #isPalindrome 
#Iterating through the list 
    #Loop through the list
    # call the isPlaindromne function if true immeidalty rreturn the  the word
    

#3. Translate each sub-problem into pseudocode:
#4. Translate each sub-problem into pseudocode:
#5. Translate the pseudocode into Python and share your final answer:#1. Share 2 questions you would ask to help understand the question:



#1. Share 2 questions you would ask to help understand the question:
#Understand
#2. Write out in plain English what you want to do: 


#3. Translate each sub-problem into pseudocode:
#4. Translate each sub-problem into pseudocode:
#5. Translate the pseudocode into Python and share your final answer:#1. Share 2 questions you would ask to help understand the question:


print("--------------------------Problem 5----------------------------------")

