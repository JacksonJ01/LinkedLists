class Data:
    def __init__(self, data=None):
        self.prev = None
        self.data = data
        self.next = None


class DoubleLinkedListTail:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_head(self, add):
        new_node = Data(add)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return f'{add} has been added to the head'
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        return f'{add} has been added to the head'

    def add_tail(self, add):
        new_node = Data(add)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return f'{add} has been added tail'
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        return f'{add} has been added tail'

    def remove_head(self):
        if self.head is None:
            return 'No value to remove'
        gone = self.head
        self.head = self.head.next
        self.head.prev = None
        return f'{gone.data} has been removed from the head'

    def remove_tail(self):
        if self.head is None:
            return 'No value to remove'
        gone = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        return f'{gone.data} has been removed from the tail'

    def remove(self, remove):
        if self.head is None:
            return 'No value to remove'
        if self.head.data == remove:
            self.head = self.head.next
            self.head.prev = None
            return f'{remove} has been removed from the list'
        gone = self.head
        previous = self.head
        while gone.next is not None or gone.data == remove:
            if gone.data == remove and gone.next is None:
                self.tail = previous
                previous.next = None
                return f'{gone.data} has been removed from the list'
            if gone.data == remove:
                previous.next = previous.next.next
                previous.next.prev = previous
                return f'{gone.data} has been removed from the list'
            previous = gone
            gone = gone.next
        return 'No value to remove'

    def search(self, seek):
        elements = self.display()
        if self.head.data == seek or self.tail.data == seek:
            return True, 'this value is in the list'
        for element in elements:
            if seek == element:
                return True, 'this value is in the list'
        return False, 'this value is not in the list'

    def seek(self, search):
        if self.head.data == search or self.tail.data == search:
            return True, 'this value is in the list'
        current = self.head
        while current.next is not None or current.data == search:
            if current.data == search:
                return True, 'this value is in the list'
            current = current.next
        return False, 'this value is not in the list'

    def display(self):
        elements = []
        current = self.head
        while current.next is not None:
            elements.append(current.data)
            current = current.next
        elements.append(self.tail.data)
        return elements

    def display_bk(self):
        elements = []
        current = self.tail
        while current.prev is not None:
            elements.append(current.data)
            current = current.prev
        elements.append(self.head.data)
        return elements

    def show_ht(self):
        return f'Beginning: {self.head.data} \nEnd: {self.tail.data}'

    def clear_all(self):
        self.head = None
        self.tail = None
        return 'All values cleared'
