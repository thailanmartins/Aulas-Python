nome = 'Thailan Martins'
altura = 2.00
peso = 115
imc = peso / (altura ** 2) # IMC = peso / (altura x altura).

#f-strings
linha_1 = f'{nome} tem {altura:,.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu {imc:.2f} é'

print(linha_1)
print(nome, 'tem', altura, 'de altura,', 'pesa', peso, 'quilos e seu IMC é ', imc)

# Thailan Martins tem 2.00 de altura,
# pesa 115 quilos e seu IMC é
# 28.75

print(...) # ... é um place holder

nome = "Luiz"
idade = 23
formato = '{1} tem {0} anos'