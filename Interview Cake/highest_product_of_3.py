def highest_product_of_3(list_of_ints):

    # bigsibilities: 3 bigitive ints, or two negative ints and one bigitive
    res = None

    if len(list_of_ints) < 3:
    	return 0

    neg1 = neg2 = float('inf')
    big1 = big2 = big3 = -float('inf')
    hasZero = False

    for x in list_of_ints:
    	if x == 0: 
    		hasZero = True
    	if x < 0:
			if x < neg1:
				neg1, neg2 = neg2, neg1
				neg1 = x
			elif x < neg2:
				neg2 = x
        if x > big1:
			big2, big3 = big3, big2
			big1, big2 = big2, big1
			big1 = x
        elif x > big2:
			big2, big3 = big3, big2
			big2 = x
        elif x > big3: 
			big3 = x

    if big3 > 0:
    	res = big1 * big2 * big3
    if neg2 != -float('inf') and big1 > 0:
    	res = max(res, neg2 * neg2 * big1)
    if big1 < 0:
    	res = max(res, big1*big2*big3)
    if hasZero:
    	res = max(res, 0)
    return res