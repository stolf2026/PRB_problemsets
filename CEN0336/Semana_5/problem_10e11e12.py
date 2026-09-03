#Script de análise de substrings de DNA
print("Analisador dos nucleotídeos 100-200")
sequencia = input("Insira aqui sua sequência de nucleotídeos:").strip().upper()

string = sequencia[99:200]

teor_a = string.count("A")
teor_c = string.count("C")
teor_t = string.count("T")
teor_g = string.count("G")
total = teor_a +  teor_c + teor_t + teor_g
teor_a_t = (teor_a + teor_t)/total*100
teor_g_c = (teor_g + teor_c)/total*100


print(f"Há {teor_g} guaninas na substring de DNA (nucleotídeo 100-200)")
print(f"O teor AT na sequência é de {teor_a_t}%")
print(f"O teor GC na sequência é de {teor_g_c}%")
