```commandline
>>> python -m doctest -v -o NORMALIZE_WHITESPACE morse.py       
Trying:
    encode('CQ')
Expecting:
    '-.-. --.-'
ok
Trying:
    encode('73')
Expecting:
    '--... ...--'
ok
Trying:
    encode('A')
Expecting:
    '.-'
ok
Trying:
    encode('AAAAAAAAAAAAAAAAAAAAAAAA') # doctest: +ELLIPSIS
Expecting:
    '.- ... .-'
ok
Trying:
    encode('SOS')
Expecting:
    '... ---   ...'
ok
Trying:
    encode('sos')
Expecting:
    Traceback (most recent call last):
        ...
    KeyError: 's'
ok
Trying:
    encode(1)
Expecting:
    Traceback (most recent call last):
        ...
    TypeError: 'int' object is not iterable
ok
Trying:
    encode()
Expecting:
    Traceback (most recent call last):
        ...
    TypeError: encode() missing 1 required positional argument: 'message'
ok
2 items had no tests:
    morse
    morse.decode
1 items passed all tests:
   8 tests in morse.encode
8 tests in 3 items.
8 passed and 0 failed.
Test passed.
```