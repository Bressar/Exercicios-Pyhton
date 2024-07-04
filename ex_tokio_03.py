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



