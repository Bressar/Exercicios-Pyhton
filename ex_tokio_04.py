def linha():
    print('\n')
    print('---' * 40)
    print('\n')
    
""" 
1) Fazer um programa que leia três números por teclado e permitir avaliar o seguinte:
Se os números estão por ordem ascendente
Se os números não estão por ordem ascendente
Se há um erro devido a que o primeiro número introduzido é 0 
"""
lista = []
lista2 = []
for n in range(1, 4):
    numero = float(input(f"Informe o {n}° número: "))
    #lista.append(numero)
    lista += [numero]
    if lista[0] == 0:
        print("ERRO! ->> o primeiro número precisa ser diferente de 0 <<-\n-> Saindo do Programa...")
        break
if lista[0] != 0:
    lista2 = sorted(lista) # sorted() deixa a lista em oredem ascendente
    if lista[0] == lista[1] or lista[1] == lista[2] or lista[0] == lista[2]:
        print("ERRO! ->> Dois números iguais! <<-\n-> Saindo do Programa...")
    elif lista == lista2:
        print("Os números estão em ordem ascendente.")
    else:
        print("Os números não estão em ordem ascendente.")
  
        
linha()  
"""
2) Fazer um programa que realize o somatório dos primeiros N números, começando em 0, e sendo N o número limite que o utilizador proporciona por teclado:
Exemplo de número limite introduzido pelo utilizador: 5
somatório = 0 + 1 + 2 + 3 + 4 (somamos os 5 primeiros números) """
contador = -1
soma = 0
numero = int(input("Digite um número: ")) # recebe o valor limite fornecido pelo usuário
for i in range(numero):# faz o ciclo de 0 até o número limite
    contador += 1 # mostra os numeros a serem somados em sequência
    soma += i # soma 1 número a cada ciclo
    print(contador, end= " + ") # apresenta os números de cada ciclo em sequência
print(f"\nA soma dos números é de: {soma}") # apresenta o resultado da soma dos números de todo o ciclo


linha()
"""
3) Fazer um programa que leia dois números por teclado e mostre o seguinte menu:
Mostrar uma soma dos dois números
Mostrar um resto dos dois números (o primeiro menos o segundo)
Mostrar uma multiplicação dos dois números
Em caso de não introduzir uma opção válida, o programa irá informar que não é correta 
"""
opcao = 1
print("Insira dois números:")
num1 = float(input(f"1° número: "))
num2 = float(input(f"2° número: "))
print("Escolha a opção:")
while opcao > 0 and opcao < 4:
    for c in range(1, 5):
        opcao = int(input("=============================================\n"
                 "[1] Somar\n"
                 "[2] Subtrair\n"
                 "[3] Multiplicar\n"
                 "[4 ou +] Sair\n"))
        if opcao == 1:
            print("O resultado da soma é: ", num1 + num2)
        elif opcao == 2:
            print("O resultado da subtração é: ", num1 - num2)
        elif opcao == 3:
            print("O resultado da multiplicação é: ", num1 * num2)
        else:
            print("Saindo...")
            break
    print("-*-"*10)
    
    
linha()
"""
4) Fazer um programa que leia letras e conte com uma variável contadora as letras “a” que se introduzem. Para sair do programa, introduzir o carácter “.”. Ao finalizar mostrar o número de vezes que se pressionou a letra “a” 
"""
cont_letra = 0
cont_letra_total = 0
while (True):
    frase = str(input("Introduza uma palavra para saber o número\n"
                      "de vezes em que a letra 'A' aparece: " )).strip().upper()
    for letra in frase:
        if letra == "A":
            cont_letra += 1
    print(f"A palavra '{frase}' tem {cont_letra} vezes a letra 'A'.")
    print("---" * 20)

    cont_letra_total += cont_letra
    cont_letra = 0

    sair = str(input("Para sair, digite ponto [.]\n"
                     "Para continuar pressione ENTER. "))
    if sair == ".":
        print("-*-" * 20)
        print(f"Saindo do Programa...\n"
              f"No total a letra 'A' foi escrita {cont_letra_total} vezes.")
        break
    print("===" * 20)
    
    
linha()
"""
5) Fazer um programa que leia por teclado um número ímpar. Deve repetir-se o processo enquanto o utilizador continue a introduzir números ímpares. Quando introduzir um número par, o programa irá parar.
"""
while (True):
    num = int(input("Introduza um número Ímpar: "))
    if num < 0:
        print("Número inválido! Introduza um número maior que 0." )
    else:
        if num % 2 == 1:
            print("-----" * 5)
        else:
            print(f"-------------------------\n"
                  f"Saindo do Programa...\n"
                  f"{num} é um número Par!")
            break


