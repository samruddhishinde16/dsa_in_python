# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Function to reverse link list
def reverse_linked_list(head):
    prev = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev


# Function to display linked list
def display(head):
    current = head

    while current is not None:
        print(current.data, end=" -> ")
        current = current.next

    print("None")


# Create linked list
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

print("Original linked list:")
display(head)

head = reverse_linked_list(head)

print("Reversed linked list:")
display(head)

