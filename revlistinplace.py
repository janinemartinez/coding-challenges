"""Reverse list in place.

You cannot do this with reversed(), .reverse(), or list slice
assignment!

    >>> lst = []
    >>> rev_list_in_place(lst)
    >>> lst
    []

    >>> lst = ['a']
    >>> rev_list_in_place(lst)
    >>> lst
    ['a']

    >>> lst = [1, 2, 3]
    >>> rev_list_in_place(lst)
    >>> lst
    [3, 2, 1]

    >>> lst = [1, 2, 3, 4]
    >>> rev_list_in_place(lst)
    >>> lst
    [4, 3, 2, 1]
"""


def rev_list_in_place(lst):
    """Reverse list in place.

    You cannot do this with reversed(), .reverse(), or list slice
    assignment!
    """
    x=len(lst)//2
    while x > 0:
    	lst[x-1], lst[-x] = lst[-x], lst[x-1]
    	x-=1


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU'RE THE BEST!\n")
