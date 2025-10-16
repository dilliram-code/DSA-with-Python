class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node
    

# initialize the nodes (creating objects of class Node)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)


# link the nodes to form a linked list
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

# print the linked list
current = node1
while current is not None:
    print(current.data, end='->')
    current = current.next
print("None")
