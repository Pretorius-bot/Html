from DNAToolkit import *
import random

#creating random Dna seq for testing:
randDNAStr = ''.join([random.choice(Nucleotides)
                      for nuc in range(50)])

print(validateSeq(randDNAStr))
print(countNucFrequency(randDNAStr))