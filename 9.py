def numero_reverso(numero):
    reverso = 0
    while numero > 0:
        digito = numero % 10
        reverso = reverso * 10 + digito
        numero = numero // 10
    return reverso

numero = int(input("Digite um número inteiro: "))

print(f"O reverso de {numero} é {numero_reverso(numero)}")