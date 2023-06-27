'''Construa um programa que leia uma temperatura em Fahrenheit e converta-a para
Celsius. Sabe-se que: C=(f-32)/1.8'''

tF = float (input("Digite a temperatura em Fº(Fahrenheit): "))

tC = (tF-32)/1.8

print("{:.1f}ºF = {:.1f}ºC".format(tF, tC))
