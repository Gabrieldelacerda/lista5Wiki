def valorPagamento(valor_prestacao, dias_atraso):
    if dias_atraso == 0:
        return valor_prestacao
    else:
        multa = valor_prestacao * 0.03
        juros = valor_prestacao * (0.001 * dias_atraso)
        total_pagar = valor_prestacao + multa + juros
        return total_pagar

def relatorio_do_dia(prestacoes_pagas, valor_total):
    print("\nRelatório do dia:")
    print(f"Quantidade de prestações pagas: {prestacoes_pagas}")
    print(f"Valor total recebido: R${valor_total:.2f}")

def main():
    prestacoes_pagas = 0
    valor_total = 0

    while True:
        valor_prestacao = float(input("\nDigite o valor da prestação (ou 0 para encerrar): "))
        if valor_prestacao == 0:
            break

        dias_atraso = int(input("Digite o número de dias em atraso: "))

        valor_a_pagar = valorPagamento(valor_prestacao, dias_atraso)
        print(f"Valor a ser pago: R${valor_a_pagar:.2f}")

        prestacoes_pagas += 1
        valor_total += valor_a_pagar

    relatorio_do_dia(prestacoes_pagas, valor_total)

if __name__ == "__main__":
    main()