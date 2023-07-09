import tkinter as tk
from tkinter import ttk
import sqlite3

class prompt:
    def __init__(self):
        self.calc = tk.Tk()
        self.calc.geometry('350x700')
        self.calc.title('INTEGRAÇÃO COM SQLITE')
        
        #Ferramentas
        self.titulo = ttk.Label(self.calc, text= 'LISTA DE EQUIP.')
        self.quadro1 = ttk.LabelFrame(self.calc, text='Consulta')
        self.quadro2 = ttk.LabelFrame(self.calc, text='Cadastro')
        
        self.lista_equip = tk.Text(self.quadro1)
        self.btn_att = ttk.Button(self.quadro1, text= 'Atualizar', command= self.preencher_descricao)
        
        self.lista_label = list()
        textos=('Descrição', 'Valor', 'Marca', 'Modelo')
        self.lista_entry = list()
        
        for element in textos:
            self.lista_label.append(ttk.Label(self.quadro2, text= element))
            self.lista_entry.append(ttk.Entry(self.quadro2))

        self.btn_cad = ttk.Button(self.quadro2, text= 'Cadastrar', command= self.cadastrar_equip)

        self.btn_fechar = ttk.Button(self.calc, text= 'Fechar', command= self.acao_fechar)
        
        #Montagem
        self.titulo.pack()
        self.quadro1.pack(fill= 'x')
        self.quadro2.pack(fill= 'x')
        self.btn_fechar.pack()
        
        self.lista_equip.pack()
        self.btn_att.pack()
        
        for ferram in range(4):
            self.lista_label[ferram].grid(row= ferram, column= 0)
            self.lista_entry[ferram].grid(row= ferram, column= 1)
        self.btn_cad.grid(row= 4, column= 0, columnspan= 2, sticky= 'e')
         
        self.calc.mainloop()
        
    
    def acao_fechar(self):
        self.calc.destroy()
        
    def preencher_descricao(self):
        nova_conn = conexao(caminho= 'eca10_2023_1.db')
        lista_equip = nova_conn.consultar_dec()
        self.lista_equip.delete(0.0, 'end')
        for linha in lista_equip:
            self.lista_equip.insert('end', f'{linha[0]}\n')
    
    def cadastrar_equip(self):
        nova_conn = conexao(caminho= 'eca10_2023_1.db')
        nova_conn.inserir(desc= self.lista_entry[0].get(), valor= self.lista_entry[1].get(), marca= self.lista_entry[2].get(), modelo= self.lista_entry[3].get())
        
class conexao:
    def __init__(self, caminho=None):
        self.caminho = caminho
        
    def consultar_dec(self):
        minha_conexao = sqlite3.connect(self.caminho)
        cursor = minha_conexao.cursor()
        cursor.execute('SELECT descricao FROM equipamentos;')
        resp = cursor.fetchall()
        return list(resp)
    
    def inserir(self, desc=None, marca=None, modelo=None, valor=None):
        minha_conexao = sqlite3.connect(self.caminho)
        cursor = minha_conexao.cursor()
        cursor.execute(f"INSERT INTO equipamentos (descricao, marca, modelo, preco) VALUES ('{desc}', '{modelo}', '{marca}', {valor});")
        minha_conexao.commit()
        
        
        
if __name__ == "__main__":
    calc = prompt()
