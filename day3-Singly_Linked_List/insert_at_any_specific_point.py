class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

# create nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

# link the nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# create new node
new_node = Node(100)

# insert the new node at a specific point
# suppose we want to put after 30
target = 30
current = node1
while current is not None and current.data != 30:
    current = current.next

new_node.next = current.next
current.next = new_node

# print the SSL:
head = node1             # reset the reference to the start of SSL
current = head
while current.next is not None:
    print(current.data, end='->')
    current = current.next
print("None")