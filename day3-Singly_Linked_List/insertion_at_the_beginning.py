# insert a node at the beginning of the list

class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

# create objects
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


# create a reference
head = node1

# create a new node 
new_node = Node(60)                 # data = 60, new_node.next = None
new_node.next = head

# recreate a reference making the new node as a new reference
head = new_node


# print the list
current = head

while current is not None:
    print(current.data, end='->')
    current = current.next
print("None")
