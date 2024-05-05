def somaImposto(taxaImposto, custo):
    imposto = custo * (taxaImposto / 100)
    custo_com_imposto = custo + imposto
    return custo_com_imposto

taxaImposto = float(input("Digite a taxa de imposto (em porcentagem): "))
custo = float(input("Digite o custo do item antes do imposto: "))

custo_com_imposto = somaImposto(taxaImposto, custo)

print(f"O custo do item com imposto é R${custo_com_imposto:.2f}")