import tkinter as tk
from tkinter import ttk, messagebox
import time

class calc_ohm:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title('Pattern')
#         self.win.geometry('300x300')
        
        #Ferramentas
        self.titulo = ttk.Label(self.win, text= 'CALCULADORA BÁSICA') # Etiqueta (Label)
        self.lbl_tensao = ttk.Label(self.win, text= 'Valor 1') # Etiqueta (Label)
        self.lbl_resistencia = ttk.Label(self.win,text= 'Valor 2') # Etiqueta (Label)
        self.lbl_resultado = ttk.Label(self.win, text= ' ') # Etiqueta (Label)
        self.txt_tm1 = ttk.Entry(self.win) # Caixa de texto (entrada de dados)
        self.txt_tm2 = ttk.Entry(self.win) # Caixa de texto (entrada de dados)
        self.btn_calcular = ttk.Button(self.win, text= 'Calcular',command= self.acao_calcular) # Adiciona o Button
        self.btn_fechar = ttk.Button(self.win, text= 'Fechar',command= self.acao_fechar) # Adiciona o Button
        self.frame1 = ttk.LabelFrame(self.win, text='Frame01')
        
        self.estado_selecao = tk.StringVar(value = 'VL1') #Cria objeto tipo texto do tkinter
        self.RadioB1 = ttk.Radiobutton(self.frame1, text='SOM', variable=self.estado_selecao, value='VL1') # Pode se add o 'command'
        self.RadioB2 = ttk.Radiobutton(self.frame1, text='SUB', variable=self.estado_selecao, value='VL2') # Pode se add o 'command'
        self.RadioB3 = ttk.Radiobutton(self.frame1, text='MUL', variable=self.estado_selecao, value='VL3') # Pode se add o 'command'
        self.RadioB4 = ttk.Radiobutton(self.frame1, text='DIV', variable=self.estado_selecao, value='VL4') # Pode se add o 'command'
        
        #Montagem
        self.titulo.grid(row= 0, column= 0, columnspan= 2)
        self.lbl_tensao.grid(row= 1, column= 0)
        self.lbl_resistencia.grid(row= 2, column= 0)
        self.txt_tm1.grid(row= 1, column= 1)
        self.txt_tm2.grid(row= 2, column= 1)
        self.btn_calcular.grid(row= 4, column= 0, columnspan= 2, sticky= 'ew',padx= 10, pady= 23)
        self.lbl_resultado.grid(row= 5, column= 0, columnspan= 2)
        self.btn_fechar.grid(row= 6, column= 1, sticky= 'es')
        
        self.frame1.grid(row= 3, column=0)
        self.frame1.config(borderwidth=5, width=75)
        
        self.RadioB1.grid(row= 3, column= 0)
        self.RadioB2.grid(row= 3, column= 1)
        self.RadioB3.grid(row= 3, column= 2)
        self.RadioB4.grid(row= 3, column= 3)
        
#         self.RadioB1.pack()
#         self.RadioB2.pack()
#         self.RadioB3.pack()
#         self.RadioB4.pack()
        
        self.win.mainloop()
        
    def acao_calcular(self): # Ação do Button        
        match self.estado_selecao.get():
            case 'VL1':
                valor = int(self.txt_tm1.get()) + int(self.txt_tm2.get())
                self.lbl_resultado.config(text= 'O resultado da soma é: {}'.format(valor))
            case 'VL2':
                valor1 = int(self.txt_tm1.get()) - int(self.txt_tm2.get())
                self.lbl_resultado.config(text= 'O resultado da subtração é: {}'.format(valor1))
            case 'VL3':
                valor2 = int(self.txt_tm1.get()) * int(self.txt_tm2.get())
                self.lbl_resultado.config(text= 'O resultado da multiplicação é: {}'.format(valor2))
            case 'VL4':
                valor3 = int(self.txt_tm1.get()) / int(self.txt_tm2.get())
                self.lbl_resultado.config(text= 'O resultado da divisão é: {:.3f}'.format(valor3))
                
        self.txt_tm1.delete(0, "end")
        self.txt_tm2.delete(0, "end")

                
    def acao_fechar(self): # Ação do Button
        exit = messagebox.askyesno('Finalizar', 'Já saindo ?', icon='question')
        if exit == True:
            self.win.destroy()
        else:
            self.lbl_resultado.config(text='')
        
if __name__ == "__main__":
    win = calc_ohm()
