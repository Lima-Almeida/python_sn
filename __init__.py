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
dimensao_quadrado = 20 #atributo importante, determina o tamanho do quadrado da grid (em pixels)
blocos_por_segundo = 10
altura = 400
largura = 500
periodo = 1000 // blocos_por_segundo
direcao = "baixo"
pontuacao = 0
qnt_quadrados = (largura/dimensao_quadrado) * (altura/dimensao_quadrado)
virou = False
atualizou = False
bot = False
supervelocidade = False

def get_coord_aleatoria(cobra):
    x = random.randint(0, ((largura / dimensao_quadrado) - 1)) * dimensao_quadrado
    y = random.randint(0, ((altura / dimensao_quadrado) - 1)) * dimensao_quadrado
    #Checa se o novo ponto será spawnado em cima do corpo da cobra (se sim, gera nova coordenada)
    for partes in cobra.coordenadas[1:]:
        if partes[0] == x and partes[1] == y:
            #print("OK")
            x, y = get_coord_aleatoria(cobra)
    return [x, y]


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
    def __init__(self, cobra):
        x, y = get_coord_aleatoria(cobra)
        self.coordenadas = [x, y]
        canvas.create_oval(x, y, x+dimensao_quadrado, y+dimensao_quadrado, fill="#0000FF", tag="ponto")

def checagem_colisoes(cobra):
    x, y = cobra.coordenadas[0]

    #Checa se houve colisão da cabeça da cobra com as bordas do mapa
    if x < 0 or x >= largura:
        return True
    elif y < 0 or y >= altura:
        return True
    
    #Checa se houve uma colisão da cabeça da cobra com a própria cobra
    for partes in cobra.coordenadas[1:]:
        if x == partes[0] and y == partes[1]:
            return True
        
    return False


def fim_de_jogo():
    canvas.delete(all)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('consolas', 70), text="GAME OVER", fill="red", tag="gameover")
    

def vitoria():
    canvas.delete(all)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('consolas', 70), text="VICTORY", fill="blue", tag="victory")


def ligar_bot(event=None):
    global bot
    bot = not bot

velocidade_anterior = 0
def super_velocidade(event=None):
    global periodo, supervelocidade, blocos_por_segundo, velocidade_anterior
    velocidade_anterior = blocos_por_segundo
    supervelocidade = not supervelocidade
    if supervelocidade:
        periodo = 0
    else:
        blocos_por_segundo = velocidade_anterior

def aumentar_velocidade(event=None):
    global blocos_por_segundo
    if(blocos_por_segundo >= 1000):
        return
    else:
        if blocos_por_segundo < 100 and blocos_por_segundo >= 10:
            blocos_por_segundo += 10
        elif blocos_por_segundo < 10:
            blocos_por_segundo += 1
        else:
            blocos_por_segundo += 100


def reduzir_velocidade(event=None):
    global blocos_por_segundo
    if(blocos_por_segundo <= 2):
        return
    else:
        if blocos_por_segundo <= 10:
            blocos_por_segundo -= 1
        elif blocos_por_segundo > 10 and blocos_por_segundo <= 100:
            blocos_por_segundo -= 10
        else:
            blocos_por_segundo -= 100

