def calcular_soma_tupla(tupla_numeros):

  if not isinstance(tupla_numeros, tuple):
    raise TypeError("Argumento 'tupla_numeros' deve ser uma tupla.")

  if not all(isinstance(numero, int) for numero in tupla_numeros):
    raise TypeError("Todos os elementos da tupla devem ser números inteiros.")

  soma = 0
  for numero in tupla_numeros:
    soma += numero
  return soma

def main():
  try:
    tupla_str = input("Digite uma tupla de números inteiros (separados por vírgula): ")
    tupla_numeros = tuple(int(numero) for numero in tupla_str.split(",")) 
    soma = calcular_soma_tupla(tupla_numeros)
    print(f"A soma dos números na tupla é: {soma}")
  except TypeError as e:
    print(f"Erro: {e}")
  except ValueError:
    print("Erro: Valores inválidos na tupla.")

if __name__ == "__main__":
  main()
