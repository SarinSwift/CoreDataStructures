#!python

from linkedlist import LinkedList


# Implement LinkedQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class LinkedQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        return self.list.is_empty()

    def length(self):
        """Return the number of items in this queue."""
        return self.list.length()

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(1) calling the ll append method by just changing the tail node"""
        self.list.append(item)      # adding to end of list

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        if self.length() != 0:
            return self.list.head.data      # returning the head
        else:
            return None

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(1) from getting the front item and removing at the head of the ll"""
        if self.length() != 0:
            frontItem = self.front()
            self.list.delete(frontItem)     # removing the head of list
            return frontItem
        else:
            raise ValueError('No items in list to dequeue: []')


# Implement ArrayQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class ArrayQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        if len(self.list) == 0:
            return True
        else:
            return False

    def length(self):
        """Return the number of items in this queue."""
        return len(self.list)

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(1) using append method on list"""
        self.list.append(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        if self.list:               # if list is not empty then return the first item
            return self.list[0]
        return None

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(1) removing the first item in ll"""
        if not self.is_empty():
            return self.list.pop(0)
        raise ValueError('No items in list to dequeue: []')


# Implement LinkedQueue and ArrayQueue above, then change the assignment below
# to use each of your Queue implementations to verify they each pass all tests
Queue = LinkedQueue
# Queue = ArrayQueue
