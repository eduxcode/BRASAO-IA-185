# -*- coding: utf-8 -*-

# Leia o número do funcionário (inteiro)
numero_funcionario = int(input("Digite o número do funcionário: "))

# Leia a quantidade de horas trabalhadas (inteiro)
horas_trabalhadas = int(input("Digite a quantidade de horas trabalhadas: "))

# Leia o valor que o funcionário recebe por hora (ponto flutuante)
valor_por_hora = float(input("Digite o valor que o funcionário recebe por hora: "))

# Calcule o salário
salario = horas_trabalhadas * valor_por_hora

# Imprima o número do funcionário
print(f"NUMBER = {numero_funcionario}")

# Imprima o salário formatado com duas casas decimais
print(f"SALARY = R$ {salario:.2f}")