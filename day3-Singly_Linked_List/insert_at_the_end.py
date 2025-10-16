# insert an element the end of the linked list

class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

# create nodes (create the objects of the class Node)
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

# link the nodes to make list
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# create a node to be added at the end of the list
new_node = Node(100)

# traverse to the end of the list
head = node1
current = node1

while current.next is not None:
    current = current.next
current.next = new_node