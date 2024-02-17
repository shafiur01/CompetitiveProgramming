# Definition for singly-linked list.
from typing import Type


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
        value = 0
        l3 = Type[ListNode]
        while l1.next:
            l3.val = l1.val + l2.val + value
            if l3.val > 10:
                l3.val = l3.val % 10
                value = l3.val/10
        return l3



