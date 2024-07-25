def linha():
    print('--' * 20)
    print('\n')

""" 1) Utilizar o método input() para fazer as seguintes tarefas:
Pedir um número por teclado, mostrar o resultado e o tipo (para saber em que tipo de dado captura a informação input())
Pedir um número por teclado e assegurar que capturamos a informação em formato int
Pedir um número por teclado e assegurar-se de que capturamos a informação en formato float """

numero1 = input("Informe um número: ")
print(f"O número informado: {numero1}, é do tipo:", type(numero1))
numero2 = int(input("Informe um número inteiro: "))
numero3 = float(input("Informe um número real: "))


linha()
# 2) Formatar os seguintes valores para mostrar o resultado indicado:

# Olá Mundo” → Alinhado à direita em 20 caracteres
print("{:>20}".format("Olá Mundo"))

# Olá Mundo” → Truncagem no quarto carácter (índice 3)
print("{:.4}".format("Olá Mundo"))

# “Olá Mundo” → Alinhamento ao centro em 20 caracteres com truncagem no segundo carácte (índice 1)
print("{:^20.1}".format("Olá Mundo"))

# 150 → Formatar a 5 números inteiros preenchidos com zeros
print("{:05d}".format(150))

# 7887 → Formatar a 7 números inteiros preenchidos com espaços
print("{:>7}".format(7887))

#20.02 → Formatar a 3 números inteiros e 3 números decimais
print("{:07.3f}".format(20.02))

