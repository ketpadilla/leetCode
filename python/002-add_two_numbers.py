# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        temp = ListNode
        res = temp
        carry = 0 

        while l1 is not None or l2 is not None:
            # Get node value
            currl1 = l1.val if l1 else 0
            currl2 = l2.val if l2 else 0

            # Get sum and carry
            total = currl1 + currl2 + carry
            carry = total // 10
            res.next = ListNode(total % 10) 

            # Move to next nodes
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            res = res.next
        
        # Add remaining carry as last node
        if carry > 0:
            res.next = ListNode(carry)

        return temp.next


# Test
if __name__ == '__main__':
  l1 = ListNode(2, ListNode(4, ListNode(3)))
  l2 = ListNode(5, ListNode(6, ListNode(4)))
  res = Solution().addTwoNumbers(l1, l2)
  print(res.val, res.next.val, res.next.next.val)
