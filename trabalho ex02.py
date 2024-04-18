def ler_numeros_reais():
  numeros = []
  for i in range(10):
    try:
      numero = float(input(f"Digite o {i + 1}º número real: "))
    except ValueError:
      print("Valor inválido. Digite um número real.")
      continue
    numeros.append(numero)
  return numeros


def imprimir_inverso(numeros):
  for i in range(len(numeros) - 1, -1, -1):
    print(numeros[i])


numeros = ler_numeros_reais()

print("\nNúmeros na ordem inversa:")
imprimir_inverso(numeros)
