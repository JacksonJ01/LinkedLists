# Jackson Jared
# 02/26/20
# This file will contain the 2 classes that will allow the creation and alteration of LinkedLists


# This creates the Data class which will allow the insertion of data along with its node, or pointer to the next Link
class Data:

    def __init__(self, data=None):
        self.data = data
        self.next = None


# This is the LinkedLink class which
class LinkedList:

    # Creates the head node, which points to the list
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

    def search1(self, check):
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
        if current.data == check:
            return True
        return False

    # For these methods, remove1 and remove2, I had the problem where i set the previous.next to None and that got rid of the list.
    # It took me a while to realize i needed to set it equal to previous.next.next
    # Because previous.next points to the data that points to the rest of the list and i got rid of that piece.
    # These 2 methods only delete things if it isn't the 1st or last node
    def remove1(self, delete):
        if delete == self.head.data:
            self.head = self.head.next
            return
        gone = self.head
        previous = self.head
        if self.search1(delete) is True:
            while gone.next is not None or gone.data == delete:
                if gone.data == delete:
                    previous.next = previous.next.next
                    return f'Link deleted! {gone.data} is no longer included'
                previous = gone
                gone = gone.next
            return f'Link deleted! {gone.data} is no longer included'
        return 'No value to remove'

# adding .data to the end of the if delete == self.head made it work, along with adding the or done.data == delete for these 2 remove methods
    def remove2(self, delete):
        if delete == self.head.data:
            self.head = self.head.next
            return
        gone = self.head
        previous = self.head
        while gone.next is not None or gone.data == delete:
            if gone.data == delete:
                previous.next = previous.next.next
                return f'{gone.data} has been removed'
            previous = gone
            gone = gone.next
        else:
            return 'No data to remove'

    def remove3(self, delete):
        elements = self.display()
        current = self.head
        delete_this = 0
        for element in elements:
            if delete == element:
                delete_this += 1
        while current.next != delete_this:
            print()
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
        elements.append(current.data)
        return elements

    def dis_elm(self):
        return f'\nThe items in this Linked List are:\n{self.display()}'

    def clear_all(self):
        self.head = None
        self.dis_elm()
        return
