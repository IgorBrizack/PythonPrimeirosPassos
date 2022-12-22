import math
"OPERAÇÕES ARITMÉTICAS"

print('5 + 2 = ', 5+2)
print('5 - 2 = ', 5-2)
print('5 * 2 = ', 5*2)
print('5 / 2 = ', 5/2)
print('5 ^ 2 = ', 5**2)
print('5 // 2 (inteiro) = ', 5//2)
print('5 / 2 (resto da divisão) = ', 5%2)

# "mostre na tela um programa que leia um número inteiro e mostre sucessor e seu antecessor"
N1 = int(input("Digite um número "))
RAIZ_QUADRADA = math.sqrt(N1)
print("O antecessor de {} é {} e o sucessor é {}".format(N1, N1 - 1, N1 + 1))
print("O dobro de {} é {},  é {} e a raiz quadrada é {}".
      format(N1, N1 * 2, N1 * 3, RAIZ_QUADRADA))
