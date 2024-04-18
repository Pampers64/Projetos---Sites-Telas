def cadastrar_usuario():

  nome = input("Digite seu nome: ")
  email = input("Digite seu email: ")
  telefones = []

  while True:
    telefone = input("Digite um telefone (ou pressione Enter para finalizar): ")
    if telefone == "":
      break
    telefones.append(telefone)

  usuario = {
    "nome": nome,
    "email": email,
    "telefones": telefones
  }

  return usuario

def main():
 
  agenda = {}

  for i in range(4):
    usuario = cadastrar_usuario()
    nome = usuario["nome"]
    agenda[nome] = usuario

  print("\nAgenda:")
  for nome, dados in agenda.items():
    print(f"\nNome: {nome}")
    print(f"Email: {dados['email']}")
    print(f"Telefones:")
    for telefone in dados["telefones"]:
      print(f"- {telefone}")

if __name__ == "__main__":
  main()


