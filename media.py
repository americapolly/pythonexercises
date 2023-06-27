'''Escreva um programa que leia 3 números inteiros, calcule e escreva a média
aritmética  entre eles'''

num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite mais um número inteiro: "))
num3 = int(input("Digite o último número inteiro: "))

media=(num1+num2+num3)/3

print("Média: {:.1f}".format(media))
