tupla1 = ('José', 'Maria', 'Orlando', 'Jonas')
tupla2 = (2.25, 4.5, 8.25, 9.75)

if len(tupla1) != len(tupla2):
  raise ValueError("As tuplas devem ter o mesmo tamanho.")

dados_ordenados = sorted(zip(tupla1, tupla2), key=lambda item: item[1])

impressao_formatada = ""
for nome, nota in dados_ordenados:
  impressao_formatada += f"{nome}: {nota:.2f}\n"


saida_formatada = impressao_formatada

print(saida_formatada) 
