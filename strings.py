#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    if len(pattern) > len(text):
        return False
    if pattern == "":
        return True
    str1Pointer = 0
    str2Pointer = 0
    while str1Pointer < len(text) and str2Pointer < len(pattern):
        if text[str1Pointer] == pattern[str2Pointer]:
            if str2Pointer == len(pattern) - 1:
                return True
            str1Pointer += 1
            str2Pointer += 1
        elif text[str1Pointer] != pattern[str2Pointer]:
            str1Pointer += 1
    return False


    # Psuedocode
    # Keep pointers for str1 an str2
    # Guard that str2 has to be shorter than str1 else return false
    # loop through str1[str1Pointer] until we find str2[str2Pointer]
    # if we find it:
    #   increase str1Pointer by 1
    #   increase str2Pointer by 1
    # if we don't find it yet:
    #   increase str1Pointer by 1


def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    if pattern == "":
        return 0
    doesContainPattern = contains(text, pattern)
    if doesContainPattern:
        pointer = 0
        while pointer < len(text):
            if text[pointer] == pattern[0]:
                return pointer
            pointer += 1
    else:
        return None

    # Psuedocode
    # Call the contains method so we can check if there is such pattern or not
    # if it returns true, that means there is the pattern and we can loop through to find the first letter and return it's index
    # if returns false, we can just return None because we know there's nothing in it.


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
