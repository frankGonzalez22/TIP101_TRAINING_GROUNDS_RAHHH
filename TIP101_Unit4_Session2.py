def get_element_at_index(lst, index):
    if index < 0 or index >= len(lst):
        return None  # Handle out-of-bounds cases
    return lst[index]

#Best Case Scenario: O(1) for time complexity 
#Reasoning: 
#If index is chosen first  in list then its return 
#Worst Case Scenario: O(1) for time complexity
#Reasoning: 
#Theres already an assigned  memory stored for each value in the lst array
#Each index is assoicated with a value. So  instead of iterating through 
#Each number, the associated index can quickly retrieve the value store with assigned index

#Space Complextiy: 
#O(1) We have 1 return statement. The return statement holds a value
#And we return it once for function



def sum_array(arr):
    total = 0
    for num in arr:
        total += num
    return total

#Best Case:
#O(n) if the arr length is only at n = 1 we loop once. However, we are still looping and iterating 
# through the loop so its O(n)
#Worst Case:
#O(n) if the arr length is n, and if we loop through the arr,
# we are incrementing total variable n times

#Space complexity:
#O(1). We have 1 variable total that holds a single value.We returna  single variable


 