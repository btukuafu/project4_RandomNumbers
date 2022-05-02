"""
Sourced from: https://en.wikipedia.org/wiki/Xorshift
Date accessed: April 25th, 2022
"""

import time
state = [time.time_ns() % 4294967296 for x in range(4)]

def xorshift():
	t = state[3]
	
	s = state[0]
	state[3] = state[2]
	state[2] = state[1]
	state[1] = s

	t ^= t << 11
	t ^= t >> 8
	state[0] = (t ^ s ^ (s >> 19)) % 4294967296

	return state[0]

num = xorshift()
print(num)
exit(num)