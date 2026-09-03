#Script de obtenção de sequência complementar, reversa e reversa complementar de DNA.
print("Conversor de sequências de DNA - reverso/complemento/etc")

sequencia = input("Insira aqui sua sequência de nucleotídeos:").strip().upper()
complementar = sequencia.replace ("A","t")
complementar = complementar.replace ("T", "a")
complementar = complementar.replace ("C","g")
complementar = complementar.replace ("G", "c")
complementar = complementar.upper()
inverso_complementar = complementar[::-1]
RNA = sequencia.replace('T', 'U')

print(f"Sequência Original 5'{sequencia}3'")
print(f"Sequência Complemento 3'{complementar}5'")
print(f"Sequência Inverso Complemento 5'{inverso_complementar}3'")
print(f"Sequência RNA teórico transcrito 5'{RNA}3'")

