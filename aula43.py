"""
texto = 'Python'

i = 0
tamanho_string = len(texto)

while i < tamanho_string:
    print(texto[i], i)
    i += 1
"""

texto = 'Teste'
novo_texto = ''
for letra in texto:
    novo_texto += (f'*{letra}')
    print(letra)
print(novo_texto + '*')