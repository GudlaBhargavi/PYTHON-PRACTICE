class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating nodes
head = Node(10)
second = Node(20)

head.next = second

print(head.data)
print(head.next.data)