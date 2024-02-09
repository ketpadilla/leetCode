## Problem 206. Reverse Linked List
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head # return empty list
        
        newList = None 
        copyHead = head

        while copyHead: 
            nextNode = copyHead.next # save the next node
            copyHead.next = newList # reverse the pointer
            newList = copyHead # move the new list to the next node
            copyHead = nextNode # move the copyHead to the next node
    
        return newList