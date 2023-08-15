
branco = ' '
token = ('X','O')


def criaBoard():
    board = [
        [branco, branco, branco],
        [branco, branco, branco],
        [branco, branco, branco]
    ]
    return board


def printBoard(board):

    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
         print('---------')


def getIputValido(mensagem):
    try:
        n = int(input(mensagem))
        if n > 3 or n < 1:
            print('O numero deve estar entre 1 e 3.')
            return getIputValido(mensagem)
        else:
            return n -1 
    except (ValueError, TypeError):
        print('Digite apenas numeros')
        return getIputValido(mensagem)


def verficaMoviMovements(board, linha, coluna):
    if board[linha][coluna]==branco:
        return True
    return False


def fazMovement(board, linha, coluna, jogador):
    board[linha][coluna] = token[jogador]


def VerificaWinner(board):
    #verifica linha
    for i in range(3):
        if board[i][0]!= branco and board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            return  board[i][i]
    #verfica colunas
    for i in range(3):
            if board[0][i]!=branco and board[0][i] == board[1][i] and board[1][i] == board[2][i]:
                return board[i][i]
    #verifica diagonais
    #diagonal pricipal
    if board[0][0]!= branco and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    #Diagonal 2
    elif board[0][2]!= branco and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return  board[0][2]
    for c in range(3):
        for j in range(3):
            if board [c][j] == branco:
                return False
    return 'EMPATE'

def modo_de_jogo (string):

    try:
        print('1) JOGAR 1v1 \n2) JOGAR CONTRA A MÁQUINA')
        modo_jogo = int(input(string))
        if modo_jogo > 2:
            return modo_de_jogo(string)
        
        return modo_jogo

    except(ValueError, TypeError):
        print('Digite apenas números.')
        return modo_de_jogo(string)
    

                                  
