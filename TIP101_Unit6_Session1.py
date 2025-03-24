#Helper functions:

#HEADS UP !!!!
#Functions printNodeList() and createdLinkedList(n) are not needed!!!
#THEY ACT AS HELPER FUNCTIONS FOR ME TO TEST THINGS OUT AND LOWKEY LEARN/PRACTICE
#IGNORE THEM
        


class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def printNodeList(head):
        while head:
            if head.next is None:
                print(head.value)
            else:
                print(head.value, end=" -> ")
            head = head.next


#-----------------------IGNORE THIS --------------------------
#How Can I return the address of the head?
#How can I create a new Node a
#This function serves to take in a int n value that determins n ammount of nodes
#Return an adress of head 
#Create the first node store value as n
#If next is none
#create new node again and lnk node to first node
#Repeat N times
#Value of n declines till 1 
def createLinkedList(n):
    head =Node(n)
    output = head
    for i in range(n-1, 0,-1):
        if head.next is None:
            head.next = Node(i)
            
        head = head.next 
        #print("i =" ,head.value)
    return output
#-----------------------IGNORE THIS --------------------------

#1. Share 2 questions you would ask to help understand the question:
#Understand
#How can I nest the nodes into  a single line?
#Answer: Yes it is possible 
#What is the space complexity of this? 
#Answer: O(n) space complextiy . Despite the var holding a address it also holds a 
#connection of 'n' nodes 
#2. Write out in plain English what you want to do create a copy of a node 
#Create a instance of a node or in plain english 
#3. Translate each sub-problem into pseudocode:
#Within that node, input another node in its next paramter 
#4. Translate each sub-problem into pseudocode:
#Repeat until we get 4 -> 3, -> 1
#5. Translate the pseudocode into Python and share your final answer:#1. Share 2 questions you would ask to help understand the question:
#Understand

print("-----------------Problem 1---------------")
head = Node(4, Node(3, Node(2)))
head.printNodeList()

#1. Share 2 questions you would ask to help understand the question:
#Understand
#Can I solve this using a dictionary to store occuranes and linked list?
#Can I solve this with strictly only using  linked list 
#This function takes in a head/linked list  and int value input
#This function returns the count of 'value' in linked list 
#2. Write out in plain English what you want to do: 
#Edge case: If linked list is 1 node and value matches return count 1
#Return 0 if otherwise
#If node DNE return 0
#Loop through linked list
#Declare counter variable called 'count'
#3. Translate each sub-problem into pseudocode:
#If node value has value eqaul to 'val'
#4. Translate each sub-problem into pseudocode:
#Plus 1 by counter
#5. Translate the pseudocode into Python and share your final answer:
print("-----------------Problem 2---------------")

def count_element(head, val):
    count = 0
    while head: 
        if head.value == val:
            count+=1
        head = head.next
    return count


    
head = Node(3,Node(1,Node(2,Node(1, None))))
print((count_element(head,1)))
print("Time complexity: O(n) - We are iterating n nodes times")
print("Space complexity: O(1) we are stroring a single variable that holds an int")



#1. Share 2 questions you would ask to help understand the question:
#Understand
#What are some possible test cases that I can use to test the bug?
#Are there any more edge cases ?
#Can we imlement a dictionary to keep count of this
#2. Write out in plain English what you want to do: 

#Read and understand the 1st 2 edgecases
#Edgecases are reasonable 
#3. Translate each sub-problem into pseudocode:
#Potentnial issue
#while current.next in plain english checks if next node is none
#If the node after the current node DNE then the curret node is the tail
#However outside the while loop, it points the next none existant node as None
#current.next  sets  the current nodes pointer to none
#4. Translate each sub-problem into pseudocode:
#Wihtout using python tutor it seems as if the last node is pointing to None
#outide the while loop. Which explains why the output is the same after calling function
#5. Translate the pseudocode into Python and share your final answer:
#too fix this we set current.next.next 
#We are 2 nodes ahead 
#Once we are at the 2nd last node, set the 2nd last pointer to point none
print("-----------------Problem 3---------------")
def remove_tail(head):
    if head is None: # If the list is empty, return None
        return None
    if head.next is None: # If there's only one node, removing it leaves the list empty
        return None 
		
	# Start from the head and find the second-to-last node
    current = head
    while current.next.next: 
        current = current.next

    current.next = None # Remove the last node by setting second-to-last node to None
    return head
head4 = createLinkedList(5)
head4.printNodeList()
remove_tail(head4)

#1. Share 2 questions you would ask to help understand the question:
#Understand
#What happens if we have even number of nodes? 
# How do ensure we return the value of 2nd Node
#how do we keep track of the 2nd node if their even # of nodes?
#Happy Casae: 3 ->2 ->1 
#Function returns 2  since odd number of nodes
#Worst case: 4->3->2->1
#Function should return 2 since question asl to return 2nd node 
#2. Write out in plain English what you want to do: 
#declare 'slow' and 'fast' pointer pointing to head and '
#3. Translate each sub-problem into pseudocode:
#Move 'fast' pointer by 2 steps until fast pointer reaches the end of list 
#update slow by 1 step 
#4. Translate each sub-problem into pseudocode:
#once fast pointer reaches end return value of slow step 
#5. Translate the pseudocode into Python and share your final answer:
def find_middle_element(head):
    slow = fast = head
    while  fast and fast.next:
        slow =head.next
        fast = head.next.next 
    return slow.value
        

print("-----------------Problem 4---------------")
head = Node(1,Node(2,Node(3,Node(4,None))))
print(find_middle_element(head))
#1. Share 2 questions you would ask to help understand the question:
#Understand

#2. Write out in plain English what you want to do: 
#3. Translate each sub-problem into pseudocode:
#4. Translate each sub-problem into pseudocode:
#5. Translate the pseudocode into Python and share your final answer:
print("-----------------Problem 5---------------")


#1. Share 2 questions you would ask to help understand the question:
#Understand

#2. Write out in plain English what you want to do: 
#3. Translate each sub-problem into pseudocode:
#4. Translate each sub-problem into pseudocode:
#5. Translate the pseudocode into Python and share your final answer:
