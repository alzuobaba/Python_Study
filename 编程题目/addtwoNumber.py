"""
    You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.

    Example

    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        prev = result  =ListNode(None)
        carry =0
        while l1 or l2 or carry:
            if l1:
                carry +=l1.val
                l1 = l1.next
            if l2:
                carry +=l2.val
                l2  =l2.next
            prev.next = ListNode(carry%10)
            prev = prev.next
            carry//=10
        return result.next




l1 = ListNode(2)
l1.next =ListNode(7)
l2 = ListNode(5)
l2.next =ListNode(5)
s = Solution()
result = s.addTwoNumbers(l1,l2)
while result:
    print(result.val)
    result = result.next