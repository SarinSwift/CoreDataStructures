#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    # Pseudocode
    # Guard that str2 has to be shorter than str1 else return false
    # Keep pointers for str1 an str2
    # loop through str1[str1Pointer] until we find str2[str2Pointer]
    # if we find them to be equal:
    #   increase str1Pointer by 1
    #   increase str2Pointer by 1
    #   do a check to see if str2Pointer was the last index of str2. Because that means we have found a pattern!
    # if we don't find it yet:
    #   set the patternPointer to be 0
    #   increase str1Pointer by 1 ONLY IF str1[str1Pointer] != str2[0]
    #   so we don't check on the next letter if this current letter may be the where the pattern begins!!!!

    if len(pattern) > len(text):        # edge case where it will text will never contain the pattern if it's larger
        return False
    if pattern == "":
        return True

    textPointer = 0
    patternPointer = 0
    while textPointer < len(text):
        if text[textPointer] == pattern[patternPointer]:   # matches a pattern letter! so we can move to the next pattern letter
            textPointer += 1
            patternPointer += 1
            if patternPointer == len(pattern):             # All the letters in the pattern have appeard in the text in correct order
                return True
        else:
            patternPointer = 0                             # We want to set to check back at the first letter in the pattern
            # Catches the edge case where the current letter in text might equal to the the pattern's letter.
            if text[textPointer] != pattern[patternPointer]:
                textPointer += 1
            # In this case, we would not want to increment the text's pointer and we can continue our while loop

    return False


def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    # Pseudocode
    # Call the contains method so we can check if there is such pattern or not
    # if it returns true, that means there is the pattern and we can loop through to find the first letter and return it's index
    # if returns false, we can just return None because we know there's nothing in it.

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




def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    # Pseudocode
    # create variable to store empty array where we will be appending indexes and return in the end
    # code similar to contains method

    


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
