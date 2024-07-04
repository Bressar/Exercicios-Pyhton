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