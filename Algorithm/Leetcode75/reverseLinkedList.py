# class Solution(object):
#     def __init__(self):
#         print("hello Shafiur")
#
#     def reverseList(self, head):
#         # none| 1(h) -> 2 -> 3 -> 4
#         prev = None
#         while head:
#             tmp = head
#             head = head.next
#             tmp.next = prev
#             prev = tmp
#
#         return prev
#
# if __name__ == "__main__":
#     reversed_Linked_list = Solution()
#     listToBeReversed = []
#     print(reversed_Linked_list.reverseList(listToBeReversed))


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



# 1-> 2-> 3-> 4-> 5 (Head)
# None <-1 <-2 <-3 <-4 <-5(previous) <-None
# at the last iteration 5 will be the previous so if we return the previous then we'll return the whole linked list

class Solution:
    def reverseList(self, head: ListNode):
        previous = None
        while head:
            temp = head.next  # 2
            head.next = previous
            previous = head
            head = temp
        return previous


Sol = Solution()
l1 = linkedList()
l1.insert(1)
l1.insert(2)
l1.insert(3)
l1.insert(4)
l1.insert(5)
print(l1.toString())

X = Sol.reverseList(l1.head)

while X is not None:
    print(X.val, "-> ", end="")
    X = X.next
print("None")
