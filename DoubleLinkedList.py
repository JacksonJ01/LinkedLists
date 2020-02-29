class Data:

    def __init__(self, data):
        self.previous = None
        self.data = data
        self.next = None


class DoubleLinks:

    def __init__(self):
        self.head = None

    def add_head(self, add):
        new = Data(add)
        new.next = self.head
        if self.head is not None:
            self.head.next.previous = new
        else:
            new.previous = None
        self.head = new
        return

    def add_end(self, add):
        new = Data(add)
        if self.head is None:
            self.head = new
            return
        current = self.head
        curr = self.head
        while current.next is not None:
            curr = current
            current = current.next
        new.previous = curr
        current.next = new
        return

    def remove_head(self):
        return

    def remove_end(self):
        return

    def remove(self, delete):
        return

    def display(self):
        return
