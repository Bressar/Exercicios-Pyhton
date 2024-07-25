def linha():
    print('\n')
    print('---' * 40)
    print('\n')
    
    """ Exercícios de tipos avançados
1) Trabalhar com listas e tuplas

Criar uma lista e uma tupla que contenha strings (pelo menos 3 elementos). Será de temática livre, sobre o que quiser: veículos, comida, música, etc.
Imprimir a lista e a tupla.
Imprimir o 2.º elemento da lista e o penúltimo da tupla.
Modificar (se puder) algum elemento da lista e da tupla. E imprimir o resultado novamente.
Mostrar o tamanho da lista e da tupla.
Procurar um elemento dentro da lista e da tupla. Mostrar se nos devolve True ou False.
Adicionar (se puder) algum elemento à lista e à tupla. Mostrar a lista e a tupla novamente para verificar se a ação foi realizada corretamente.
Apagar ou eliminar (se puder) o conteúdo da lista e da tupla. Imprimir a lista e a tupla novamente para verificar se a ação foi realizada corretamente. """

# Criação
musics = ['Há tempos', 'Fábrica', 'Quase sem querer', 'Índios']
artists = ('Fellini', 'Picasso', 'Rodin', 'Bach', 'Shakira')

# Mostrar
print("Lista de músicas:\n",musics)
print("\nTupla de artistas:\n",artists)

# Mostrar elementos específicos
print("\n2° elemento da lista:\n",musics[1:2])
print("\nPenúltimo elemento da Tupla:\n",artists[-2])

# Modificar
musics [0] = "Enjoy the Silence"
print("\nLista de músicas com um novo primeiro elemento:\n",musics)

# Tamanho
print("\nNúmero de elementos na lista:",len(musics))
print("\nNúmero de elementos na Tupla:",len(artists))

# Pesquisa de elementos
print("\nA música 'Help' está na lista?")
if ("Help" in musics):
    print(True)
else:
    print(False)

print("\nO/a artista", artists[4], "está na lista?")
if (artists[0] in artists):
    print(True)
else:
    print(False)
    
# Adicionar elementos
musics.append('Levanta e Anda')# pode ser usada a função insert() para acrescentar mais elementos(no início da lista)
print("\nLista de músicas com mais um elemento:\n",musics)

# só dá para acrescentar pelo menos 2 elementos, senão será lido como apenas uma string e não uma tupla
artists2 = ('Monica Bellucci', 'Scarlet Johansson')
artists += artists2
print("\nTupla de artistas com mais elementos:\n",artists)

# Apagado
musics.clear()
print(musics)# Com a função clear() já não fica nenhuma informação da variável na memória...

print("\n",artists)
# Como a tupla é uma CONSTANTE, a função clear ou delete não funcionam com ela...
# se ouver um outro jeito de apagar, além de apagar manualmente a variável eu gosaria de saber.. tks


linha()
""" 
2) Trabalhar com sets e dicionários
Criar um set e um dicionário que contenham strings (pelo menos 3 elementos no caso do set e 3 conjuntos de chave: valor no caso do dicionário). Temática livre, sobre o que quiser, veículos, comida, música, etc.
Mostrar o set e o dicionário
Mostrar (se puder) o 2º elemento do set e o valor da primeira chave-valor do dicionário
Modificar (se puder) algum elemento do set ou do dicionário. E mostrar o resultado
Mostrar o tamanho do set e do dicionário
Fazer uma pesquisa de um elemento dentro do set e dentro do dicionário. Imprimir o resultado (True ou False).
Adicionar (se puder) algum elemento ao set e alguma chave-valor ao dicionário. Imprimir novamente o set e o dicionário para verificar se a acção foi realizada corretamente.
Apagar ou eliminar (se puder) o conteúdo do set e do dicionário. Imprimir de novo o set e o dicionário para verificar se a acção foi realizada corretamente. """

# Criação
animais = {'aves', 'peixes', 'reptéis', 'anfíbios'} # set

mamiferos = {
    'classe' : 'felino',
    'tipo' : 'gato',
    'raça' : 'persa',
    'nome' : 'pepi'
}
# Mostrar
print("\nLista de animais:", animais)
print("\nDicionário de mamíferos:", mamiferos)

# Mostrar elementos específicos
# Só é possível usar o index após converter o set p/ uma lista
# Já que o set é um conjunto desordenado, assim como os dicionários
animais_list = list(animais)# escolhe os itens para a lista de forma aleatória
print(animais_list)
print("\n2° elemento do Set 'animais':",animais_list[1])

