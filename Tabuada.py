n=m=0

while True:
    n=int(input('Qual o numero que será multiplicado... \n (numeros negativos,finalizara o Terminal.) ->'))
    if n<=-1:
        break
    print(50*'-')
    for mul in range(1,11):
        res=n*mul
        
        print(f'{n} * {mul} = {res}')
    print(50*'-')
print('Fim')
