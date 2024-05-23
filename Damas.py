# Jogo de Damas #
# Disciplina Programação de Computadores - Prof Leonardo Souto #
# Grupo: Natan Gabriel, Matheus Emanuel e Inara #


# Classe do Jogo para Tabuleiro, Peças e Movimentação #

class JogoDamas:    # Classe Inicial e Nome do Jogo #
    
    # CRIAÇÃO DO TABULEIRO #
    
    def __init__(self):  # __init___ utilizado para contrução do objeto que no caso seria o Tabuleiro e preenchimento com as peças #
    # a função __init__ será responsável por configurar a classe 'JogoDamas', criação do Tabueiro, preenchimento do Tabuleiro e o jogador atual. #
        self.tabuleiro = [[' ' for _ in range(8)] for _ in range(8)]    # Criar um Tabuleiro de 8x8 todo em branco #
        self.preencher_tabuleiro() # Preenchimento do Tabuleiro com as peças #
        self.jogador_atual = 'O' # Jogador inicial sempre vai ser o O para poder passar o turno #
    
    # CRIAÇÃO DAS PEÇAS #
    
    def preencher_tabuleiro(self): # Tabuleiro a ser preenchido #
        for linha in range(8): # Preencher um total de 8 LINHAS #
            for coluna in range(8): # Preencher um total de 8 COLUNAS #
                if (linha + coluna) % 2 != 0: # Função para que seja impar a soma das colunas #  
                    # % é o operador módulo que retorna o resto da divisão da soma pelo número 2 #
                    # != 0 verifica se o resto da divisão não é igual a zero #
                    if linha < 3: # Imprimir as speças em Linha/Coluna Impar #
                        self.tabuleiro[linha][coluna] = 'X' # Peças X vão sempre começar em colunas Impar #
                    elif linha > 4: # Imprimir as speças em Linha/Coluna Par #
                        self.tabuleiro[linha][coluna] = 'O' # Peças O vão sempre começar em colunas Par #
    
    # IMPRESSÃO DO TABULEIRO COM AS PEÇAS #

    def imprimir_tabuleiro(self): # Imprimir o Tabuleiro no Terminal com as casas de 0 até 7 #
        print("  0 1 2 3 4 5 6 7") # Print 0 até 7 #
        for i in range(8):  # Imprimir com um total de 8 celulas em loop de LINHA #
            print(i, end=' ') # Imprimir a nossa Variavel em LINHA de 0 até 7 com o ' ' que seria o espaço entre elas #
            for j in range(8): # Imprimir com um total de 8 celulas em loop de COLUNA #
                print(self.tabuleiro[i][j], end=' ') # Imprimir a nossa Variavel em COLUNA de 0 até 7 com o ' ' que seria o espaço entre elas #
            print() # Imprimir Tudo feito a cima #
 
 # ---------------------------------------------------------------------------------------------------------------------------------------------#
 
    # MOVIMENTAÇÃO DE PEÇAS #

    def mover_peca(self, linha_origem, coluna_origem, linha_destino, coluna_destino): # Movimento de Peças por Linhas e Colunas #
        if self.movimento_valido(linha_origem, coluna_origem, linha_destino, coluna_destino): # Verificar se o movimento da peça da posição Linha/Coluna Origem para a posição Linha/Coluna Destino é permitido #
            self.tabuleiro[linha_destino][coluna_destino] = self.tabuleiro[linha_origem][coluna_origem] # Move a peça para a posição de destino. A peça que estava na posição de origem Linha/Coluna Origem é agora colocada na posição de destino Linha/Coluna Destino #
            self.tabuleiro[linha_origem][coluna_origem] = ' ' # Definir se a posição é Vazia para receber o moviento da peça #
            if linha_destino == 0 and self.tabuleiro[linha_destino][coluna_destino] == 'O':
                self.tabuleiro[linha_destino][coluna_destino] = 'OO' # Se uma peça 'O' chegou chegar a linha 0 ele vira dama e muda pra 'OO' #
            elif linha_destino == 7 and self.tabuleiro[linha_destino][coluna_destino] == 'X':
                self.tabuleiro[linha_destino][coluna_destino] = 'XX' # Se uma peça 'X' chegou chegar a linha 7 ele vira dama e muda pra 'XX' #
            return True # Se a movimentação das peças forem válidas, o jogo volta ao inicio e passa o turno #
        else:
            return False # Se a movimentação das peças NÃO for válida, o ela não é validada e volta pra tentar de novo #
    
    # REGRAS DAS MOVIMENTAÇÕES #

    def movimento_valido(self, linha_origem, coluna_origem, linha_destino, coluna_destino): # Entender o movimento de uma peça do tabuleiro de uma posição de origem para uma posição de destino é válido #
        if linha_destino < 0 or linha_destino > 7 or coluna_destino < 0 or coluna_destino > 7: # O destino tem que ser sempre ente Colunas e Linhas 0 até 7 #
            return False # Caso não seja entre 0 e 7 ele retorna a jogada #
        if self.tabuleiro[linha_destino][coluna_destino] != ' ': # Verificar se o local de movimento está vazio #
            return False # Caso o local não esteja vazio ele retorna a jogada #
        
        # Movimentação do 'O' #
        if self.tabuleiro[linha_origem][coluna_origem] == 'O': # Entender se peça está no local de origem #  
            if linha_destino == linha_origem - 1 and (coluna_destino == coluna_origem - 1 or coluna_destino == coluna_origem + 1): # Se a peça 'O' está se movendo uma linha para CIMA e uma coluna para a esquerda ou direita #
                return True # Se sim, o movimento é válido e a função retorna True #
          
          # Movimento de Captura de Peças O # 
            if linha_destino == linha_origem - 2 and (coluna_destino == coluna_origem - 2 or coluna_destino == coluna_origem + 2): # Verifica se a peça 'O' está se movendo duas linhas para CIMA e duas colunas para a esquerda ou direita #
                if self.tabuleiro[linha_origem - 1][(coluna_origem + coluna_destino) // 2] == 'X': # Se sim, verifica se há uma peça 'X' no meio do caminho #
                    self.tabuleiro[linha_origem - 1][(coluna_origem + coluna_destino) // 2] = ' ' # Se houver um X no caminho ele é removido e o espaço fica em branco #
                    return True # O movimento é validado da captura do X #
        
        # Movimentação do 'X' #
        elif self.tabuleiro[linha_origem][coluna_origem] == 'X': # Entender se peça está no local de origem #  
            if linha_destino == linha_origem + 1 and (coluna_destino == coluna_origem - 1 or coluna_destino == coluna_origem + 1): # Se a peça 'X' está se movendo uma linha para BAIXO e uma coluna para a esquerda ou direita #
                return True # Se sim, o movimento é válido e a função retorna True #
            
            # Movimento de Captura de Peças X #
            if linha_destino == linha_origem + 2 and (coluna_destino == coluna_origem - 2 or coluna_destino == coluna_origem + 2): # Verifica se a peça 'X' está se movendo duas linhas para BAIXO e duas colunas para a esquerda ou direita #
                if self.tabuleiro[linha_origem + 1][(coluna_origem + coluna_destino) // 2] == 'O': # Se sim, verifica se há uma peça 'O' no meio do caminho #
                    self.tabuleiro[linha_origem + 1][(coluna_origem + coluna_destino) // 2] = ' ' # Se houver um O no caminho ele é removido e o espaço fica em branco #
                    return True # O movimento é validado da captura do O #
        
        # Movimentação da DAMA já feita #
        elif self.tabuleiro[linha_origem][coluna_origem] == 'OO' or self.tabuleiro[linha_origem][coluna_origem] == 'XX': # Se a peça na posição de origem é uma dama ('OO' para 'O' promovida e 'XX' para 'X' promovida) #
            if abs(linha_destino - linha_origem) == 1 and abs(coluna_destino - coluna_origem) == 1: # Verifica se a dama está se movendo uma linha e uma coluna em qualquer direção #
                return True # Se sim o movimento é válido #
            if abs(linha_destino - linha_origem) == 2 and abs(coluna_destino - coluna_origem) == 2: # Se a dama está se movendo duas linhas e duas colunas em qualquer direção #
                if self.tabuleiro[(linha_origem + linha_destino) // 2][(coluna_origem + coluna_destino) // 2] == 'X' or self.tabuleiro[(linha_origem + linha_destino) // 2][(coluna_origem + coluna_destino) // 2] == 'O': # Verifica se há uma peça adversária no meio do caminho para capturar #
                    self.tabuleiro[(linha_origem + linha_destino) // 2][(coluna_origem + coluna_destino) // 2] = ' ' # Se for capturada vai ficar em branco o espaço #
                    return True # Se o moviemnto for valido, a peça vai ser removida e ficar o espaço em branco #
        return False # Se essas condições não foram atendidas sobre DAMA, a função é cancelada #

 # ---------------------------------------------------------------------------------------------------------------------------------------------#
    
    # TROCAS DE TURNOS #
    def trocar_jogador(self): # Verificação de Jogadores para Troca de Turnos #
        if self.jogador_atual == 'O': # Se o jogador atual for 'O' #
            self.jogador_atual = 'X' # Ele é trocado para 'X' #
        else:
            self.jogador_atual = 'O' # Caso contrário, ele é trocado para 'O' #
    
    # Identificar o Vencedor # 
    def verificar_vencedor(self): # Verificar vencedor do jogo # 
        for linha in self.tabuleiro: # Verificar pecas na linha #
            if 'X' in linha: # Se houver qualquer peça 'X' na linha #
                return False # Retorna como False indicando que o jogo não acabou, pois ainda há peças X #
            if 'XX' in linha: # Se houver qualquer peça 'XX' na linha #
                return False # Retorna como False indicando que o jogo não acabou, pois ainda há peças XX #
        return True # Se não houver peças X ou XX em jogo, ele volta como True indicando que o O venceu #
    
    # Textos, Troca de Turnos e Base Dinal de Vencedor #
    def jogar(self):
        while not self.verificar_vencedor(): # Enquanto não houver um "Vencedor" o jogo continuará #
            self.imprimir_tabuleiro() # Imprimir o estado atual do tabuleiro em tele #
            print("É a vez do jogador {}.".format(self.jogador_atual)) # Será impresso o indicador de turno do jogador mediante a variante jogador_atual #
            linha_origem = int(input("Digite a LINHA da peça que você deseja mover: ")) 
            coluna_origem = int(input("Digite a COLUNA da peça que você deseja mover: "))
            linha_destino = int(input("Digite a LINHA para onde você deseja mover a peça: "))
            coluna_destino = int(input("Digite a COLUNA para onde você deseja mover a peça: "))
            if self.mover_peca(linha_origem, coluna_origem, linha_destino, coluna_destino): #  Aqui é feita uma verificação condicional para determinar se o movimento da peça é valido #
                self.trocar_jogador() # Troca do turno do Jogador # 
            else:
                print("Movimento inválido!") # Movimento invalido mediante ao 'mover peca' #
        print("O jogador {} venceu!".format(self.jogador_atual)) # Após o loop while terminar, significa que a condição de vitória foi alcançada. Então é impresso o vencedor da partida #

jogo = JogoDamas() # Basicamente você está criando um objeto chamado jogo que é uma instância da classe JogoDamas # 
# Quando você faz isso o método __init__ da classe JogoDamas é inicializado #
jogo.jogar() # Inicia o jogo de damas controlando o fluxo principal do jogo #
# As linhas de código inicializam o jogo de damas e começam a execução do loop principal do jogo, até que um vença #