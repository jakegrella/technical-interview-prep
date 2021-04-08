'''
Add Two Numbers
https://leetcode.com/problems/add-two-numbers/
4/8/21
'''

'''
add first elem of each linked list together, that's first element of new linked list
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, val=0):
        newnode = ListNode(val)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newnode
        else:
            self.head = newnode


class Solution:
    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        print('hw')
    
ll = LinkedList()
ll.head = ListNode(3)
# add_two_numbers(self, [2,4,3], [5,6,4])
print(ll.head.val)

