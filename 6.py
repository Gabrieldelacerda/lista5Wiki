def converter_12_horas(horas, minutos):
    periodo = 'A' if horas < 12 else 'P'
    horas = horas if horas <= 12 else horas - 12
    return horas, minutos, periodo

def imprimir_horario(horas, minutos, periodo):
    print(f"{horas}:{minutos:02d} {periodo}.M.")

def main():
    while True:
        try:
            horas = int(input("Digite as horas (0-23): "))
            minutos = int(input("Digite os minutos (0-59): "))
            if horas < 0 or horas > 23 or minutos < 0 or minutos > 59:
                print("Por favor, insira horas entre 0 e 23 e minutos entre 0 e 59.")
                continue
            horas_12, minutos, periodo = converter_12_horas(horas, minutos)
            imprimir_horario(horas_12, minutos, periodo)
        except ValueError:
            print("Entrada inválida. Por favor, insira números inteiros.")
        finally:
            repetir = input("Deseja converter outro horário? [S/N]: ").upper()
            if repetir != 'S':
                break

if __name__ == '__main__':
    main()