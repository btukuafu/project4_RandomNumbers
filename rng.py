"""
Sourced from: https://en.wikipedia.org/wiki/Xorshift
Date accessed: April 25th, 2022
"""

import time

MAX_INT32 = 4294967296
state = [time.time_ns() % MAX_INT32 for x in range(4)]

def xorshift():
	t = state[3]

	s = state[0]
	state[3] = state[2]
	state[2] = state[1]
	state[1] = s

	t ^= t << 11
	t ^= t >> 8	# t = t ^ (t >> 8)
	state[0] = (t ^ s ^ (s >> 19)) % MAX_INT32

	return state[0]

if __name__ == "__main__":
	num = xorshift()
	print(num)
	exit(num)