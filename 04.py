quantia = int(input('Quantia de pares desejados: '))
par_impar = input('Par ou impar? ').lower()
contador = 0
numero = 1
opcoes = ['par', 'impar']

if par_impar not in opcoes:
    print ('Digite "par" ou "impar"')
else:
    while contador < quantia:
        if par_impar == 'par':
            if numero %2 == 0:
                print (f'Sua quantia de pares é: {numero}')
                contador +=1

        elif par_impar == 'impar':
            if numero %2 == 1:
                print (f'Sua quantia de Impares é: {numero}')
                contador +=1
        numero +=1