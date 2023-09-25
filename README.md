# python_sn
Código do jogo da cobrinha
Referenciado de -> https://www.geeksforgeeks.org/snake-game-using-tkinter-python/

O objetivo principal deste código é oferecer aos alunos do "Olá, Mundos!" (@olamundos no instagram) uma proposta de valor partindo da linguagem Python. Em outras palavras, a ideia é mostrar que é possível produzir coisas muito legais somente com o Python e algum estudo.

Obtive uma boa parte da lógica do código do link referenciado no início do documento, porém, apenas a lógica do código foi utilizada, sendo que algumas alterações foram, e serão, feitas ao longo do tempo. Apesar disso, o código foi inteiro reescrito (em português) e avaliado por mim, também inseri comentários para que os trechos ficassem bem explicados

Lista de alterações feitas:
-Ao jogar um pouco notei que havia chance do ponto spawnar "dentro" do corpo da cobra. Para contornar isso adicionei uma nova lógica de atribuição de coordenadas para a classe Ponto. Toda vez que um novo objeto Ponto vai ser instanciado, no momento de gerar as coordenadas aleatórias com a função get_coord_aleatoria, a função checa se as coordenadas que serão passadas são iguais às coordenadas de algum dos segmentos do corpo da cobra, se forem, novas coordenadas são geradas e testadas, até não serem mais iguais.

-Adicionei uma tela de vitória para quando o jogador vencer o jogo

-Adicionei um bot para que a cobrinha ande por todos os quadrados do campo automaticamente. Isso foi feito para testar algumas funções sem ter a preocupação de jogar o jogo sem morrer. Também adicionei um botão de liga/desliga para o bot (tecla 'B')

-Adicionei uma função de aumentar/reduzir a velocidade da cobrinha. (Tecla 'Z' para aumentar e 'X' para reduzir)

-Completei a lógica do bot para mapas com número par de colunas. Mantive também uma opção de bot para números ímpares de colunas e linhas, mas aviso previamente que este não é capaz de completar o jogo, pois este caso se trata de um problema NP-difícil

Lista de alterações pendentes:
-Quando duas teclas (cima e esquerda, direita e cima, baixo e direita, etc.) são pressionadas muito rapidamente, existe a chance de a cobra simplesmente burlar a lógica da função mudar_direcao e dar um giro de 180º (mudar a direção mas permanecer na mesma linha/coluna). Quando isso ocorre geralmente acontece um game over pois a cabeça da cobra colide com seu corpo (já que estão na mesma linha). Ainda é necessário desenvolver uma solução para essas ocasiões.

-Completar a lógica do bot para linhas pares.
