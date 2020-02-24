# Jackson Jared
# 2/20/20
# Creating a class to create singly linked lists


# We need a nodes class to hold the data we want to enter and have a pointer to another node
class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def rep(self):
        return repr(self.data)


# This class is how we utilize the data we put in the Node class
class LinkedList:
    def __init__(self):
        self.head = Node()

# This method prepends, adding to the beginning of the head of the program
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

# This method appends, meaning it adds to the end
    def append(self, data):
        new_node = Node(data)
        current = self.head
        if self.head is None:
            self.head = new_node
        while current.next is not None:
            current = current.next
        current.next = new_node

    def erase_all(self):
        self.head = None

# This displays the contents of the list
    def display(self):
        elements = []
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            elements.append(current_node.data)
        print(elements)

# This displays the length of the LinkedList
    def length(self):
        current = self.head
        total = 0
        while current.next is not None:
            total += 1
            current = current.next
        return total

# This method erases a node from the list
    def erase(self, index):
        if index >= self.length():
            print("Error 'Erase' Index out of range!")
            return
        current_index = 0
        current_node = self.head
        while True:
            last_node = current_node
            current_node = current_node.next
            if current_index == index:
                last_node.next = current_node.next
                return
            current_index += 1
