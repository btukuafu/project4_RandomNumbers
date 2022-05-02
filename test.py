import os
import rng

import statistics as stats

def rng_cmd():
	return os.system("cmd /c python rng.py") % 52

def rng_import():
	return rng.xorshift() % 52

def test_rng(generator, iter = 200):
	distribution = [0] * 52
	for i in range(iter):
		distribution[generator()] += 1

	return distribution

iterations = 1000000
dist = test_rng(rng_import, iterations)
percents = [int(x/iterations*10000)/100 for x in dist]
print(dist)
print(stats.stdev(dist))
print(percents)
print(stats.mean(percents))