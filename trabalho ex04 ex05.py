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

def listar_contatos(agenda):

  if not agenda:
    print("Agenda vazia!")
    return

  print("\nContatos:")
  for nome in agenda.keys():
    print(nome)

def listar_informacoes_contato(agenda, nome):
 
  if nome not in agenda:
    print(f"Contato '{nome}' não encontrado.")
    return

  dados_contato = agenda[nome]
  print("\nInformações do contato:")
  print(f"Nome: {dados_contato['nome']}")
  print(f"Email: {dados_contato['email']}")
  print(f"Telefones:")
  for telefone in dados_contato["telefones"]:
    print(f"- {telefone}")

def main():
 
  agenda = {}

  while True:
    print("\nMenu:")
    print("1. Cadastrar novo contato")
    print("2. Listar contatos")
    print("3. Exibir informações de um contato")
    print("4. Sair")

    opcao = input("Digite sua opção: ")

    if opcao == "1":
      novo_usuario = cadastrar_usuario()
      agenda[novo_usuario["nome"]] = novo_usuario
      print("Contato cadastrado com sucesso!")
    elif opcao == "2":
      listar_contatos(agenda)
    elif opcao == "3":
      nome_contato = input("Digite o nome do contato: ")
      listar_informacoes_contato(agenda, nome_contato)
    elif opcao == "4":
      break
    else:
      print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
  main()

