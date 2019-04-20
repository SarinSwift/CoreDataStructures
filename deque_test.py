#!python

from deque import Deque
import unittest


class DequeTest(unittest.TestCase):

    def test_init(self):
        dq = Deque()
        assert dq.front() is None
        assert dq.length() == 0
        assert dq.is_empty() is True

    def test_init_with_list(self):
        q = Deque(['A', 'B', 'C'])
        assert q.front() == 'A'
        assert q.length() == 3
        assert q.is_empty() is False

    def test_length(self):
        q = Deque()
        assert q.length() == 0
        q.push_front('A')
        assert q.length() == 1
        q.push_front('B')
        assert q.length() == 2
        q.pop_front()
        assert q.length() == 1
        q.pop_front()
        assert q.length() == 0

    def test_push_front(self):
        q = Deque()
        q.push_front('A')
        assert q.front() == 'A'
        assert q.length() == 1
        q.push_front('B')
        assert q.front() == 'B'
        assert q.length() == 2
        q.push_front('C')
        assert q.front() == 'C'
        assert q.length() == 3
        assert q.is_empty() is False

    def test_push_back(self):
        q = Deque()
        q.push_back('A')
        assert q.front() == 'A'
        assert q.length() == 1
        q.push_back('B')
        assert q.front() == 'A'
        assert q.length() == 2
        q.push_back('C')
        assert q.front() == 'A'
        assert q.length() == 3
        assert q.is_empty() is False

    def test_pop_back(self):
        q = Deque(['A', 'B', 'C'])
        assert q.pop_back() == 'C'
        assert q.length() == 2
        assert q.back() == 'B'
        assert q.pop_back() == 'B'
        assert q.back() == 'A'
        assert q.length() == 1
        assert q.pop_back() == 'A'
        assert q.length() == 0
        assert q.is_empty() is True
        with self.assertRaises(ValueError):
            q.pop_back()

    def test_pop_front(self):
        q = Deque(['A', 'B', 'C'])
        assert q.back() == 'C'
        assert q.pop_front() == 'A'
        assert q.length() == 2
        assert q.pop_front() == 'B'
        assert q.length() == 1
        assert q.pop_front() == 'C'
        assert q.length() == 0
        assert q.is_empty() is True
        with self.assertRaises(ValueError):
            q.pop_front()

if __name__ == '__main__':
    unittest.main()
