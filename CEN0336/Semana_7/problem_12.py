seqs = ['ATGCCCGGCCCGGC', 'GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT']

# Compreensão de lista gerando tuplas (comprimento, sequência)
seq_lengths = [(len(seq), seq) for seq in seqs]

# Imprimir no formato "comprimento\tsequência\n"
for length, seq in seq_lengths:
    print(f"{length}\t{seq}")
