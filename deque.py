#!python

from linkedlist_doubly import LinkedList

class LinkedDeque(object):

    # Setting our front as the head of the doubly linked list
    def __init__(self, iterable=None):
        """Initialize this deque and push_back the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push_back(item)

    def __repr__(self):
        """Return a string representation of this deque."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this deque is empty, or False otherwise."""
        return self.list.is_empty()

    def length(self):
        """Return the number of items in this deque."""
        return self.list.length()

    def push_front(self, item):
        """Insert the given item at the front of the linkedlist.
        Running time: O(1) calling the ll prepend method by just changing the head node"""
        self.list.prepend(item)

    def push_back(self, item):
        """Insert the given item at the back of this deque.
        Running time: O(1) calling the ll append method by just changing the tail node"""
        self.list.append(item)

    def front(self):
        """Return the item at the front of this deque without removing it,
        or None if this deque is empty."""
        if self.length() != 0:
            return self.list.head.data      # returning the head
        else:
            return None

    def back(self):
        """Return the item at the end of this deque without removing it,
        or None if this deque is empty."""
        if self.length() != 0:
            return self.list.tail.data      # returning the tail
        else:
            return None

    def pop_front(self):
        """Remove and return the item at the front of this deque,
        or raise ValueError if this deque is empty.
        Running time: O(1) from getting the front item and removing at the head of the ll"""
        if self.length() != 0:
            front_item = self.front()
            self.list.delete(front_item)
            return front_item
        else:
            raise ValueError('No items in list to pop_front: []')

    def pop_back(self):
        """Remove and return the item at the back of this deque,
        or raise ValueError if this deque is empty.
        Running time: O(1) from getting the back item and removing at the tail of the ll"""
        if self.length() != 0:
            back_item = self.back()
            self.list.delete(back_item)
            return back_item
        else:
            raise ValueError('No items in list to pop_back: []')

Deque = LinkedDeque

# if __name__ == '__main__':
#     deque = LinkedDeque()
#     print(deque)
#     assert deque.front() is None
#     assert deque.length() == 0
#     assert deque.is_empty() is True
