def verificar_positivo(numero):
    if numero > 0:
        return 'P'
    else:
        return 'I'

numero = int(input("Digite um número: "))

resultado = verificar_positivo(numero)
print(f"O resultado é {resultado}")