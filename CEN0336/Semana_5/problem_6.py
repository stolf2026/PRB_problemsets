# Arquivo para leitura do número de nucleotídeos e análise de composição

print("Analisador de composição de sequências de DNA")
print("Copie aqui a sua sequência de nucleotídeos:")
sequencia = input().strip().upper() 
print("Contagem iniciada")

tamanho = len(sequencia)
teor_a = sequencia.count("A")
teor_t = sequencia.count("T")
teor_c = sequencia.count("C")
teor_g = sequencia.count("G")

print(f"A sequência fornecida possui {tamanho} nucleotídeos")
print(f"A sequência de {tamanho} pb possui {teor_a} adeninas, {teor_t} timinas, {teor_c} citosinas, {teor_g} guaninas")
