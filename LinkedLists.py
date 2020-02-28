# Jackson Jared
# 2/20/20
# Creating a class to create singly linked lists
from LinkedList import *


# I am making these to test if i remember the basic methods
def head_add(self, data):
    new = Data(data)
    new.next = self.head
    self.head = new


def head_remove(self):
    remove = self.head
    self.head = self.head.next
    return remove.data


def tail_add(self, data):
    new = Data(data)
    if self.head is None:
        self.head = new
        return
    current = self.head
    while current.next is not None:
        current.next = None
    current.next = new
    return


def tail_remove(self):
    if self.head is None:
        return
    gone = self.head
    previous = self.head
    while gone.next is not None:
        previous = gone
        gone = gone.next
    previous.next = None
    return gone.data


def look(self, looking):
    if self.head.data == looking:
        return True
    search = self.head
    while search.next is not None:
        if search.data == looking:
            return True
        search = search.next
    if search.data == looking:
        return True
    return False


def looking(self, look):
    elements = self.display()
    for element in elements:
        if element == look:
            return True
    return False


def remove_anywhere(self, remove):
    if self.head.data == remove:
        self.head = self.head.next
        return remove
    gone = self.head
    previous = self.head
    while gone.next is not None or gone.data == remove:
        if gone.data == remove:
            previous.next = previous.next.next
            return gone.data
        previous = gone
        gone = gone.next
    else:
        return gone.data
