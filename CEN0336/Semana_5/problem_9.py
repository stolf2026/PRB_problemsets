#Script de cálculo do teor A/T em sequências de nucleotídeos
print("Analisador de teor A/T")
sequencia = input("Insira aqui sua sequência de nucleotídeos").strip().upper()

teor_a = sequencia.count("A")
teor_c = sequencia.count("C")
teor_t = sequencia.count("T")
teor_g = sequencia.count("G")
total = teor_a +  teor_c + teor_t + teor_g
teor_a_t = (teor_a + teor_t)/total*100 
teor_g_c = (teor_g + teor_c)/total*100

print(f"O teor AT na sequência é de {teor_a_t}%")
print(f"O teor GC na sequência é de {teor_g_c}%")

