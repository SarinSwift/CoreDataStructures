#!python

from linkedlist_doubly import LinkedList, Node
import unittest


class NodeTest(unittest.TestCase):

    def test_init(self):
        data = 'ABC'
        node = Node(data)
        assert node.data is data
        assert node.next is None


class LinkedListTest(unittest.TestCase):

    def test_init(self):
        ll = LinkedList()
        assert ll.head is None
        assert ll.tail is None
        assert ll.size == 0

    def test_init_with_list(self):
        ll = LinkedList(['A', 'B', 'C'])
        assert ll.head.data == 'A'  # first item
        assert ll.tail.data == 'C'  # last item
        assert ll.size == 3

    def test_items(self):
        ll = LinkedList()
        assert ll.items() == []
        ll.append('B')
        assert ll.items() == ['B']
        ll.prepend('A')
        assert ll.items() == ['A', 'B']
        ll.append('C')
        assert ll.items() == ['A', 'B', 'C']

    def test_length(self):
        ll = LinkedList()
        assert ll.length() == 0
        # append and prepend operations increase length
        ll.append('B')
        assert ll.length() == 1
        ll.prepend('A')
        assert ll.length() == 2
        ll.append('C')
        assert ll.length() == 3
        # delete operations decrease length
        ll.delete('B')
        assert ll.length() == 2
        ll.delete('C')
        assert ll.length() == 1
        ll.delete('A')
        assert ll.length() == 0

    def test_size(self):
        ll = LinkedList()
        assert ll.size == 0
        # append and prepend operations increment size
        ll.append('B')
        assert ll.size == 1
        ll.prepend('A')
        assert ll.size == 2
        ll.append('C')
        assert ll.size == 3
        # delete operations decrement size
        ll.delete('B')
        assert ll.size == 2
        ll.delete('C')
        assert ll.size == 1
        ll.delete('A')
        assert ll.size == 0


    def test_append(self):
        ll = LinkedList()
        ll.append('A')
        assert ll.head.data == 'A'  # new head
        assert ll.tail.data == 'A'  # new tail
        assert ll.size == 1
        ll.append('B')
        assert ll.head.data == 'A'  # unchanged
        assert ll.tail.data == 'B'  # new tail
        assert ll.size == 2
        ll.append('C')
        assert ll.head.data == 'A'  # unchanged
        assert ll.tail.data == 'C'  # new tail
        assert ll.size == 3

    def test_prepend(self):
        ll = LinkedList()
        ll.prepend('C')
        assert ll.head.data == 'C'  # new head
        assert ll.tail.data == 'C'  # new head
        assert ll.size == 1
        ll.prepend('B')
        assert ll.head.data == 'B'  # new head
        assert ll.tail.data == 'C'  # unchanged
        assert ll.size == 2
        ll.prepend('A')
        assert ll.head.data == 'A'  # new head
        assert ll.tail.data == 'C'  # unchanged
        assert ll.size == 3

    def test_find(self):
        ll = LinkedList(['A', 'B', 'C'])
        assert ll.find(lambda item: item == 'B') == 'B'
        assert ll.find(lambda item: item < 'B') == 'A'
        assert ll.find(lambda item: item > 'B') == 'C'
        assert ll.find(lambda item: item == 'X') is None

    def test_delete(self):
        ll = LinkedList(['A', 'B', 'C'])
        ll.delete('A')
        assert ll.head.data == 'B'  # new head
        assert ll.tail.data == 'C'  # unchanged
        assert ll.size == 2
        ll.delete('C')
        assert ll.head.data == 'B'  # unchanged
        assert ll.tail.data == 'B'  # new tail
        assert ll.size == 1
        ll.delete('B')
        assert ll.head is None  # new head
        assert ll.tail is None  # new head
        assert ll.size == 0
        with self.assertRaises(ValueError):
            ll.delete('X')  # item not in list


if __name__ == '__main__':
    unittest.main()
