#!python

class CircularBuffer(object):

    def __init__(self, max_size):
        """initialize a new circular buffer that can store at most max_size items."""
        # Initialize a new linked list to store the items
        self.list = []
        self.size = 0
        for i in range(max_size):
            self.list.append(None)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """check if the buffer is empty."""
        return self.size == 0

    def is_full(self):
        """check if the buffer is full."""
        for el in self.list:
            if el == None:
                return False
        return True

    def enqueue(self, item):
        """insert item at the back of the buffer"""
        if self.list[-1] == None:
            self.list[-1] = item
            self.size += 1
        else:
            for i in range(len(self.list)):
                if i+1 == len(self.list):
                    self.list[i] = item
                    break
                else:
                    self.list[i] = self.list[i+1]

        if not self.is_full:
            self.size += 1


    def front(self):
        """return the item at the front of the buffer"""
        if self.size == 0:
            return None
        for el in self.list:
            if el != None:
                return el


    def dequeue(self):
        """remove and return the item at the front of the buffer"""
        if self.size == 0:
            return None
        for (ind, item) in enumerate(self.list):
            if item != None:
                self.list[ind] = None
                self.size -= 1
                return item
