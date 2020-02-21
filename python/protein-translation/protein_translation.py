rna = {
        'AUG': "Methionine",
        'UUU': "Phenylalanine",
        'UUC': "Phenylalanine",
        'UUA': "Leucine",
        'UUG': "Leucine",
        'UCU': "Serine",
        'UCC': 'Serine',
        'UCA': 'Serine',
        'UCG': 'Serine',
        'UAU': 'Tyrosine',
        'UAC': 'Tyrosine',
        'UGU': "Cysteine",
        'UGC': "Cysteine",
        'UGG': 'Tryptophan',
        "UAA": "STOP",
        "UAG": "STOP",
        "UGA": "STOP", 
        }

def proteins(strand):
    # create a list of codons using loop and range(start, stop, step)
    codons = [strand[i:i+3] for i in range(0, len(strand), 3)]
    # for loop to iterate through codons and to create a list
    translation = []
    for codon in codons:
        # translate using the the dict
        protein = rna[codon]
        # stoping on certain proteins
        if protein == "STOP":
            break
        # append list
        translation.append(protein)

    return translation