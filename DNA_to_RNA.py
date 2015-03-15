def dna_to_rna(dna):
	return dna.replace('T', 'U')

def main():


	with open('data/dataset_dna.txt') as input_data:
		dna = input_data.read().strip()
	rna = dna_to_rna(dna)
	print rna

	with open('output/data_RNA.txt', 'w') as output_data:
		output_data.write(rna)

if __name__ == '__main__':
main()

    

