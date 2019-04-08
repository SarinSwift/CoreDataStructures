#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests
    if index > len(array)-1:        # captures an invalid index
        return None
    # the 'is' keyword will check if both sides are exactly the same object: similar to '===' in swift
    elif array[index] == item:
        return index
    else:
        # Going to the next index
        return linear_search_recursive(array, item, index + 1)
        # return linear_search_recursive(array[1:], item, index + 1) <-- this can be done but works very
                                                                       # slow becasue we have to copy the array of count n-1


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # runtime: Olog(n) -- Dividing the size of data by half. So it's very slow growing
    # Best case: O(1) - time & O(1) - space
    # Worst case: O(logn)
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests
    left = 0                            # low_bound
    right = len(array) - 1
    while left <= right:
        middleIndex = (left + right) // 2
        middleVal = array[middleIndex]
        if middleVal == item:
            return middleIndex          # Found item
        if middleVal < item:            # need to search in the right side of array
            left = middleIndex + 1
        elif middleVal > item:          # need to search in the left side of array
            right = middleIndex - 1


def binary_search_recursive(array, item, left=None, right=None):
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
    if right == None:                   # instantiating for the first iteration
        left = 0
        right = len(array) - 1
    elif left > right:                  # will end if the recursion has gon too far (intersecting)
        return None
    middleIndex = (left + right) // 2
    middleVal = array[middleIndex]
    if middleVal == item:
        return middleIndex
    if middleVal < item:                # need to search in the right side of array
        left = middleIndex + 1
    elif middleVal > item:              # need to search in the left side of array
        right = middleIndex - 1

    return binary_search_recursive(array, item, left, right)
