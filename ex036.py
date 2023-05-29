casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar um casa de R${:.2f} em {} anos, a prestação será de {:.2f}'.format(casa, anos, prestacao))
if prestacao > minimo:
    print('Empréstimo invalido')
else:
    print('Financiamento validado')
