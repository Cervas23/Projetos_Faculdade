lista_r = list()
listap = list()

while True:
    modo = input('Digite se série ou paralelo: ').upper()
    while True: 
        resist = input('Digite o valor do resistor (ou fim para encerrar): ')
        if resist.upper() == 'FIM':
            break
        lista_r.append(float(resist))

    match modo:
        case 'SÉRIE':
            resul_serie = sum(lista_r)
            print(f'Resistor equivalente é: {resul_serie:.3f} Ohms')
        case 'PARALELO':
            for x in lista_r:
                val_pot = round(pow(x, -1), 3)
                listap.append(float(val_pot))
            resul_para = sum(listap)
            print(f'Resistor equivalente é: {resul_para:.3f} Ohms')
        case _:
            print('modo inválido')
            exit()
            
    again = input("Reiniciar (s/n) ")

    if 's' in again:
        lista_r.clear()
        listap.clear()
        continue
    else:
        print("Até a próxima")
        break
