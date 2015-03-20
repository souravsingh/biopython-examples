#!/usr/bin/env python
'''

Problem Title: Counting DNA Nucleotides
In this problem We have to count the number of nucleotides present in DNA
'''

from collections import Counter
def base_count_dna(dna):

	base_count = Counter(dna)
	return [base_count[base] for base in 'ACGT']

def main():

# Read the input data.
	with open('data/dna_dataset.txt') as input_data:
		dna = input_data.read().strip()

# Get the count of each base appearing in the DNA sequence.
	base_count = map(str, base_count_dna(dna))

# Print and save the answer.
	print ' '.join(base_count)
	with open('output/DNA_dataset.txt', 'w') as output_data:
		output_data.write(' '.join(base_count))

if __name__ == '__main__':
	main()
