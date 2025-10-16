# Contador de Cliques em um Botão (Simulado)
# Simule um contador que pergunte quantas vezes o botão foi clicado 
# e mostre mensagens como “Clique 1 registrado”,
# “Clique 2 registrado” até o número informado.

cliques = []
cliques_informados = int(input("Digite quantos cliques foram : "))
cliques.append(cliques_informados)
for c in cliques:
    print(f"Clique {c} registrado.")

# Não consegui :(