# Testando código gerado pelo ChatGPT
# Lista de repetição que irá imprimir os números pares divisiveis por 4 usandor for

numeros = list(range(1,101))

for num in numeros:
    if num % 2 == 0 and num % 4 == 0:
        print(num)


# Refinando o código

numeros = list(range(1,101))

print("Números pares divisiveis por 4:")
for num in numeros:
    if num % 2 == 0 and num % 4 == 0:
        print(num, end=" ")
print("\n")

# Com List comprehension 
# Sabemos que é uma comprehension devido a presença dos [], ele resumo o código em uma linha

numeros = list(range(1, 101))

numeros_divisiveis_por_4 = [num for num in numeros if num % 2 == 0 and num % 4 == 0]

print("Números pares divisiveis por 4:")
print(numeros_divisiveis_por_4)
