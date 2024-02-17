# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class linkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, val):
        node = ListNode(val)
        if self.head is None:
            self.head = node
            return
        current_node = self.head
        while True:  # this means while the current_node.next is not None
            if current_node.next is None:  # it will be true only if the current node is the tail node
                current_node.next = node
                break
            current_node = current_node.next

    def toString(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.val, "-> ", end="")
            current_node = current_node.next
        print("None")


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2 : ListNode):
        dummyNode = ListNode()  # just making an empty/dummy Linked list at first with which we can work later
        current = dummyNode     # referencing the dummyNode to the variable named current

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10

            # the two steps below are very important
            # making a new Linked List
            current.next = ListNode(val)    # Here we're making the new linked List which will contain the sum of the other two linked list

            # updating the pointers
            current = current.next      # Updating the current node of the summation Linked List.

            l1 = l1.next if l1 else None  # that means l1 = l1.next if l1 is not None, if l1 is none then
            l2 = l2.next if l2 else None

        return dummyNode.next


l1 = linkedList()
l1.insert(2)
l1.insert(3)
l1.insert(4)
l1.toString()

l2 = linkedList()
l2.insert(5)
l2.insert(7)
l2.insert(8)
l2.toString()
print("\n")


solution = Solution()
result = solution.addTwoNumbers(l1.head, l2.head)

while result is not None:
    print(result.val, "-> ", end="")
    result = result.next
print("None")