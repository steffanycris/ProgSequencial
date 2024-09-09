'''
Elaborar um programa que pergunte quatro valores inteiros e apresente 2 resultados:
a) Resultado de suas adições
b) Resultado de suas multiplicações
'''

n1 = int(input("Informe o primeiro número "))    #int() -> classificando a variável como inteiro
n2 = int(input("Informe o segundo número "))
n3 = int(input("Informe o terceiro número "))
n4 = int(input("Informe o quarto número "))

'''
CONVERSÕES DE TIPO NO INPUT:

- inteiro -> int()
- real -> float()
- caracter -> não é preciso fazer nada, já que é string por padrão

'''

adicao = n1+n2+n3+n4
mult = n1*n2*n3*n4

print("O resultado da adição dos números informados é: ",adicao)
print("O resultado da multiplicação dos números informados é: ",mult)