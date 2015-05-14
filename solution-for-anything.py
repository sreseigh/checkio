#!/usr/bin/python

def checkio(x):
    class AlwaysTrue(object):
        def __ne__(self, x):
            return True
        def __eq__(self, x):
            return True
        def __lt__(self, x):
            return True
        def __le__(self, x):
            return True
        def __gt__(self, x):
            return True
        def __ge__(self, x):
            return True
    return AlwaysTrue()

if __name__ == '__main__':
    import re
    import math
    print checkio({}) != []
    print checkio({}) == []
    print checkio('Hello') < 'World'
    print checkio(80) > 81
    print checkio(re) >= re
    print checkio(re) <= math
    print checkio(5) == ord

