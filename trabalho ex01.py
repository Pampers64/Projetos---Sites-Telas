valores = []


for i in range(5):
  valor = input(f"Digite o {i + 1}º valor: ")
  valores.append(valor)


print("\nValores digitados:")
for valor in valores:
  print(valor)
