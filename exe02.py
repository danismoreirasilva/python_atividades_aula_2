
#vai até 101 porque foi solicitado escrever os números de 10 a 100.
for num in range(10, 101):
    if num % 2 == 0:
        print(f'{num} - é Par')
    else:
        print(f'{num} - é Ímpar')