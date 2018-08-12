import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName


'''
problem 4.11 from elements of programming interviews python -- rectangular intersection

given two rectangles, see if they intersect, and if they do, return the intersected rectangle

Here's an example:
       _______
 _____|B____  |
|A    |     | |
|     |_____|_|
|___________|


A _
|_|  _
    |_|B
'''
Rectangle = collections.namedtuple('Rectangle', ('x', 'y', 'width', 'height'))

def intersect_rectangle(R1, R2):
    # check if they intersect at all first 
    if max(R1.x, R2.x) > min(R1.x + R1.width, R2.x + R2.width) or \
       max(R1.y, R2.y) > min(R1.y + R1.height, R2.y + R2.height):
       return Rectangle(0, 0, -1, -1) #nonexistant rectangle the epi judge wants when there is no intersection
    else:
        return Rectangle(max(R1.x, R2.x), max(R1.y, R2.y), \
                         min(R1.x + R1.width, R2.x + R2.width) - max(R1.x, R2.x), \
                         min(R1.y + R1.height, R2.y + R2.height) - max(R1.y, R2.y))


def intersect_rectangle_wrapper(R1, R2):
    return intersect_rectangle(Rectangle(*R1), Rectangle(*R2))


def res_printer(prop, value):
    def fmt(x):
        return [x[0], x[1], x[2], x[3]] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "rectangle_intersection.py",
            'rectangle_intersection.tsv',
            intersect_rectangle_wrapper,
            res_printer=res_printer))
