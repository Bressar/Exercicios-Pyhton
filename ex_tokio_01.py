def linha():
    print('--' * 20)
    print('\n')
    
""" 1) Armazenar 3 variáveis com 3 notas numéricas e fazer a média aritmética. Mostrar o resultado final com uma mensagem como esta: “A nota média é 6,0” """

n1, n2, n3 = 3, 5, 10
media = (n1 + n2 + n3) / 3
print(f'"A nota média é {media}"')


linha()
""" 2) Continuar o exercício anterior. Cada nota tem o valor percentual seguinte:
1ª nota: vale 15% do total
2ª nota: vale 35% do total
3ª nota: vale 50% do total
Calcular a nota média final. """

nota_1 = 10
nota_2 = 7
nota_3 = 4
media_notas = (nota_1 * 0.15) + (nota_2 * 0.35) + (nota_3 * 0.5)
print(f"Média Final: {media_notas:.2f}")


linha()
""" 3) Ler 2 números inteiros por teclado e avaliar de forma booleana (True ou False) os seguintes aspetos:
Se os dois números são iguais
Se os dois números são diferentes
Se o primeiro é maior que o segundo
Se o segundo é maior ou igual ao primeiro """

num1 = int(input("Informe o 1° número: "))
num2 = int(input("Informe o 2° número "))

if (num1 == num2):
    print(f"Os números: {num1} e {num2} são iguais.")

if (num1 != num2):
    print(f"Os números: {num1} e {num2} são diferentes.")

if (num1 > num2):
    print(f"O 1° número: {num1} é maior do que o 2°: {num2} ")

if (num2 >= num1):
    print(f"O 2° número: {num2} é maior ou igual do que o 1° número: {num1}")

  
linha()  
""" 4) Ler uma cadeia de texto introduzida pelo teclado e avaliar se tem um comprimento maior ou igual a três e menor que dez (mostrar unicamente True ou False) Pista: utilizar operadores lógicos """

frase = str(input("Escreva uma frase para saber se o seu\n"
                  "número de caracteres é maior ou igual a 3\n"
                  "ou menor do que 10: "))

if ((len(frase) >= 3) and (len(frase) < 10)):
    print(True)
else:
    print(False)
    

linha() 
""" 5) Transcrever o seguinte algoritmo (utilizar operadores de atribuição sempre que possa):
Guardar numa variável o número_mágico o valor 12345679 (sem o 8)
Ler por ecrã outro número_utilizador, especificar que seja entre 1 e 9 (assegurar que seja inteiro)
Multiplicar o número_utilizador por 9 por si mesmo
Multiplicar o número_mágico pelo número_utilizador por si mesmo
Finalmente mostrar o valor final do número_mágico por ecrã """

num_magic = int(12345679)
num_utl = int(input("Digite um número entre 1 e 9: "))
num_utl *= 9
print(num_utl * num_magic)

