'''
6) Fazer um programa que pergunte uma temperatura ao usuário, em graus Fahrenheit, e apresente esta
temperatura convertida em graus Celsius. A fórmula da conversão é c	=	(f	–	32)	x	5	:	9	, onde c	 é a temperatura
em graus Celsius e f em Fahrenheit.
'''

f = float(input("Informe a temperatura em graus Fahrenheit: "))

c = (f - 32) * 5/9
#print(f, "graus Fahrenheit =" ,c," graus celsius")
#print(" {} graus Fahrenheit = {} graus celsius ".format(f,c))  printf no java
#print( f"{f} graus Fahrenheit = {c} graus celsius ")

print(f"{f:.1f} graus Fahrenheit = {c:.1f} graus Celsius")
