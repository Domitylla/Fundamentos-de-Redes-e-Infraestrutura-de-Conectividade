# revisao_1_ex37.py
valor_hora = float(input("Quanto você ganha por hora? "))
horas_mes = float(input("Horas trabalhadas no mês: "))
bruto = valor_hora * horas_mes
ir = bruto * 0.11
inss = bruto * 0.08
sindicato = bruto * 0.05
liquido = bruto - ir - inss - sindicato

print(f"Salário Bruto: R$ {bruto:.2f}")
print(f"IR (11%): R$ {ir:.2f}")
print(f"INSS (8%): R$ {inss:.2f}")
print(f"Sindicato (5%): R$ {sindicato:.2f}")
print(f"Salário Líquido: R$ {liquido:.2f}")
