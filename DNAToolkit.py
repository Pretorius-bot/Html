
Nucleotides = ["G","T", "C", "A"]

#check the string to make sure it is a dna string
def validateSeq(dna_seq):
    tmpseq =  dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq

def countNucFrequency(seq):
    tmpFreqDict ={"A":0, "C":0, "T":0, "G":0 }
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict



