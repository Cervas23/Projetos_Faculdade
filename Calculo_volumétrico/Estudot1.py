import math

class calculadora:
    
    def __init__(self, hcil=None, rcil=None, lcubo=None, resf=None):
        self.hcil = hcil
        self.rcil = rcil
        self.lcubo = lcubo
        self.resf = resf
    
    def cilindro(self):
        self.hcil = int(input('Digite a altura do cilindro: '))
        self.rcil = input('Digite o raio do cilindro: ')
        volcil = pow(int(self.rcil), 2) * 3.14159 * self.hcil #math.pi pow(variavel_base , exponencial)
        cil = print(f'O volume do cilindro é de {volcil:.3f} cm³')
        return cil
    
    def cubo(self):
        self.lcubo = input('Digite o lado do cubo: ')
        volcub = pow(int(self.lcubo), 3)
        cb = print('O volume do cubo é de {:.3f} cm³'.format(volcub))
        return cb
    
    def esfera(self):
        self.resf = input('Digite o raio da esfera: ')
        esf = (4/3) * math.pi * pow(int(self.resf), 3)
        era = print('O volume da esfera é de {:.3f} cm³'.format(esf))
        return era


while True:
    mod = input('Escolha entre o volume de Cilindro(A), Cubo(B) ou Esfera(C): ').upper()
#     modo = mod.upper()
    
    match mod:
        case 'A':
            teste = calculadora()
            teste.cilindro()
        case 'B':
            teste = calculadora()
            teste.cubo()
        case 'C':
            teste = calculadora()
            teste.esfera()
        case _:
            print('Escolha entre A B C!')
            
    fim = input('Deseja finalizar S/N ? ').upper()
    if fim == 'S':
        break
    else:
        continue

        