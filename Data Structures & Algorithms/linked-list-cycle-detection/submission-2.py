# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #if no cycle, eventually we will get to the end of the list
        #if there is a cycle, we wont ever get to the end

        #we can use a fast and a slow pointer to iterate through
        #the linkedlist

        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False