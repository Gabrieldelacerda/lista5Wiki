import random

def embaralhar_palavra(palavra):
    palavra = palavra.lower()
    lista_caracteres = list(palavra)
    random.shuffle(lista_caracteres)
    palavra_embaralhada = ''.join(lista_caracteres)
    return palavra_embaralhada

palavra = input("Digite uma palavra: ")
print(f"Palavra embaralhada: \n{embaralhar_palavra(palavra)}")