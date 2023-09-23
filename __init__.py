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
tamanho_inicial = 2
dimensao_quadrado = 20 #atributo importante, determina o tamanho do quadrado (em pixels)
altura = 500
largura = 500
velocidade = 200
direcao = "baixo"
pontuacao = 0

def get_coord_aleatoria():
    n = random.randint(0, ((altura / dimensao_quadrado) - 1)) * dimensao_quadrado
    return n


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


class Ponto:
    def __init__(self):
        x = get_coord_aleatoria()
        y = get_coord_aleatoria()
        self.coordenadas = [x, y]
        canvas.create_oval(x, y, x+dimensao_quadrado, y+dimensao_quadrado, fill="#0000FF", tag="ponto")

def checagem_colisoes(cobra):
    x, y = cobra.coordenadas[0]

    if x < 0 or x >= largura:
        return True
    elif y < 0 or y >= altura:
        return True
    
    for partes in cobra.coordenadas[1:]:
        if x == partes[0] and y == partes[1]:
            return True
        
    return False


def fim_de_jogo():
    canvas.delete(all)
    canvas.create_text(canvas.winfo_width()/2, 
                       canvas.winfo_height()/2,
                       font=('consolas', 70), 
                       text="GAME OVER", fill="red", 
                       tag="gameover")
    

def calcula_pos(cobra, ponto):
    x, y = cobra.coordenadas[0]

    if direcao == "cima":
        y -= dimensao_quadrado
    elif direcao == "baixo":
        y += dimensao_quadrado
    elif direcao == "esquerda":
        x -= dimensao_quadrado
    elif direcao == "direita":
        x += dimensao_quadrado

    cobra.coordenadas.insert(0, (x, y))
    quadrado = canvas.create_rectangle(x, y, x+dimensao_quadrado, y+dimensao_quadrado, fill="#FFFFFF")
    cobra.quadrados.insert(0, quadrado)

    if x == ponto.coordenadas[0] and y == ponto.coordenadas[1]:
        global pontuacao
        pontuacao += 1
        label.config(text="Pontos:{}".format(pontuacao))
        canvas.delete("ponto")
        ponto = Ponto()
    else:
        del cobra.coordenadas[-1]
        canvas.delete(cobra.quadrados[-1])
        del cobra.quadrados[-1]
    
    if checagem_colisoes(cobra):
        fim_de_jogo()
    else:
        janela.after(velocidade, calcula_pos, cobra, ponto)


def mudar_direcao(prox_direcao):
    global direcao
    if prox_direcao == "direita" and direcao != "esquerda":
        direcao = "direita"
    elif prox_direcao == "esquerda" and direcao != "direita":
        direcao = "esquerda"
    elif prox_direcao == "cima" and direcao != "baixo":
        direcao = "cima"
    elif prox_direcao == "baixo" and direcao != "cima":
        direcao = "baixo"


#Mainloops
#menu.mainloop()
label = ttk.Label(janela, text="Points:{}".format(pontuacao), 
              font=('consolas', 20))
label.pack()
canvas = tk.Canvas(janela, bg="#000000", height=altura, width=largura)
canvas.pack()
janela.update()

janela.bind('<Left>', 
            lambda event: mudar_direcao("esquerda"))
janela.bind('<Right>', 
            lambda event: mudar_direcao("direita"))
janela.bind('<Up>', 
            lambda event: mudar_direcao("cima"))
janela.bind('<Down>', 
            lambda event: mudar_direcao("baixo"))

#Instanciando cobra e ponto
cobra = Cobra()
ponto = Ponto()
calcula_pos(cobra, ponto)
janela.mainloop()