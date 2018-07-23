# gallons[i] is the amount of gas in city i, and distances[i] is the
# distance city i to the next city.
def find_ample_city(gallons, distances):
    MPG = sum(distances) // sum(gallons)
    least_gas = 0
    least_gas_city = 0
    current_gas = 0
    
    for i in range(1, len(gallons)):
    	current_gas += gallons[i-1] - distances[i-1] // MPG
    	if current_gas < least_gas:
    		least_gas = current_gas
    		least_gas_city = i

    return least_gas_city


from sys import exit

from test_framework import generic_test, test_utils

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('refueling_schedule.tsv',
                                       find_ample_city))