linha()
"""
6) Fazer um programa que some todos os números pares desde 0 até 100:
Sugestão: pode utilizar as funções sum() e range() para o tornar mais fácil. O terceiro parâmetro na função range (início, fim, salto) indica um salto de números, experimente-o
""" 
soma = 0
for n in range(0, 101, 2):# versão 1 forma mais simples
    soma += n
print(soma)

soma = 0
for n in range (0, 101):# versão 2
    if n % 2 == 0:
        soma += n
print(soma)


linha()
"""
7) Fazer um programa que solicite ao utilizador um número que representa o total de números que se vão introduzir. Posteriormente, ler todos esses números e fazer a média aritmética de todos eles:
"""
quant_num = int(input("Informe de quantos números quer saber a média: "))
soma = 0
lista = []
for i in range (1, quant_num + 1):
    num = float(input(f"Insira o {i}° número: "))
    soma += num
    lista += [num]
media = soma / quant_num
print(f"A média entre os números: {lista}\né de: {media:.2f}")


linha()
"""
8) Fazer um programa que solicite ao utilizador um número inteiro de 0 a 9, e que enquanto o número não seja correto se repita o processo. Logo deve comprovar se o número se encontra na lista de números e notificá-lo:
Conselho: a sintaxis “valor in lista” permite comprovar facilmente se um valor se encontra numa lista (devolver True ou False)
 """
numeros = [1, 3, 6, 9]
while (True):
    num = int(input("Introduza um número entre 0 e 9: "))
    if num < 0 or num > 10:
        print("Valor inválido!, escreva novamente.\n"
              "------------------------------------")
    elif num in numeros:
        print(f"O número {num} está na lista:\n"
              f"{numeros}\n"
              f"------------------------------------")
        break
    else:
        num >= numeros[0] and num <= numeros[-1]
        print(f"O número {num} não está na lista.\n"
              f"------------------------------------")
        

linha()
"""
9) Fazer um programa que utilize a função range() e a conversão para listas gera as seguintes listas dinamicamente (e mostrá-las com print): 
9) Fazer um programa que utilize a função range() e a conversão para listas gera as seguintes listas dinamicamente (e mostrá-las com print):
Todos os números de 0 a 10 [0, 1, 2, ..., 10]
Todos os números de -10 a 0 [-10, -9, -8, ..., 0]
Todos os números pares de 0 a 20 [0, 2, 4, ..., 20]
Todos os números ímpares entre -20 e 0 [-19, -17, -15, ..., -1]
Todos os números múltiplos de 5 a 50 [0, 5, 10, ..., 50]
Pista: utilizar o terceiro parâmetro da função range (início, fim, salto).
"""
l1 = []
l2 = []
l3 = []
l4 = []
l5 = []

for n in range (0, 11):
    l1 += [n]

for n in range (-10, 1):
    l2.append(n)

for n in range (0, 21, 2):
    l3 += [n]

for n in range (-20, 1):
    if n % 2 == 1:
        l4 += [n]

for n in range (5, 51, 5):
    l5 += [n]

print(f"{l1}\n"
      f"{l2}\n"
      f"{l3}\n"
      f"{l4}\n"
      f"{l5}\n")


linha()
"""
10) Fazer um programa que dadas duas listas, gera uma terceira lista com todos os elementos que se repitam nelas, mas não deve repetir-se nenhum elemento na nova lista:
"""
lista_1 = ["o",'l','a',' ', 'm','u','n','d','o']
lista_2 = ["o",'l','a',' ', 'l','u','a'] 
lista_3 = []

lista_4 = [1, 2, 3, 4, 5, 7, 9, 11, 13]
lista_5 = [0, 2, 3, 4, 6, 7, 8, 9, 10, 12]
lista_6 = []

for item in lista_1:
        lista_3 += [item]

for item in lista_2:
    if item not in lista_3:
        lista_3 += [item]

print(f"A junção das listas:\n{lista_1} e \n"
      f"{lista_2},\n"
      f"sem repetições de itens resulta em:\n",sorted(lista_3))

print('\n')

print(f"A junção das listas:\n{lista_4} e \n"
      f"{lista_5},\n"
      f"sem repetições de itens resulta em:\n",sorted(lista_6))
