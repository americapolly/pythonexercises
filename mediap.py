'''Escreva um programa que leia duas notas de um aluno de programação. Em Seguida,
a média ponderada, com pesos 2 e 3, respectivamente, deve ser calculada. Por fim,
o programa deve imprimir a nota obtida'''

num1 = float(input("Digite a primeira nota: "))
num2 = float(input("Digite a segunda nota: "))

mediap=(num1*2+num2*3)/5

print("Média ponderada das notas: {:.1f}".format(mediap))
