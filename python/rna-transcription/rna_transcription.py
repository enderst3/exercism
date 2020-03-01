'''
Given a DNA strand, return its RNA complement (per RNA transcription).

Both DNA and RNA strands are a sequence of nucleotides.

The four nucleotides found in DNA are adenine (A), cytosine (C), guanine (G) and thymine (T).

The four nucleotides found in RNA are adenine (A), cytosine (C), guanine (G) and uracil (U).

Given a DNA strand, its transcribed RNA strand is formed by replacing each nucleotide with its complement:

G -> C
C -> G
T -> A
A -> U

Could be done using maketrans(), and translate

conversion = str.maketrans("GCTA", "CGAU")
return dna_strand.translate(conversion)
'''
# create dictionary
rna = {"G":"C",
       "C":"G",
       "T":"A",
       "A":"U"}

def to_rna(dna_strand):
    # create empty string to populate with translation
    translation = ''
    # for loop to iterate through string
    for i in dna_strand:
        # add the translated letter to the string
        translation += rna[i]
    # return translation string
    return translation
    
    
