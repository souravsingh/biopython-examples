#!/usr/bin/env python

""" This is a Program based on Mendel's Law
"""


from scipy.misc import comb
def mendels_first_law(hom, het, rec):
	total = 4*comb(hom+het+rec, 2)
	total_rec = 4*comb(rec, 2) + 2*rec*het + comb(het,2)
	return 1 - total_rec/total

def main():

# Read the input data.
with open('data/mendel.txt') as input_data:
	k, m, n = map(int, input_data.read().strip().split())
prob = str(mendels_first_law(k,m,n))
# Print the output.
print prob
with open('output/mendel.txt', 'w') as output_data:
	output_data.write(prob)

if __name__ == '__main__':
	main()
