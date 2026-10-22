import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(seed = sum([ord(c) for c in "dsci_club"]))
plt_cnt = 1
n = 500

def make_data(dist, relation = None):
	global plt_cnt

	if relation:
		rel = relation(dist)
		rel = rel + (rng.normal(0, np.var(dist) // 5, size = n))

	with open(f"data/plot{plt_cnt}.csv", 'w') as w:
		wr = ','.join([str(i) for i in dist])
		if relation:
			wr += '\n'
			wr += ','.join([str(i) for i in rel])
		w.write(wr)

	plt_cnt += 1

# Plot 1
make_data(rng.normal(0, 1, size = n))
# Plot 2
make_data(rng.binomial(35, 0.90, size = n))
# Plot 3
make_data(rng.binomial(200, 0.5, size = n) / 200)
# Plot 4
make_data((rng.integers(1, 101, size = 200) <= 55) + 0)
# Plot 5
a = np.round(rng.exponential(100/45, size = n)) - 1
make_data(a)
# Plot 6
make_data(np.array([np.mean(np.random.choice(a, 5*n)) for i in range(n)]))
