class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

# create nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

# link nodes
node1.next = node2
node2.next = node3
node3.next = node4

# delete the last node
head = node1
current = head

while current.next.next is not None:
    current = current.next
current.next = None

# print the SSL
current = node1

while current is not None:
    print(current.data, end="->")
    current = current.next
print("None")