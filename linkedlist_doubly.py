
class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)

class LinkedListIter(object):
    def __init__(self, head):
        self.curr = head

    def __next__(self):
        if self.curr == None:
            raise StopIteration
        self.curr = curr.next
        return self.curr



class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None
        self.tail = None
        self.size = 0
        # Append the given items
        if iterable is not None:
            for item in iterable:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def __iter__(self):
        """Iterating through the entire list with an iterator class starting from the head"""
        return LinkedListIter(self.head)

    def items(self):
        """Return a list of all items in this linked list.
        Best and worst case running time: Theta(n) for n items in the list
        because we always need to loop through all n nodes."""
        result = []
        node = self.head
        while node is not None:
            result.append(node.data)
            node = node.next
        return result

    def length(self):
        return self.size

    def is_empty(self):
        """Return True if this linked list is empty, or False."""
        return self.head is None

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        As well as updating the prev node
        Best and worst case run time: O(1) because we have access to the tail so we did not have to traverse through the
            whole list to get to the end """
        # Create a new node to hold the given item
        new_node = Node(item)
        # Check if this linked list is empty
        if self.is_empty():
            # Assign head to new node
            self.head = new_node
        else:
            new_node.previous = self.tail           # new nodes prev to the last item in list
            self.tail.next = new_node               # connect the last item's next to new_node
        # Update tail to new node regardless
        self.tail = new_node
        self.size += 1

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Best and worst case running time: O(1) because we're just changing the pointer of first item"""
        # Create a new node to hold the given item
        new_node = Node(item)
        # Check if this linked list is empty
        if self.is_empty():
            # Assign tail to new node
            self.tail = new_node
        else:
            # Otherwise insert new node before head
            self.head.previous = new_node           # set heads previous to new_node
            new_node.next = self.head               # new_node's next must be the head
        # Update head to new node regardless
        self.head = new_node
        self.size += 1

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: Omega(1) if item is near the head of the list.
        Worst case running time: O(n) if item is near the tail of the list or
        not present and we need to loop through all n nodes in the list."""
        # Start at the head node
        node = self.head
        while node is not None:
            if quality(node.data):
                return node.data
            node = node.next
        return None

    def replace(self, old_item, new_item):
        """Replace the given old_item in this linked list with given new_item
        using the same node, or raise ValueError if old_item is not found.
        Best case running time: O(1) where we're replacing a node at self.head
        Worst case running time: O(n) where n is the index where the old item is """
        curr = self.head                # keep check of current node
        while curr is not None:
            if curr.data == old_item:   # found the old item!
                curr.data = new_item    # set the old data to our new data
                return
            else:
                curr = curr.next        # traverse on the next node

        # no old_item
        raise ValueError('old_item not found: {}'.format(old_item))

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: O(1) where the item is the first item in list
        Worst case running time: O(n) where n is the amount of nodes in list."""
        curr = self.head
        found = False
        while not found and curr is not None:
            if curr.data == item:
                found = True
            else:
                curr = curr.next
        if found:
            if curr is not self.head and curr is not self.tail:
                curr.previous.next = curr.next          # changing previous's next
                curr.next.previous = curr.previous      # changing next's previous

            if curr is self.head:
                self.head = curr.next
                if self.head == None:
                    self.tail = None
                if self.head != None:
                    self.head.previous = None

            if curr is self.tail:
                self.tail = curr.previous
                self.tail.next = None
            self.size -= 1
        else:
            raise ValueError('Item not found: {}'.format(item))

    def get_at_index(self, index):
        """Return the item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size.
        Best case running time: O(1) where we're getting at index 0
        Worst case running time: O(n) where n is the index we want to get"""
        # Check if the given index is out of range and if so raise an error
        if not (0 <= index < self.size):
            raise ValueError('List index out of range: {}'.format(index))
        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.data

    def insert_at_index(self, index, item):
        """Insert the given item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size.
        Best case running time: O(1) if we want to insert at index 0
        Worst case running time: O(n) where n is the index number. Can be the total amount of items in list"""
        # Check if the given index is out of range and if so raise an error
        if not (0 <= index <= self.size):
            raise ValueError('List index out of range: {}'.format(index))

        if index == 0:
            self.prepend(item)
        elif index == self.size:
            self.append(item)
        else:
            new_node = Node(item)
            curr = self.head
            for i in range(index):              # curr will become the node that comes after the new_node we want to insert
                curr = curr.next
            print(curr.data)
            curr.previous.next = new_node       # setting the prev's next of the curr to become new_node
            new_node.next = curr                # setting the new_node to point to correct next node
            new_node.previous = curr.previous   # setting the new_node to point to correct previous node
            curr.previous = new_node            # curr's prev is now the new node instead of the old curr's prev
            self.size += 1



def test_linked_list():
    ll = LinkedList()
    print(ll)

    print('Appending items:')
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))

    print('\nTesting previous nodes:')
    print('heads prev: {}'.format(ll.head.previous))
    print('tails prev: {}'.format(ll.tail.previous))

    print('\nPrepending items:')
    ll.prepend('prepend')
    print(ll)

    print('\nTesting previous nodes:')
    print('head: {}'.format(ll.head))
    print('heads next: {}'.format(ll.head.next))
    print('heads prev: {}'.format(ll.head.previous))

    print('\nDeleting items:')
    print("\ndeleting 'prepend'")
    ll.delete('prepend')
    print(ll)
    print('head: {}'.format(ll.head))
    print('heads nexts previous: {}'.format(ll.head.next.previous))
    print('tails: {}'.format(ll.tail))
    print('tails previous: {}'.format(ll.tail.previous))
    print("\ndeleting 'B'")
    ll.delete('B')
    print(ll)
    print('head: {}'.format(ll.head))
    print('tails previous: {}'.format(ll.tail.previous))
    print("\ndeleting 'C'")
    ll.delete('C')
    print(ll)
    print('head: {}'.format(ll.head))
    print('heads next: {}'.format(ll.head.next))
    print("\ndeleting 'A'")
    ll.delete('A')
    print(ll)
    print('head: {}'.format(ll.head))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
