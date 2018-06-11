def num_moves(initial, final):
	num_moves = 0
	car_to_idx = {}
	empty_idx = None

	for i, v in enumerate(initial):
		if v == 0:
			empty_idx = i
			continue
		if final[i] != v:
			car_to_idx[v] = i

	while car_to_idx:
		if final[empty_idx] == 0:
			rand_car = list(car_to_idx.keys())[0]
			rand_car_idx = car_to_idx[rand_car]
			
			initial[empty_idx] = rand_car
			initial[rand_car_idx] = 0
			car_to_idx[rand_car] = empty_idx
			empty_idx = rand_car_idx
			num_moves += 1
		else:
			moved_car = final[empty_idx]
			moved_car_old_idx = car_to_idx[moved_car]
			
			initial[empty_idx] = moved_car
			initial[moved_car_old_idx] = 0
			empty_idx = moved_car_old_idx
			car_to_idx.pop(moved_car)
			num_moves += 1

	return num_moves

print(num_moves([0,4,2,3,1],[1, 2, 3, 4, 0]))