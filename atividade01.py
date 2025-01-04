idade = int(input('Qual a sua idade?'))
if idade >= 0 and idade < 15:
    print('Você é uma criança')
elif idade >=15 and idade <30:
    print('Você é um jovem')
elif idade >=30 and idade <60:
    print('Você é um adulto')
else:
    print('Você é um idoso')