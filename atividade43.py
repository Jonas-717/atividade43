# Contador de Cliques em um Botão (Simulado)
# Simule um contador que pergunte quantas vezes o botão foi clicado 
# e mostre mensagens como “Clique 1 registrado”,
# “Clique 2 registrado” até o número informado.

cliques = []
cliques_informados = int(input("Digite quantos cliques foram : "))
cliques.append(cliques_informados)
for c in cliques:
    c = c + 1 #Faz o número digitado aparecer no terminal (EX: se digitar 10 aparecerar "Clique 10 registrado", invés de "Clique 9 registrado")
    while c != 1:
        c = c - 1
        print(f"clique {c} registrado")
