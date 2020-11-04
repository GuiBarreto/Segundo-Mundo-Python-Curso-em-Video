print("-=-" * 11)
print(" ANALISADOR DE CRÉDITO APROVADO")
print("-=-" * 11)
casa = float(input("Qual o valos da casa? R$ "))
salario = float(input("Qual o seu salário? R$ "))
anos = float(input("Em quantos anos pretende pagar? " ))
meses = (anos * 12) 
credito = salario * 0.3
parcela = casa / meses
if credito >= parcela:
    print('PARABÉNS SEU CRÉDITO FOI APROVADO!!! Será {:.0f} parcelas de R${:.2f} o seu financiamento !' .format(meses, parcela))
else:
    print('CRÉDITO NEGADO ! Infelizmente não foi aprovado para financiamento')
