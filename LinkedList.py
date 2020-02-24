class Data:

    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def add_head(self, data):
        new_node = Data(data)
        new_node.next = self.head
        self.head = new_node
        return

    def add_end(self, data):
        new_node = Data(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        return

    def rem_front(self):
        gone = self.head
        self.head = self.head.next
        return gone.data, "was removed from the front of the Linked List."

    def rem_end(self):
        gone = self.head
        previous = self.head
        if self.head is None:
            return "There is nothing to remove."
        while gone.next is not None:
            previous = gone
            gone = gone.next
        previous.next = None
        return gone.data, "was removed from the Linked List."

    def clear_all(self):
        self.head = None
        self.display()
        return

    def search(self, data=None):

        return

    def remove(self):
        self.search()
        return

    def display(self):
        elements = []
        if self.head is None:
            print(elements)
            return
        current = self.head
        while current.next is not None:
            elements.append(current.data)
            current = current.next
        print("The contents in this Linked List are:\n", elements)
