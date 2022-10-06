import random

print('Bem Vindo ao Gerador de Senha!!')
print('-'*32)

chars = 'abcdefghijklmnopqrstuvwxzABCDEFGHIJKLMNOPQRSTUVWXZ!@#$%¨&*().,?0123456789'

number = input('Quantidade de Senhas para gerar: ')
number = int(number)

length = input('Entre com o Tamanho da Senha: ')
length = int(length)

print('\nAqui esta(ão) sua(s) senha(s):')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
