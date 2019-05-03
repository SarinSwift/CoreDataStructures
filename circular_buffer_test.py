
from circular_buffer import CircularBuffer
import unittest

class CircularBufferTest(unittest.TestCase):

    def test_init(self):
        c = CircularBuffer(3)
        assert c.size == 0
        assert c.list == [None, None, None]

        CircVal = CircularBuffer(2)
        assert CircVal.size == 0
        assert CircVal.list == [None, None]

    def test_enqueue(self):
        c = CircularBuffer(3)
        c.enqueue(2)
        c.enqueue(3)
        c.enqueue(4)
        assert c.list == [2, 3, 4]

        cc = CircularBuffer(3)
        cc.enqueue(2)
        cc.enqueue(3)
        cc.enqueue(4)
        cc.enqueue(5)
        assert cc.list == [3, 4, 5]
        assert cc.front() == 3

    def test_front(self):
        c = CircularBuffer(3)
        c.enqueue(2)
        assert c.size == 1
        assert c.list == [None, None, 2]
        assert c.front() == 2

    def test_dequeue(self):
        c = CircularBuffer(3)
        c.enqueue(2)
        c.enqueue(3)
        assert c.list == [None, 2, 3]
        assert c.dequeue() == 2
        assert c.list == [None, None, 3]

        cc = CircularBuffer(3)
        cc.enqueue(2)
        cc.enqueue(3)
        cc.enqueue(4)
        cc.enqueue(5)
        assert cc.list == [3, 4, 5]
        assert cc.front() == 3
