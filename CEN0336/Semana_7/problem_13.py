#Script: imprimir posição, comprimento e sequência
seqs = ['ATGCCCGGCCCGGC', 'GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT']

for pos, seq in enumerate(seqs, start=1):
    print(f"{pos}\t{len(seq)}\t{seq}")
