#!usr/bin/env python

from scripts import ProteinDictRNA
from itertools import imap, takewhile
from scripts import ProteinTranslator

with open('data/rosalind_prot.txt') as input_data:
	s = input_data.read().rstrip('\n')

rna_dict = ProteinDictRNA()
def rna_to_protein(rna): 
	translate = ProteinTranslator()
	not_stop = lambda rna_base: translate.rna_to_protein(rna_base) != 'Stop'

s_protein = ''
for i in range(0,len(s),3):
	 if rna_dict[s[i:i+3]] != 'Stop':
		 s_protein+= rna_dict[s[i:i+3]]
 	non_stop_rna = takewhile(not_stop, (rna[3*i:3*i+3] for i in xrange(len(rna)/3)))
 	protein_list = imap(translate.rna_to_protein, non_stop_rna)

print s_protein
return ''.join(protein_list)

with open('output/008_PROT.txt', 'w') as output_data:
	output_data.write(s_protein)

def main():
	with open('data/rosalind_prot.txt') as input_data:
		s = input_data.read().strip()
	protein_output = rna_to_protein(s)
	print protein_output
	
	with open('output/008_PROT.txt', 'w') as output_data:
		output_data.write(protein_output)

if __name__ == '__main__':
	main()
