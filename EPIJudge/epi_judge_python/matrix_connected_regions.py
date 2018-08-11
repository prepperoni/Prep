from test_framework import generic_test
import collections


#Question 18.2 in the Python EPI book
#DFS approach
def flip_color(x, y, image):
    #image colors are 0 and 1
    start_color = image[x][y]
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def flip(x, y):
        if x >= 0 and x < len(image[0]) and y >= 0 and y < len(image) and image[x][y] == start_color:
            image[x][y] = 1 if start_color == 0 else 0
            
            for d in directions:
                flip(x + d[0], y + d[1])

    flip(x, y)

#BFS Approach
'''
intiial state:
0 1 1 0
1 0 0 1
0 1 0 0

starting point (1, 1)

final state:
0 1 1 0
1 1 1 1
0 1 1 1

'''

def flip_color1(x, y, image):
    #image colors are 0 and 1
    start_color = image[x][y]
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    q = collections.deque([(x,y)])

    while q:
        x_, y_ = q.popleft()
        if x_ >= 0 and x_ < len(image[0]) and y_ >= 0 and y_ < len(image) and image[x_][y_] == start_color:
            image[x_][y_] = 1 if start_color == 0 else 0

            for d in directions:
                q.append((x_ + d[0], y_ + d[1]))



def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_connected_regions.py",
                                       'painting.tsv', flip_color_wrapper))
