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
        return f"{gone.data} was removed from the front of the Linked List."

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

    def search1(self, check=None):
        elements = self.display()
        for element in elements:
            if check == element:
                return True
        return False

    def search2(self, check):
        current = self.head
        if self.head.data == check:
            return True
        while current.next is not None:
            if current.data == check:
                return True
            current = current.next
        return False

    def remove(self, delete):
        gone = self.head
        previous = self.head
        if self.search1(delete) is True:
            if delete == self.head:
                self.head = self.head.next
                return f'Link deleted! {gone.data} is no longer included'
            while gone.next is not None:
                previous = gone
                gone = gone.next
            previous.next = None
            return f'Link deleted! {gone.data} is no longer included'
        return 'No value to remove'

    def display(self):
        elements = []
        if self.head is None:
            print(elements)
            return
        current = self.head
        while current.next is not None:
            elements.append(current.data)
            current = current.next
        elements.append(current.data)
        return elements
