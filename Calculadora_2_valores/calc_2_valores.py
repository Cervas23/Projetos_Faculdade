num1, num2 = input('Digite 2 numeros separdos por espaço: ').split()
num1, num2 = int(num1), int(num2)
modo = input('Digite qual operção matemática você deseja: ')
match modo:
    case 'soma':
        sum = num1 + num2
        print('O resultado da soma é: {}'.format(sum))
    case 'subtração':
        sub = num1 - num2
        print('O resultado da subtração é: {}'.format(sub))
    case 'divisão':
        div = num1 / num2
        print(f'O resultado da divisão é: {div:.3f}')
    case 'multiplicação':
        mult = num1 * num2
        print('O resultado da multiplicação é: {}'.format(mult))
    case _:
        print("Operação {} não válida".format(modo))
    
