from jogo_da_velha import modo_de_jogo, modo_contra_maquina, modo_um_contra_um

# Escolhendo o modo de jogo
print('ESCOLHA O MODO DE JOGO')
opc_modo_jogo = modo_de_jogo('Sua opção: ')

# Chamando a função de cada modo de jogo
if opc_modo_jogo == 1:
    modo_um_contra_um()
else:
    modo_contra_maquina()
