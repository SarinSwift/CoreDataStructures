#!python

from linkedlist import LinkedList
from hashtable import HashTable


class SetArray(object):

    def __init__(self, elements=None):
        """Initialize this set with the given initial elements."""
        self.items = LinkedList()
        if elements is not None:
            for el in elements:
                self.items.append(el)

    def __iter__(self):
        for el in self.items:
            yield el

    def length(self):
        """returns the length of the set"""
        return len(self.items)

    def all_items(self):
        return self.items

    def contains(self, element):
        """return a boolean indicating whether element is in this set"""
        for el in self.items:
            if el == element:
                return True
        return False

    def add(self, element):
        """add element to this set, if not present already"""
        if self.contains(element) is False:
            self.items.append(element)

    def remove(self, element):
        """remove element from this set, if present, or else raise KeyError"""
        if self.contains(element):
            self.items.remove(element)
        else:
            raise KeyError('Element not found: {}'.format(element))

    def union(self, other_set):
        """return a new set that is the union of this set and other_set"""
        new_set = SetArray()
        for el in other_set:
            new_set.add(el)         # add all elements in other_set
        for el in self:
            new_set.add(el)         # add all elements in our current set
        return new_set              # return both the circles combined

    def intersection(self, other_set):
        """return a new set that is the intersection of this set and other_set"""
        new_set = SetArray()            # create empty Set
        for el in other_set:
            if self.contains(el):
                new_set.add(el)             # only add elements if in both sets
        return new_set                      # return the middle circle (between X and Y)

    def difference(self, other_set):
        """return a new set that is the difference of this set and other_set"""
        new_set = SetArray(self.all_items())            # creating a new_set with the same data in our current set
        intersect_set = new_set.intersection(other_set)     # finding elements in both self and other_set
        for el in intersect_set:
            new_set.remove(el)                              # remove all items in the middle circle
        return new_set                                      # return X - Y

    def is_subset(self, other_set):
        """return a boolean indicating whether other_set is a subset of this set"""
        for el in other_set:
            print(el)
            if not self.contains(el):
                return False
        return True


class SetLinkedList(object):

    def __init__(self, elements=None):
        """Initialize this set with the given initial elements."""
        self.items = LinkedList()
        if elements is not None:
            for el in elements:
                self.items.append(el)

    def __iter__(self):
        for el in self.all_items():
            yield el

    def length(self):
        """is a method so we don't need to update every time we add or remove from the set!"""
        return self.items.length()

    def all_items(self):
        return self.items.items()

    def contains(self, element):
        """return a boolean indicating whether element is in this set"""
        if self.items.find(lambda item: item == element) is not None:
            return True
        return False

    def add(self, element):
        """add element to this set, if not present already"""
        if not self.contains(element):
            self.items.append(element)

    def remove(self, element):
        """remove element from this set, if present, or else raise KeyError"""
        self.items.delete(element)              # delete method on this hash table will raise value error if no element

    def union(self, other_set):
        """return a new set that is the union of this set and other_set"""
        new_set = SetLinkedList()
        for el in other_set:
            new_set.add(el)         # add all elements in other_set
        for el in self:
            new_set.add(el)         # add all elements in our current set
        print(new_set.all_items())
        return new_set              # return both the circles combined

    def intersection(self, other_set):
        """return a new set that is the intersection of this set and other_set"""
        new_set = SetLinkedList()            # create empty Set
        for el in other_set:
            if self.items.find(lambda item: item == el) is not None:
                new_set.add(el)             # only add elements if in both sets
        return new_set                      # return the middle circle (between X and Y)

    def difference(self, other_set):
        """return a new set that is the difference of this set and other_set"""
        new_set = SetLinkedList(self.all_items())            # creating a new_set with the same data in our current set
        intersect_set = new_set.intersection(other_set)     # finding elements in both self and other_set
        for el in intersect_set:
            new_set.remove(el)                              # remove all items in the middle circle
        return new_set                                      # return X - Y

    def is_subset(self, other_set):
        """return a boolean indicating whether other_set is a subset of this set"""
        for el in other_set:
            print(el)
            if self.items.find(lambda item: item == el) is None:
                return False
        return True





