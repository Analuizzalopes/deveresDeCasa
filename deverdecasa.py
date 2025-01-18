from time import sleep 
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
d = int(input('Digite o quarto número: '))
maior = a
if b > a and b > c and b > d:
    maior = b
elif c > a and c > b and c > d:
    maior = c
elif d > a and d > b and d > c:
    maior = d
menor = a
if b < a and b < c and b < d:
    menor = b
elif c < a and c < b and c < d:
    menor = c
elif d < a and d < b and d < c:
    menor = d
print('O maior valor é....')
sleep(2)
print(f'{maior}')
sleep(1)
print('E o menor valor é....')
sleep(2)
print(f'{menor}')