import tkinter as tk
import tkinter.ttk as ttk
import random

#Setando as janelas
#menu = tk.Tk()
janela = tk.Tk()

#Setando os componentes do menu
# frame1 = ttk.Frame()
# frame2 = ttk.Frame(relief=tk.RAISED, borderwidth=3)
# lbl_title = ttk.Label(master=frame1, text="SNG!")
# btn_inicio = ttk.Button(master=frame2, text="Começar")
# frame1.grid()
# frame2.pack()
# lbl_title.pack()
# btn_inicio.pack()

#Setando os componentes da janela principal

#Setando informações da cobra
tamanho_inicial = 1
dimensao_quadrado = 25
class Cobra:
    def __init__(self):
        self.tamanho = tamanho_inicial
        self.coordenadas = []
        self.quadrados = []

        for i in range(0, tamanho_inicial):
            self.coordenadas.append([0,0])

        for x, y in self.coordenadas:
            quadrado = canvas.create_rectangle(x, y, x+dimensao_quadrado, y+dimensao_quadrado, fill="#FFFFFF", tag="cobra")
        self.quadrados.append(quadrado)


#Mainloops
#menu.mainloop()
altura = 500
largura = 500
canvas = tk.Canvas(janela, bg="#000000", height=altura, width=largura)
canvas.pack()
janela.mainloop()