import pygame

from jogo_da_velha import criaBoard, fazMovement, \
    printBoard, verficaMoviMovements, VerificaWinner

from minimax import movimentIA

pygame.font.init()

def draw_board (win, board):
    height = 600
    width = 600
    tamanho = 600/3

    for i in range (1, 3):
        pygame.draw.line(win, (0, 0, 0), (0, i*tamanho), (width, i * tamanho), 3)
        pygame.draw.line(win, (0, 0, 0), (i*tamanho, 0), ( i * tamanho, height), 3)
    
    #Desenhando o X e O
    for i in range(3):
        for j in range(3):
            font = pygame.font.SysFont("arial", 100)
            x = j * tamanho
            y = i * tamanho

            if board [i][j] == 'X':
                text = font.render(board[i][j], 1, (255, 0, 0))
                win.blit(text, ((x + 60), (y + 60)))
            elif board[i][j] == 'O':
                text = font.render(board[i][j], 1, (0, 255, 0))
                win.blit(text, ((x + 60), (y + 60)))
        

def redraw_window (win, board):
    win.fill((255, 255, 255))
    draw_board(win, board)

def main ():
    win = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('JOGO DA VELHA')
    
    board = criaBoard()
    
    redraw_window(win, board)
    pygame.display.update()

    jogador = 0 #jogador 1
    ganhador = VerificaWinner(board)

    while not ganhador:
        printBoard(board) #Gerando o tabuleiro
        if jogador == 1:
            linha, coluna = movimentIA(board, jogador)
        else:
            jogou = False
            while not jogou:
            # Perguntando ao jogador em qual linha e coluna deseja jogar
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return
                    elif event.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()
                        linha = int(pos[1]/200)
                        coluna = int(pos[0]/200)
                        jogou = True
            
        
            #Verficando se o movimento que o player escolheu está correto
        if verficaMoviMovements(board, linha, coluna):
            fazMovement(board, linha, coluna, jogador)
            jogador = (jogador + 1)%2
        
        ganhador = VerificaWinner(board)
        redraw_window(win, board)
        pygame.display.update()
        
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
main()