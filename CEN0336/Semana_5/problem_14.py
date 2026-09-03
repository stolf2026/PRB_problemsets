#Script para identificação em sequência de DNA do sítio de restrição EcoRI

# Script para encontrar o sítio EcoRI (GAATTC) em sequência de DNA
print("Buscador do sítio EcoRI (GAATTC)")

# Entrada da sequência
sequencia = input("Cole aqui sua sequência de DNA 5'-3': ").strip().upper()

# Sítio de restrição
sítio = "GAATTC"

# Encontra a posição inicial (índice em Python)
indice = sequencia.find(sítio)

if indice != -1:
    # Posição inicial em biologia (começa em 1)
    start_pos = indice + 1
    # Posição final (inclusive) = start + comprimento - 1
    end_pos = start_pos + len(sítio) - 1
    
    print(f"EcoRI startPos:{start_pos} endPos:{end_pos}")
else:
    print("Sítio EcoRI não encontrado na sequência.")
