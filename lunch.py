"""Leveret lunch count.

Check that garden is valid::

    >>> garden = [
    ...     [1, 1],
    ...     [1],
    ... ]

    >>> lunch_count(garden)
    Traceback (most recent call last):
    ...
    AssertionError: Garden not a matrix!

    >>> garden = [
    ...     [1, 1],
    ...     [1, 'a'],
    ... ]

    >>> lunch_count(garden)
    Traceback (most recent call last):
    ...
    AssertionError: Garden values must be ints!

Consider simple cases::

    >>> garden = [
    ...     [0, 0, 0],
    ...     [0, 0, 0],
    ...     [0, 0, 0]
    ... ]

    >>> lunch_count(garden)
    0

    >>> garden = [
    ...     [1, 1, 1],
    ...     [0, 1, 1],
    ...     [9, 1, 9]
    ... ]

    >>> lunch_count(garden)
    3

    >>> garden = [
    ...     [1, 1, 1],
    ...     [1, 1, 1],
    ...     [1, 1, 1]
    ... ]

    >>> lunch_count(garden)
    9

Make sure it works with even-sides
(this will start with the 4 and head east)::

    >>> garden = [
    ...     [9, 9, 9, 9],
    ...     [9, 3, 1, 0],
    ...     [9, 1, 4, 2],
    ...     [9, 9, 1, 0],
    ... ]

    >>> lunch_count(garden)
    6

Consider our most complex case::

    >>> garden = [
    ...     [2, 3, 1, 4, 2, 2, 3],
    ...     [2, 3, 0, 4, 0, 3, 0],
    ...     [1, 7, 0, 2, 1, 2, 3],
    ...     [9, 3, 0, 4, 2, 0, 3],
    ... ]

    >>> lunch_count(garden)
    15

"""


def lunch_count(garden):
    """Given a garden of nrows of ncols, return carrots eaten."""

    # Sanity check that garden is valid

    row_lens = [len(row) for row in garden]
    assert min(row_lens) == max(row_lens), "Garden not a matrix!"
    assert all(all(type(c) is int for c in row) for row in garden), \
        "Garden values must be ints!"

    # Get number of rows and columns

    nrows = len(garden)
    ncols = len(garden[0])

    lunch = 0
    midcols = []
    midrows = []

    if nrows%2 == 1:
        midrows.append(int(nrows//2))
    else:
        midrows.append(int(nrows/2-1)), midrows.append(int(nrows/2))
    if ncols%2 == 1:
        midcols.append(int(ncols//2))
    else:
        midcols.append(int(ncols/2-1)), midcols.append(int(ncols/2))
    # print(midrows), print(midcols)
    coords = None

    for j in midcols:
        for i in midrows:
            if coords:
                if garden[j][i] > garden[coords[0]][coords[1]]:
                    coords = [j, i]
            else:
                coords = [j, i]
            print(coords)
            lunch += garden[coords[0]][coords[1]]
            garden[coords[0]][coords[1]] = 0
            print(lunch)
    # print(coords)
    next_value = 0
    while True:
        # import pdb
        # pdb.set_trace()
        if coords[1]-1 >= 0 and garden[coords[1]-1][coords[0]] > next_value:
            next_value = garden[coords[1]-1][coords[0]]
            next_coords = [coords[0]-1, coords[1]]
            print(next_value), print(next_coords)
        elif coords[0]-1 >= 0 and garden[coords[1]][coords[0]-1] > next_value:
            next_value = garden[coords[0]][coords[1]-1]
            next_coords = [coords[0], coords[1]-1]
            print(next_value), print(next_coords)
        elif  coords[1] < len(garden[1]) and garden[coords[1]+1][coords[0]] > next_value:
            next_value = garden[coords[1]+1][coords[0]]
            next_coords = [coords[0]+1, coords[1]]
            print(next_value), print(next_coords)
        elif coords[0] < len(garden) and garden[coords[1]][coords[0]+1] > next_value:
            next_value = garden[coords[1]][coords[0]+1]
            next_coords = [coords[0], coords[1]+1]
            print(next_value), print(next_coords)
        elif next_value > 0:
            lunch += next_value
            next_value = 0
            garden[next_coords[1]][next_coords[0]] = 0
            coords = next_coords
        else:
            break

    print(lunch)


lunch_count([[2, 3, 1, 4, 2, 2, 3], [2, 3, 0, 4, 0, 3, 0], [1, 7, 0, 2, 1, 2, 3], [9, 3, 0, 4, 2, 0, 3]])
lunch_count([[9, 9, 9, 9], [9, 3, 1, 0], [9, 1, 4, 2], [9, 9, 1, 0] ])





# if __name__ == '__main__':
#     import doctest

#     if doctest.testmod().failed == 0:
#         print("\n*** ALL TESTS PASS! HOP ALONG NOW!\n")


