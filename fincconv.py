'''Construa um programa que leia uma temperatura em Fahrenheit e converta-a para
Celsius. Sabe-se que: C=(f-32)/1.8'''

tF = float (input("Digite a temperatura em Fº(Fahrenheit): "))

tC = (tF-32)/1.8

print("Temperatura em Celsius: {:.1f}".format(tC))
