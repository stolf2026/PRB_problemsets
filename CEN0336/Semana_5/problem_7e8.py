# Arquivo para converter sequências de DNA em RNA

print("Conversor de DNA em RNA")
print("Copie aqui a sua sequência de DNA:")
sequencia_dna = input().strip().upper()
sequencia_rna = sequencia_dna.replace("T","U")
if "U" in sequencia_dna:
    print("A sequencia fornecida contém uracila (RNA)")
else:
    sequencia_rna = sequencia_dna.replace("T", "U")
    print(f"A sequência convertida é {sequencia_rna}.")
