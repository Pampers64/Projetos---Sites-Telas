def ler_notas():
 
  notas = []
  for i in range(4):
    try:
      nota = float(input(f"Digite a {i + 1}ª nota: "))
    except ValueError:
      print("Valor inválido. Digite uma nota numérica.")
      continue
    notas.append(nota)
  return notas

def calcular_media(notas):
 
  if len(notas) == 0:
    return 0
  else:
    soma = 0
    for nota in notas:
      soma += nota
    return soma / len(notas)

def main():
 
  notas = ler_notas()
  media = calcular_media(notas)

  print("\nNotas:")
  for nota in notas:
    print(f"- {nota}")

  print(f"\nMédia: {media:.2f}")

if __name__ == "__main__":
  main()
