valor1 = 8.75217
valor2 = 73932.6
valor3 = 11.369

#formatação paenas como valor float
print("valor 1: {:f}".format(valor1))
print(f"valor 1: {valor1} ")
print("---------------------------")

#formatação com decimal de 2 dígitos

print("valor 1: {:.2f}".format(valor1))
print("valor 2: {:.2f}".format(valor2))
print("valor 3: {:.2f}".format(valor3))
print("")
print(f"valor 1: {valor1:.2f}")
print(f"valor 2: {valor2:.2f}" )
print(f"valor 3: {valor3:.2f}")
print("---------------------------")

#formatação com separador de milhares e decimal com 2 dígitos

print("valor 2: {:,.2f}".format(valor2))
print("---------------------------")
#formatação com total de dez dígitos (contando números e pontos), sendo 2 decimais

print("valor 1: {:10.2f}".format(valor1))
print("valor 2: {:10.2f}".format(valor2))
print("valor 3: {:10.2f}".format(valor3))
print("")
print(f"valor 1: {valor1:10.2f}")
print(f"valor 2: {valor2:10.2f}")
print(f"valor 3: {valor3:10.2f}")
print("---------------------------")
#semelhante ao anterior, mas preenche casas antes do ponto com zero quando necessário

print("valor 1: {:010.2f}".format(valor1))
print("valor 2: {:010.2f}".format(valor2))
print("valor 3: {:010.2f}".format(valor3))
print("")
print(f"valor 1: {valor1:010.2f}")
print(f"valor 2: {valor2:010.2f}")
print(f"valor 3: {valor3:010.2f}")
print("---------------------------")

valor4 = 0.7536

#formatação exibindo em percentual com decimal 1 dígito

print(f"valor 4: {valor4:.1%}")
print("---------------------------")

#incluindo R$ antes do valor e substituindo a vírgula do milhar por um underline

texto_valor2 = f"R$ {valor2:_.2f}"
print(f"Texto valor 2: {texto_valor2}")
print("---------------------------")

#substituindo o que é ponto por vírgula e o que é underline por ponto
texto_valor_br = texto_valor2.replace(".",",").replace( "_", ".")
print(f"Texto Valor BR: {texto_valor_br}")