class SetHashTable(object):
    def __init__(self, elements=None):
        """Initialize this set with the given initial elements."""
        self.items = HashTable()
        # self.size = self.items.length()
        if elements is not None:
            for el in elements:
                # we know that the hash tables will always have unique keys!
                self.add(el)      # setting the key and value to be the same!

    def __iter__(self):
        for el in self.all_items():
            yield el

    def length(self):
        """is a method so we don't need to update every time we add or remove from the set!"""
        return self.items.length()

    def all_items(self):
        return self.items.keys()

    def contains(self, element):
        """return a boolean indicating whether element is in this set"""
        return self.items.contains(element)

    def add(self, element):
        """add element to this set, if not present already"""
        # setting the same data within tuples will point to the same data within the tuple.
        # so, we're really not creating 2 different elements, but instead, we're making the tuple for the key and value to
        #   point to 1 value
        # TIP: can also store the value as None ex. set(element, None) But it basically takes up the same space as below
        self.items.set(element, element)        # set method on this hash table will calculate duplicates for you

    def remove(self, element):
        """remove element from this set, if present, or else raise KeyError"""
        self.items.delete(element)              # delete method on this hash table will raise value error if no element

    def union(self, other_set):
        """return a new set that is the union of this set and other_set"""
        new_set = other_set
        for el in self:
            new_set.add(el)         # add all elements in our current set
        return new_set              # return both the circles combined

    def intersection(self, other_set):
        """return a new set that is the intersection of this set and other_set
        runtime: O(n) where n is the amount of items in the smaller set.
            or in other words, O(min(n, m))"""
        # create empty Set
        new_set = SetHashTable()

        # determining which set is smaller so we can save time when looping through!
        if other_set.length() >= self.length():
            big_set = other_set
            small_set = self
        else:
            big_set = self
            small_set = other_set

        # loop over elements in smaller set
        for el in small_set:
            if big_set.contains(el):
                new_set.add(el)             # only add elements if it's in both sets

        return new_set                      # return the middle circle (between X and Y)

    def difference(self, other_set):
        """return a new set that is the difference of this set and other_set
        runtime: O(n) where n is the amount of items in the """
        new_set = SetHashTable(self.all_items())            # creating a new_set with the same data in our current set
        intersect_set = new_set.intersection(other_set)     # finding elements in both self and other_set
        for el in intersect_set:
            new_set.remove(el)                              # remove all items in the middle circle
        return new_set                                      # return X - Y

    def symmetric_difference(self, other_set):
        """finding union - intersection"""
        union_set = self.union(other_set)
        inter_set = self.intersection(other_set)

        for el in inter_set:
            union_set.remove(el)

        return union_set

    def is_subset(self, other_set):
        """return a boolean indicating whether other_set is a subset of this set"""
        for el in other_set:
            print(el)
            if not self.contains(el):
                return False
        return True



def test_set_array():
    s = SetArray()
    print(s.items)
    print(s.length())

    s.add('aaa')
    s.add('bbb')
    s.add('ccc')
    print(s.items)
    print(s.length())

    sInit = SetArray([3, 4, 'aaa', 'bbb'])
    print(sInit.items)
    print(sInit.length())

    print("\nTesting union")
    print(s.all_items())
    print(sInit.all_items())
    print(s.union(sInit))

def test_set_hashTable():
    s = SetHashTable()

    s.add('aaa')
    s.add('bbb')
    s.add('aaa')        # should not contain duplicates in self.items
    print(s.all_items())
    print(s.length())

    print("\nTesting init")
    sInit = SetHashTable([3, 4, 'aaa', 'bbb'])
    print(sInit.all_items())
    print(sInit.length())

    print("\nTesting intersection")
    print(s.all_items())
    print(sInit.all_items())
    print(s.intersection(sInit).all_items())

if __name__ == '__main__':
    # test_set_array()
    test_set_hashTable()


# Set = SetArray
Set = SetHashTable
# Set = SetLinkedList