mamiferos_keys = list(mamiferos)# tb poderia ser a função keys()
mamiferos_values = mamiferos.values()
mamiferos_keys = list(mamiferos_keys)
mamiferos_values = list(mamiferos_values)
print("\nPrimeira chave/valor do diconário:", mamiferos_keys[0], ":", mamiferos_values[0])

 # Modificar
animais.remove("peixes")
animais.add("roedores")
print("\nNo Set foi removido o item 'peixes' e acrescentado o item 'roedores':", animais)

mamiferos["nome"] = "blau-blau"
print("\nNo dicionário foi mudada o nome:", mamiferos)

# Tamanho
print("\nO Set animais tem:", len(animais), "elementos")
print("\nO dicionário mamiferos tem:", len(mamiferos), "elementos")

# Pesquisa de elementos
print("\nO item 'aves' está no Set de animais?")
if('aves' in animais):
    print(True)
else:
    print(False)

print("\nO animal cobra está no Dicionário de mamíferos? ")
if('cobra'in mamiferos):
    print(True)
else:
    print(False)
    
# Adicionar elementos
animais.add("mamíferos")
print("\nAdicionado 1 novo item no Set",animais)
animais.update(["insetos", "crustáceos"])
print("\nAdicionados 2 novos itens no Set",animais)

print("\nAcrescentados uma nova chave e valor")
mamiferos["cor"] = "laranja"
for x in mamiferos:
    print(x, ":", mamiferos[x])

# Apagado
mamiferos.pop("cor")
print("\nEliminado o item 'cor'", mamiferos)

print("\nSet e Dicionário apagados")
animais.clear()
mamiferos.clear()
print(animais)
print(mamiferos)


linha()
""" 3) Fazer um programa que peça ao utilizador 3 números que possam int ou float (não é necessário fazer ciclos , pode repetir o código). Estes números devem ser adicionados a uma lista. Quando se finalizar a introdução dos dados, realizar a soma dos elementos da lista e atribuir a uma variavel com nome "somatório" . No final, imprimir o resultado. ” """

n1 = float(input("Informe o 1° número: "))
n2 = float(input("Informe o 2° número: "))
n3 = float(input("Informe o 3° número: "))
lista = [n1, n2, n3]
somatorio = sum(lista)
print(f"O resultado de {n1} + {n2} + {n3} é:",somatorio)


linha()
""" 4) Continuar o exercício anterior; calcular a média aritmética dos elementos da lista e imprimir o resultado.
Neste caso sabemos que o número de elementos que o utilizador introduziu é 3, mas o objetivo será deixar o programa abstrato,e portanto, não fazer referência ao número 3; deve calcular o numeros de elementos da lista """

media = sum(lista) / len(lista)
print(media)
print(f"A média entre {n1}, {n2}, {n3} é de: {media:.2f}")


linha()
""" 5) Dada a seguinte matriz (lista com quatro listas como elementos), o objectivo é que em cada sublista, o quarto elemento seja sempre o resultado da soma dos três primeiros elementos. Construa um pequeno programa que realize este cálculo.
Pista: modificar as somas erradas utilizando o slicing
Não vale colocar diretamente os valores (nem os índices nem a soma):
matriz[1][3] = 6
matriz[3][3] = 12
Há que pesquisar uma forma automatizada de aceder e modificar esses valores
 """
 
matriz = [ 
    [1, 1, 1, 3],
    [2, 2, 2, 7],
    [3, 3, 3, 9],
    [4, 4, 4, 13]
]
soma = 0
for c in range(4): # Este loop itera sobre os índices das linhas da matriz (0 a 3).
    for numero in matriz[c][:3]: # Este loop itera sobre os primeiros três elementos de cada linha da matriz 
        soma += numero # adiciona o numero atual ao valor acumulado em soma
        matriz_nova = matriz[c][:3] # cria uma nova lista (matriz_nova) com os primeiros três elementos da linha atual da matriz.
        matriz_nova.append(soma) # adiciona o valor atual de soma ao final dessa nova lista.
    print(matriz_nova) # imprime a nova lista (matriz_nova) com os primeiros três elementos da linha original e o valor acumulado de soma.
    soma= 0 # reinicializa soma para 0 antes de passar para a próxima linha.

