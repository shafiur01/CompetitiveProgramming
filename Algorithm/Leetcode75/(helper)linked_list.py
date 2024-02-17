class linkedListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


class linkedList:
        def __init__(self, head=None):
            self.head = head

        def insert(self, value):
            node = linkedListNode(value)
            if self.head is None:
                self.head = node
                return
            current_node = self.head
            while True:
                if current_node.next_node is None:  # it will be true only if the current node is the tail node
                    current_node.next_node = node
                    break
                current_node = current_node.next

        def toString(self):
            current_node = self.head
            while current_node is not None:
                print(current_node.value, "-> ", end="")
                current_node = current_node.next
            print("None")


l1 = linkedList()
l1.toString()

l1.insert("22")
l1.toString()

l1.insert("33")
l1.toString()

l1.insert("44")
l1.toString()