# Script de microrganismos presentes no intestino humano

taxonomy = dict([
    ('Proteobacteria', 4139),
    ('Sphingobacteria', 4127),
    ('Planctobacteria', 4098),
    ('Bacillati', 5097)
])

# Para listar todos os táxons presentes
print('A descobrir os táxons presentes e sua contagem no dicionário fornecido')

for taxa, count in taxonomy.items():
    print(taxa, count)

# Para buscar táxons especificados pelo usuário
print("Buscador de táxons na amostra")

busca = input("Insira aqui o nome do táxon que busca, com a primeira letra maiúscula: ")

if busca in taxonomy:
    print('Táxon encontrado nos dados')
else:
    print('Táxon não encontrado nos dados')

# Para calcular o número total de reads
print('Calculando total de leituras (reads) presentes no dicionário')

reads = 0

for taxa, count in taxonomy.items():
    reads = reads + count

print('O número total de reads nestes dados é:', reads)