#Bot bem básico que fiz pra checar algumas condições (como a de vitória) sem precisar de fato jogar o jogo até vencer
#Bot pode ser ativado e desativado pela variável bot (booleana)
indo_direita = True
def bot_cobra(x, y):
    coordenada_final_x = largura - dimensao_quadrado
    coordenada_final_y = altura - 2*dimensao_quadrado
    coordenada_y_volta = altura - dimensao_quadrado
    global indo_direita
    global direcao
    global virou
    if(largura/dimensao_quadrado) % 2 == 0:
        if indo_direita:
            if y == coordenada_y_volta and direcao == "baixo" and atualizou == False:
                direcao = "direita"
                virou = True

            if virou and atualizou and y == coordenada_y_volta and direcao == "direita":
                direcao = "cima"
                virou = False

            if y == dimensao_quadrado and direcao == "cima" and atualizou == False:
                direcao = "direita"
                virou = True

            if virou and atualizou and y == dimensao_quadrado and direcao == "direita":
                direcao = "baixo"
                virou = False

            if x == coordenada_final_x:
                indo_direita = False
        else:
            if y == coordenada_y_volta and direcao == "baixo" and atualizou == False:
                direcao = "esquerda"
                virou = True

            if y == 0 and direcao == "cima" and atualizou == False:
                direcao = "esquerda"
                virou = True

            if virou and atualizou and y == coordenada_y_volta and x == 0 and direcao == "esquerda":
                direcao = "cima"
                virou = False
                indo_direita = True

            if virou and atualizou and y == 0 and x == 0 and direcao == "esquerda":
                direcao = "baixo"
                virou = False
                indo_direita = True
    elif(altura/dimensao_quadrado) % 2 == 0:
        if indo_direita:
            if y == coordenada_y_volta and direcao == "baixo" and atualizou == False:
                direcao = "direita"

            if x == coordenada_final_x and direcao == "direita" and atualizou == False:
                direcao = "cima"
                virou = True

            if virou and atualizou and x == coordenada_final_x and direcao == "cima":
                direcao = "esquerda"
                virou = False

            if x == dimensao_quadrado and direcao == "esquerda" and atualizou == False:
                direcao = "cima"
                virou = True

            if virou and atualizou and x == dimensao_quadrado and direcao == "cima":
                direcao = "direita"
                virou = False

            if y == 0:
                indo_direita = False
        else:
            if x == 0 and direcao == "esquerda":
                direcao = "baixo"
                virou = False
                indo_direita = True
    else:
        if indo_direita:
            if y == coordenada_final_y and direcao == "baixo" and atualizou == False:
                direcao = "direita"
                virou = True

            if virou and atualizou and y == coordenada_final_y and direcao == "direita":
                direcao = "cima"
                virou = False

            if y == dimensao_quadrado and direcao == "cima" and atualizou == False:
                direcao = "direita"
                virou = True

            if virou and atualizou and y == dimensao_quadrado and direcao == "direita":
                direcao = "baixo"
                virou = False

            if x == coordenada_final_x:
                indo_direita = False
        else:
            if y == coordenada_y_volta and direcao == "baixo" and atualizou == False:
                direcao = "esquerda"
                virou = True

            if y == 0 and direcao == "cima" and atualizou == False:
                direcao = "esquerda"
                virou = True

            if virou and atualizou and y == coordenada_y_volta and x == 0 and direcao == "esquerda":
                direcao = "cima"
                virou = False
                indo_direita = True

            if virou and atualizou and y == 0 and x == 0 and direcao == "esquerda":
                direcao = "baixo"
                virou = False
                indo_direita = True

def calcula_pos(cobra, ponto):
    x, y = cobra.coordenadas[0]
    global direcao, atualizou, bot, periodo
    if not supervelocidade:
        periodo = 1000 // blocos_por_segundo

    if direcao == "cima":
        y -= dimensao_quadrado
    elif direcao == "baixo":
        y += dimensao_quadrado
    elif direcao == "esquerda":
        x -= dimensao_quadrado
    elif direcao == "direita":
        x += dimensao_quadrado

    if bot:
        bot_cobra(x, y)

    cobra.coordenadas.insert(0, (x, y))
    quadrado = canvas.create_rectangle(x, y, x+dimensao_quadrado, y+dimensao_quadrado, fill="#FFFFFF")
    cobra.quadrados.insert(0, quadrado)
    lbl_velocidade.config(text="Velocidade:{} b/s".format(blocos_por_segundo))

    if x == ponto.coordenadas[0] and y == ponto.coordenadas[1]:
        global pontuacao
        pontuacao += 1
        label.config(text="Pontos:{}".format(pontuacao))
        canvas.delete("ponto")
        ponto = Ponto(cobra)
    else:
        del cobra.coordenadas[-1]
        canvas.delete(cobra.quadrados[-1])
        del cobra.quadrados[-1]

    if len(cobra.coordenadas) == qnt_quadrados:
        vitoria()
    
    if checagem_colisoes(cobra):
        fim_de_jogo()
    else:
        janela.after(periodo, calcula_pos, cobra, ponto)
        if virou:
            atualizou = True
        else:
            atualizou = False

#Checa se a direcao para qual o jogador está tentando virar é válida
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
#Setando texto de pontuação e tela do jogo
lbl_velocidade = ttk.Label(janela, text="velocidade:{} b/s".format(blocos_por_segundo), font=('consolas', 20))
label = ttk.Label(janela, text="Pontos:{}".format(pontuacao), font=('consolas', 20))
label.pack()
lbl_velocidade.pack()
canvas = tk.Canvas(janela, bg="#000000", height=altura, width=largura)
canvas.pack()
janela.update()

#Setando as teclas/controles do jogo (setinhas do teclado)
janela.bind('<Left>', lambda event: mudar_direcao("esquerda"))
janela.bind('<Right>', lambda event: mudar_direcao("direita"))
janela.bind('<Up>', lambda event: mudar_direcao("cima"))
janela.bind('<Down>', lambda event: mudar_direcao("baixo"))
janela.bind('b', ligar_bot)
janela.bind('s', super_velocidade)
janela.bind('z', aumentar_velocidade)
janela.bind('x', reduzir_velocidade)

#Instanciando cobra e ponto
cobra = Cobra()
ponto = Ponto(cobra)
#Chamando função que roda o jogo
calcula_pos(cobra, ponto)
janela.mainloop()