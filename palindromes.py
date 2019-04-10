
#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
LETTERS = frozenset(string.ascii_letters) # dictionary without value


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    return is_palindrome_iterative(text)
    # return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    if len(text) == 0 or len(text) == 1:    # if the text is '' or 'a'
        return True

    start = 0
    end = len(text) - 1

    while start < end:
        if text[start] not in string.ascii_letters:             # need to check the next character to the right
            start += 1
        elif text[end] not in string.ascii_letters:             # need to check the next character to the left
            end -= 1
        else:
            if text[start].lower() != text[end].lower():        # should lower it incase they're in different cases
                return False
            else :
                start += 1
                end -= 1
    return True



def is_palindrome_recursive(text, left=None, right=None):
    # if len(text) == 0 or len(text) == 1:    # if the text is '' or 'a'
    #     return True
    # text = text.replace(".", "").replace(" ", "").replace(",", "").replace("*", "").replace(string.punctuation, "").replace("?", "").replace("!", "").replace(";", "").replace(":", "").replace('“', "").replace('”', "").replace('-', "").replace("'", "")
    # text = text.lower()

    if left == None:                        # first iteration
        left = 0
        right = len(text) - 1

    if left > right:                        # checked the whole string from beginning to end and we know it's a palindrome
        return True

    if text[left] not in string.ascii_letters:
        return is_palindrome_recursive(text, left+1, right)
    if text[right] not in string.ascii_letters:
        return is_palindrome_recursive(text, left, right-1)

    if text[left] != text[right]:           # returns false when we find first pair that's not equal
        if text[left].lower() != text[right].lower():
            return False

    return is_palindrome_recursive(text, left+1, right-1)


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
