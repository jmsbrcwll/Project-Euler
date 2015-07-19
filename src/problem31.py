from collections import Counter
from copy import copy
from itertools import combinations

COIN_TYPES = [200, 100, 50, 20, 10, 5, 2, 1]
EXISTING_COINS = []
def run():
	for i in range(0, len(COIN_TYPES)):
		coins_type_subset = COIN_TYPES[i:]
		for j in range(1, len(coins_type_subset)):
			for coins_to_use in combinations(coins_type_subset, j):
				check_new_coin([], 0, coins_to_use)
		
	print len(set(map(str,EXISTING_COINS)))

def check_new_coin(coins, coin_ptr, coins_to_use):
	new_coins = copy(coins)
	new_coins.append(coins_to_use[coin_ptr])
	total = sum(new_coins)
	if total == 200:
		note_combination(new_coins)
	elif total < 200:
		check_new_coin(new_coins, coin_ptr, coins_to_use)
		if coin_ptr < (len(coins_to_use) - 1):
			check_new_coin(new_coins, coin_ptr + 1, coins_to_use)
		
def note_combination(coins):
	global EXISTING_COINS
	counter_coins = Counter(coins)
	EXISTING_COINS.append(counter_coins)


if __name__ == "__main__":
	run()



