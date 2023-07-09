cores_prim = {'preto':0, 'marrom':1, 'vermelho':2, 'laranja':3, 'amarelo':4,
              'verde':5, 'azul':6, 'violeta':7, 'cinza':8, 'branco':9}
cores_mult4 = {'preto':1, 'marrom':10, 'vermelho':100, 'laranja':1000, 'amarelo':10000,
              'verde':100000, 'azul':1000000, 'violeta':10000000}
cores_mult5 = {'preto':1, 'marrom':10, 'vermelho':100, 'laranja':1000, 'amarelo':10000,
              'verde':100000, 'azul':1000000, 'violeta':10000000, 'cinza':100000000,
               'branco':1000000000, 'ouro':0.1,'prata':0.01}
tolerancia = {'marrom':'± 1%', 'vermelho':'± 2%','verde':'± 0.5%', 'azul':'± 0.25%',
              'violeta':'± 0.1%','cinza':'± 0.05%', 'dourado':'± 5%','prateado':'± 10%' ,'branco':'± 20%'}

lista_resis = list()

while True: 
    cor = input('Digite as cores do resitor (ou fim para encerrar): ').lower()
    if cor.upper() == 'FIM':
        break
    lista_resis.append(cor)

if len(lista_resis) == 4:
    prim = cores_prim[lista_resis[0]]
    sec = cores_prim[lista_resis[1]]
    terc = cores_mult4[lista_resis[2]]
    quart = tolerancia[lista_resis[3]]
    print('O resistor tem valor de ', int(str(prim) + str(sec))*terc,'Ohms', quart)
elif len(lista_resis) == 5:
    prim = cores_prim[lista_resis[0]]
    sec = cores_prim[lista_resis[1]]
    terc = cores_prim[lista_resis[2]]
    quart = cores_mult5[lista_resis[3]]
    quint = tolerancia[lista_resis[4]]
    print('O resistor tem valor de ', int(str(prim) + str(sec) + str(terc))*quart,'Ohms', quint)
else:
    print('Falta/Há excesso de cores')
    exit()
        
