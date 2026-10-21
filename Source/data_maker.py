import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(seed = sum([ord(c) for c in "rattlehead"]))

plot_cnt = 1
n = 200


def make_data(dist, relation = None):
	global plot_cnt

	if relation:
		rel = relation(dist)
		rel = rel + relation(rng.normal(0, 2, size = n))

	with open(f"data/plot{plot_cnt}.csv", 'w') as w:
		wr = ','.join([str(i) for i in dist])
		if relation:
			wr += '\n'
			wr += ','.join([str(i) for i in rel])
		w.write(wr)

	plot_cnt += 1

make_data(rng.normal(0, 1, size = n))
make_data(rng.binomial(35, 0.90, size = n))
make_data(rng.normal(10,5, size = n), relation = (lambda x: 2*x))
