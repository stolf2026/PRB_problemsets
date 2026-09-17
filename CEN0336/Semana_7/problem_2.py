#Script para divisão de string em lista
taxa = "sapiens, erectus, neanderthalensis"
print(taxa)

#mostrar caracter no índice solicitado
print(taxa[1])

#mostrar tipo de dado
print(type(taxa))

#Criar a lista a partir da string
species = taxa.split(", ")

print(species)
print(type(species))

#Ordenar
ordered_species = sorted(species)
print(ordered_species)

#Ordenar por comprimento de cada string
string_species = sorted(species, key = len)
print(string_species)

