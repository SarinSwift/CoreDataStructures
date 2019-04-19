#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text.
    O(n) runtime"""
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
    or None if not found.
    O(n) where n is the index where the last pattern is in the string"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    # Pseudocode
    # Call the contains method so we can check if there is such pattern or not
    # variables for: text pointer, pattern pointer, and one for checking where the pattern ends in the text
    # if it returns true, that means there is the pattern and we can loop through to find the pattern
    #   in order to return the starting point of pattern in the string: we have to calculate answerIndex minus the len of pattern - 1
    # if returns false, we can just return None because we know there's nothing in it.

    if pattern == "":
        return 0
    doesContainPattern = contains(text, pattern)
    if doesContainPattern:
        textPointer = 0
        patternPointer = 0
        answerIndex = 0
        while textPointer < len(text):
            if text[textPointer] != pattern[patternPointer]:
                patternPointer = 0
                if text[textPointer] != pattern[patternPointer]:
                    textPointer += 1

            else:       # letters are equal so may have a chance it's the pattern
                answerIndex = textPointer       # set index to where we found it!
                if patternPointer == len(pattern) - 1:
                    answerIndex -= len(pattern) - 1
                    return answerIndex

                textPointer += 1
                patternPointer += 1

    else:
        return None




def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found.
    O(n) where n is the number of letters in the text"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    if pattern == '':                                   # empty pattern case
        return [i for i in range(len(text))]
    if len(pattern) == 1:                               # single pattern len case
        answerArr = []
        for i in range(len(text)):
            if text[i] == pattern:
                answerArr.append(i)
        return answerArr

    # doesContainPattern = contains(text, pattern)
    # if doesContainPattern:
    answerArr = []
    textPointer = 0
    patternPointer = 0
    # this will keep the index of where the first pattern ended in the text. So if we want to append it to the answerArr,
    #   we'll have to minus it with the (length of the pattern - 1)
    answerIndex = 0
    
    while textPointer < len(text):
        if text[textPointer] != pattern[patternPointer]:

            if patternPointer != 0:
                # set back to 1 + the first letter that matched with pattern we found in the text
                textPointer = textPointer - patternPointer + 1
            else:
                textPointer += 1

            patternPointer = 0              # start looping from beginning of pattern

        else:                               # letters match so may have a chance it's the pattern
            answerIndex = textPointer       # keep check of the pointer of pattern in text
            textPointer += 1                # check on the next letters in both the text and pattern
            patternPointer += 1

            if patternPointer == len(pattern):
                answerIndex -= len(pattern)-1
                answerArr.append(answerIndex)       # found one pattern in the text!
                answerIndex = 0
                # increment textPointer to the second letter following from the beginning of the pattern found in text
                textPointer = textPointer - patternPointer + 1
                patternPointer = 0                  # set back to 0 to check if there are more patterns in text


    return answerArr


# def covers_all_funcs(text, pattern, call):
#     if call == 'contains':
#         # use contains method
#     if call == 'findIndex':
#         # find index
#     if call == 'findAllIndexes':
#         # find all indexes



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
    print(find_all_indexes('aaa', 'aa'))
    main()
