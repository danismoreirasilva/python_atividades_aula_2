#Validando os dados para que o valor digitado não gere erro na execução caso não seja numérico.
repetir = True
while repetir:
    n = input('Digite a quantidade de números desejados: ')
    if n.isnumeric():
        n = int(n)
        if n <= 1:
            print('O valor digitado deve ser maior do que 1!')
        else:
            repetir = False
    else:
        print('O valor digitado deve ser numérico e maior do que 1')

soma = 0
for i in range(n):
    num = int(input(f'Digite o {i+1}º valor: '))
    soma += num

print(f'O resultado da soma de todos os valores é: {soma}!')
