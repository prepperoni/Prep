def change_possibilities(val, coins):
	memo = [0] * (val + 1)
	memo[0] = 1

	for c in coins:
		for i in range(c, val+1):
			memo[i] += memo[i-c]

	return memo[val]

