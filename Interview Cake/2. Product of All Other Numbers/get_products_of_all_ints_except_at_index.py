'''
20 20 5 5 1 

 3  1 4 1 5

'''

def get_products_of_all_ints_except_at_index(A):
	res = []
	prodSoFar = 1
	prodArr = [1] * len(A)

	for x in range(len(A) - 2, -1, -1):
		prodArr[x] = prodArr[x+1] * A[x+1]

	for i in range(len(A)):
		res.append(prodSoFar * prodArr[i])
		prodSoFar *= A[i]

	return res

print(get_products_of_all_ints_except_at_index([3,1,4,1,5]))