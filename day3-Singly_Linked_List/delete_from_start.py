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
