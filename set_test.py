
from set import Set
import unittest

class SetTest(unittest.TestCase):

    def test_init(self):
        s = Set()
        assert s.length() == 0
        assert s.all_items() == []

        sVal = Set([3, 4, 5])
        assert sVal.length() == 3
        assert sVal.all_items() == [3, 4, 5]

    def test_contains(self):
        s = Set()
        s.add('I')
        s.add('V')
        s.add('X')
        assert s.contains('I') is True
        assert s.contains('V') is True
        assert s.contains('X') is True
        assert s.contains('A') is False

    def test_add(self):
        s = Set()
        s.add('aaa')
        s.add('bbb')
        s.add('ccc')
        assert s.contains('ccc') is True
        assert s.contains('aaa') is True
        assert s.contains('bbb') is True
        assert s.contains('a') is False

    def test_remove(self):
        s = Set()
        s.add('aaa')
        s.add('bbb')
        s.add('ccc')
        assert s.contains('ccc') is True
        s.remove('ccc')
        assert s.contains('ccc') is False
        assert s.contains('aaa') is True
        assert s.contains('bbb') is True
        assert s.length() == 2

    def test_union(self):
        s_1 = Set([3, 4, 5])
        s_2 = Set([5, 30, 100])
        unionedSet = s_1.union(s_2)
        # assert unionedSet.all_items() == [3, 100, 4, 5, 30]
        assert unionedSet.length() == 5

    def test_intersection(self):
        s_1 = Set([3, 4, 5])
        s_2 = Set([5, 30, 100])
        interedSet = s_1.intersection(s_2)
        assert interedSet.all_items() == [5]
        assert interedSet.length() == 1

        s_11 = Set([3, 4, 5])
        s_22 = Set([5, 30, 100, 3])
        interedSet1 = s_11.intersection(s_22)
        # assert interedSet1.all_items() == [3, 5]
        assert interedSet1.length() == 2

    def test_difference(self):
        s_1 = Set([3, 4, 5])
        s_2 = Set([5, 30, 100])
        differenceSet = s_1.difference(s_2)
        assert differenceSet.all_items() == [3, 4]
        assert differenceSet.length() == 2

        s_11 = Set(['m', 'l', 'a', 'c', 'z', 'w'])
        s_22 = Set(['x', 'n', 'o', 'l', 'a', 'm'])
        differenceSet = s_11.difference(s_22)
        # assert differenceSet.all_items() == ['c', 'z', 'w']
        assert differenceSet.contains('c') == True
        assert differenceSet.contains('z') == True
        assert differenceSet.contains('w') == True

    # def test_symmetric_difference(self):
    #     s_111 = Set([3, 4, 5])
    #     s_222 = Set([5, 30, 100])
    #     diff_set = s_111.symmetric_difference(s_222)
    #     assert diff_set.all_items() == [3,4,30,100]

    def test_subset(self):
        s_1 = Set([2, 4, 6, 8, 10])
        s_2 = Set([2, 10])
        assert s_1.is_subset(s_2) == True

        s_3 = Set([2, 4, 6, 6])             # the set will remove duplicates if the input contains them so should return true
        assert s_1.is_subset(s_3) == True
