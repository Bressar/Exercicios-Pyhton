def linha():
    print('\n')
    print('---' * 40)
    print('\n')
    
    """ 1) Fazer um programa que leia três números por teclado e permitir avaliar o seguinte:
Se os números estão por ordem ascendente
Se os números não estão por ordem ascendente
Se há um erro devido a que o primeiro número introduzido é 0 """

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
""" 2) Fazer um programa que realize o somatório dos primeiros N números, começando em 0, e sendo N o número limite que o utilizador proporciona por teclado:
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
""" 3) Fazer um programa que leia dois números por teclado e mostre o seguinte menu:
Mostrar uma soma dos dois números
Mostrar um resto dos dois números (o primeiro menos o segundo)
Mostrar uma multiplicação dos dois números
Em caso de não introduzir uma opção válida, o programa irá informar que não é correta """