""" Primeira Iteração (c = 0):

Elementos: [1, 1, 1]
Soma: 1 + 1 + 1 = 3
Nova Linha: [1, 1, 1, 3]
Impressão: [1, 1, 1, 3]
Segunda Iteração (c = 1):

Elementos: [2, 2, 2]
Soma: 2 + 2 + 2 = 6
Nova Linha: [2, 2, 2, 6]
Impressão: [2, 2, 2, 6]
Terceira Iteração (c = 2):

Elementos: [3, 3, 3]
Soma: 3 + 3 + 3 = 9
Nova Linha: [3, 3, 3, 9]
Impressão: [3, 3, 3, 9]
Quarta Iteração (c = 3):

Elementos: [4, 4, 4]
Soma: 4 + 4 + 4 = 12
Nova Linha: [4, 4, 4, 12]
Impressão: [4, 4, 4, 12] """


linha()
""" 6) Supor que obtém uma string invertida. Esta string contém o nome e a nota de um aluno. Formate este string para obter o seguinte output:
Nome Apelido teve um(a) Nota de nota
Pista: Para inverter uma string usando a técnica de slicing pode-se utilizar um terceiro índice -1: cadeia[::-1] """

cadeia_A = "seroloD airaM,30"
cadeia_B = "zereP solraC,01"

cadeia1 = cadeia_A[::-1] # inverte a cadeia
cadeia2 = cadeia_B[::-1] # inverte a cadeia

print(cadeia1[3:], "teve uma nota:", cadeia1[:2])
print(cadeia2[3:], "teve uma nota:", cadeia2[:2])


linha()
""" 7) Fazer um programa que cumpra as seguintes instruções:
Criar um conjunto chamado utilizadores com os utilizadores Marta, David, Elvira, Juan e Marcos
Criar um conjunto chamado administradores com os administradores Juan e Marta.
Apagar o administrador Juan do conjunto de administradores.
Adicionar Marcos como um novo administrador, mas não o apagar do conjunto de utilizadores.
Imprimir todos os utilizadores por ecrã de forma dinâmica (loop); indicar também se os utilizadores são administradores (ou não).
Notas: os conjuntos podem ser percorridos dinâmicamente, utilizando o ciclo for de forma similar a uma lista. Também contam com um método chamado .discard (elemento) que serve para apagar um elemento. """

utilizadores = {"Marta", "David", "Elvira", "Juan", "Marcos"}
administradores = {"Juan", "Marta"}
administradores.remove("Juan")
administradores.add("Marcos")

for nome in utilizadores:
    if nome in administradores:
        print(nome, "é um(a) administrador(a)")
    else:
        print(nome, "é um(a) utilizador(a)")
        
        
linha()
""" 8) Existe um videojogo na qual os atributos das personagens estão guardadas nos seguintes dicionários:

cavaleiro = { 'vida':2, 'ataque':2, 'defesa': 2, 'alcance':2 }
guerreiro = { 'vida':2, 'ataque':2, 'defesa': 2, 'alcance':2 }
arqueiro = { 'vida':2, 'ataque':2, 'defesa': 2, 'alcance':2 }
Ao passar para o segundo nível do jogo, temos de automaticamente alterar os seus valores:

O cavaleiro terá o dobro de vida e de defesa que um guerreiro.
O guerreiro terá o dobro do ataque e do alcance que um cavaleiro.
O arqueiro terá a mesma vida e ataque que um guerreiro, mas a metade da sua defesa e o dobro do seu alcance.
Imprimir como fica os atributos das três personagens.      """ 

cavaleiro = {"vida" : 2,
             "ataque" : 2,
             "defesa" : 2,
             "alcance" : 2
             }

guerreiro = {"vida" : 2,
             "ataque" : 2,
             "defesa" : 2,
             "alcance" : 2
             }

arqueiro = {"vida" : 2,
            "ataque" : 2,
            "defesa" : 2,
            "alcance" : 2
            }

print("{:^60}".format(">>> FIRST LEVEL <<<"))
print(f"Cavaleiro: {cavaleiro}\n"
      f"Guerreiro: {guerreiro}\n"
      f"Arqueiro: {arqueiro}\n")

second_level = True

if second_level == True:
    cavaleiro["vida"] = guerreiro["vida"] * 2
    cavaleiro["defesa"] = guerreiro["defesa"] * 2

    guerreiro["ataque"] = cavaleiro["ataque"] * 2
    guerreiro["alcance"] = cavaleiro["alcance"] * 2

    arqueiro["vida"] = guerreiro["vida"]
    arqueiro["ataque"] = guerreiro["ataque"]
    arqueiro["defesa"] = guerreiro["defesa"] / 2
    arqueiro["alcance"] = guerreiro["alcance"] * 2

print("{:^60}".format(">>> SECOND LEVEL <<<"))
print(f"Cavaleiro: {cavaleiro}\n"
      f"Guerreiro: {guerreiro}\n"
      f"Arqueiro: {arqueiro}")

linha()
