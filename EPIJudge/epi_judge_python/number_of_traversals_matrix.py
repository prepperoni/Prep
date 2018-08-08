from test_framework import generic_test
import collections

def number_of_ways1(n, m):
    mat = [[False for i in range(m)] for j in range(n)]

    def recurse(x, y):
    	if x < 0 or x >= n or y < 0 or y >= m or mat[x][y]:
    		return 0

    	mat[x][y] = True
    	res = 0

    	if x == n - 1 and y == m - 1:
    		res = 1

    	res += recurse(x + 1, y) + recurse(x, y + 1)
    	mat[x][y] = False
    	return res

    return recurse(0, 0)

def number_of_ways2(n, m):
	ways = [[0 for _ in range(m)] for _ in range(n)]
	ways[0][0] = 1
	q = collections.deque([(0, 1), (1, 0)])

	while q:
		i, j = q.popleft()
		if i >= n or j >= m or ways[i][j] > 0:
			continue
		ways[i][j] = (ways[i - 1][j] if i > 0 else 0) + (ways[i][j - 1] if j > 0 else 0)
		q.append((i, j + 1))
		q.append((i + 1, j))

	return ways[-1][-1]

def number_of_ways(n, m):
	ways = [[0 for _ in range(m)] for _ in range(n)]
	ways[0][0] = 1
	def dfs(i, j):
		if i < 0 or j < 0:
			return 0
		if ways[i][j] > 0:
			return ways[i][j]

		ways[i][j] = dfs(i - 1, j) + dfs(i, j - 1)
		return ways[i][j]

	return dfs(n - 1, m - 1) 



if __name__ == '__main__':   
    exit(
        generic_test.generic_test_main("number_of_traversals_matrix.py",
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
