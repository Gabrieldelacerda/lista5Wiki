def contar_digitos(numero):
    return len(str(numero))

numero = int(input("Digite um número: "))
print(f"O número {numero} tem {contar_digitos(numero)} dígitos.")