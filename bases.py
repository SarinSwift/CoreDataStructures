#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace



def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)

    answerInt = 0
    # base 10
    if base == 10:
        return int(digits)

    # base 16
    if base == 16:
        hexlookup = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "a":10, "b":11, "c":12,
        "d":13, "e":14, "f":15}
        arrayDigits = list(digits)
        endPointer = len(arrayDigits) - 1
        toThePower = 0
        while endPointer >= 0:
            hex_value = hexlookup[arrayDigits[endPointer]]
            answerInt += hex_value * (16**toThePower)
            endPointer -= 1
            toThePower += 1
        return answerInt

    # base 2 up to 36
    arrayDigits = list(digits)
    endPointer = len(arrayDigits) - 1
    toThePower = 0
    while endPointer >= 0:
        currValue = int(arrayDigits[endPointer])
        answerInt += currValue * (base**toThePower)
        endPointer -= 1
        toThePower += 1
    return answerInt


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)

    answerString = ""

    # base 10
    if base == 10:
        return int(number)

    # base 2
    if base == 2:
        trickArray = [number]

        while trickArray[0] != 1:
            divideNumber = trickArray[0]//2
            trickArray.insert(0, divideNumber)
        for i in range(len(trickArray)):
            if trickArray[i] % 2 == 0:
                # 0 for even numbers
                trickArray[i] = 0
            else:
                # 1 for odd numbers
                trickArray[i] = 1
        return ''.join(str(x) for x in trickArray)

    # base 16
    if base == 16:
        hexdigits = string.printable  # all the bases
        arrayDigits = []
        while number > 0:
            remainder = number % 16
            number = number // 16
            arrayDigits.append(hexdigits[remainder])
        arrayDigits = arrayDigits[::-1]
        return ''.join(str(x) for x in arrayDigits)



    # base 2 up to 36
    printabledigits = string.printable
    arrayDigits = []
    while number > 0:
        remainder = number % base
        number //= base
        arrayDigits.append(printabledigits[remainder])
    arrayDigits = arrayDigits[::-1]
    return ''.join(str(x) for x in arrayDigits)


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    # ...
    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from any base to any base (2 up to 36)
    # ...


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()

    print("\n\ntestinggggg decode base 2")
    print(decode('1', 2)) # -> 1
    print(decode('1010', 2)) # -> 10
    print(decode('1111', 2)) # -> 15

    print("\ntestinggggg decode base 10")
    print(decode('1021', 10))

    print("\ntestinggggg decode base 16")
    print(decode('7de', 16))
    print(decode('c0ffee', 16))
    print(decode('ff', 16))

    print("\ntestinggggg decode base 2-36")
    print(decode('10', 8))
    print(decode('10', 25))
    print(decode('1010', 32))
    print(decode('101101', 4))

    print("\ntestinggggg encode base 10")
    print(encode(789, 10))
    print(encode(99, 10))

    print("\ntestinggggg encode base 16")
    print(encode(10, 16))
    print(encode(3735928559, 16))

    print("\ntestinggggg encode base 2-36")
    print(encode(1234, 8))
    print(encode(1234, 32))
