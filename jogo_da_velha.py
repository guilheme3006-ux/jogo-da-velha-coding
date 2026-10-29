# Trabalho de Coding - Jogo da Velha
# Integrantes: Nicolas Sá Soares e Guilherme

tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

opcao = ""

# Placar acumulado global (mantém-se entre as partidas, exigência do Dia 30)
placar_x = 0
placar_o = 0
empates = 0

# Menu principal controlado por while (Exigência do professor)
while opcao != "4":
    print("\n==============================")
    print("       JOGO DA VELHA          ")
    print("==============================")
    print("1. Jogar")
    print("2. Ver Regras")
    print("3. Ver Placar")
    print("4. Sair")
    
    opcao = input("Escolha uma opção (1 a 4): ")
    
    if opcao == "1":
        print("\n--- Iniciando a partida ---")
        
        # Limpar / resetar o tabuleiro usando for aninhado (Exigência do Dia 30)
        for i in range(3):
            for j in range(3):
                tabuleiro[i][j] = " "
        
        vez = "X"
        partida_em_andamento = True
        
        while partida_em_andamento:
            print(f"\nVez do jogador: {vez}")
            print("Tabuleiro atual:")
            print("     0    1    2 ")
            
            # Exibição da matriz com for aninhado
            for i in range(3):
                linha_formatada = ""
                for j in range(3):
                    linha_formatada += f" {tabuleiro[i][j]} "
                    if j < 2:
                        linha_formatada += "|"
                print(f"  {i}  {linha_formatada}")
                if i < 2:
                    print("     ---|---|---")
                    
            # --- VALIDAÇÃO DA LINHA ---
            valida_linha = False
            linha = 0
            while valida_linha == False:
                entrada_linha = input("Escolha a LINHA (0 a 2) ou digite '9' para voltar ao menu: ")
                if entrada_linha == "9":
                    partida_em_andamento = False
                    break
                for n in range(3):
                    if entrada_linha == str(n):
                        valida_linha = True
                        linha = n
                if valida_linha == False and partida_em_andamento:
                    print("Entrada inválida! Digite um número de 0 a 2 para a linha.")

            if not partida_em_andamento:
                break

            # --- VALIDAÇÃO DA COLUNA ---
            valida_coluna = False
            coluna = 0
            while valida_coluna == False:
                entrada_coluna = input("Escolha a COLUNA (0 a 2): ")
                for n in range(3):
                    if entrada_coluna == str(n):
                        valida_coluna = True
                        coluna = n
                if valida_coluna == False:
                    print("Entrada inválida! Digite um número de 0 a 2 para a coluna.")

            # --- CHETAGEM DE CASA OCUPADA E ATUALIZAÇÃO ---
            if tabuleiro[linha][coluna] == " ":
                tabuleiro[linha][coluna] = vez
                
                # --- 1. VERIFICAÇÃO DE VITÓRIA POR LAÇOS ---
                venceu = False

                for i in range(3):
                    if tabuleiro[i][0] == vez and tabuleiro[i][1] == vez and tabuleiro[i][2] == vez:
                        venceu = True

                for j in range(3):
                    if tabuleiro[0][j] == vez and tabuleiro[1][j] == vez and tabuleiro[2][j] == vez:
                        venceu = True

                if tabuleiro[0][0] == vez and tabuleiro[1][1] == vez and tabuleiro[2][2] == vez:
                    venceu = True
                if tabuleiro[0][2] == vez and tabuleiro[1][1] == vez and tabuleiro[2][0] == vez:
                    venceu = True

                if venceu:
                    print("\nTabuleiro final:")
                    print("     0    1    2 ")
                    for i in range(3):
                        linha_formatada = ""
                        for j in range(3):
                            linha_formatada += f" {tabuleiro[i][j]} "
                            if j < 2:
                                linha_formatada += "|"
                        print(f"  {i}  {linha_formatada}")
                        if i < 2:
                            print("     ---|---|---")

                    print(f"\n🎉 PARABÉNS! O jogador {vez} VENCEU A PARTIDA!")
                    
                    # Atualiza o placar acumulado sem zerar os pontos anteriores
                    if vez == "X":
                        placar_x += 1
                    else:
                        placar_o += 1
                        
                    partida_em_andamento = False
                    break
                
                # --- 2. VERIFICAÇÃO DE EMPATE POR FOR ANINHADO ---
                vazias = 0
                for i in range(3):
                    for j in range(3):
                        if tabuleiro[i][j] == " ":
                            vazias += 1
                            
                if vazias == 0 and not venceu:
                    print("\nTabuleiro final:")
                    print("     0    1    2 ")
                    for i in range(3):
                        linha_formatada = ""
                        for j in range(3):
                            linha_formatada += f" {tabuleiro[i][j]} "
                            if j < 2:
                                linha_formatada += "|"
                        print(f"  {i}  {linha_formatada}")
                        if i < 2:
                            print("     ---|---|---")

                    print("\n🤝 FIM DE JOGO! Deu empate!")
                    empates += 1
                    partida_em_andamento = False
                    break

                # Alternar a vez
                if vez == "X":
                    vez = "O"
                else:
                    vez = "X"
            else:
                print("Atenção: Esta casa já está ocupada! Escolha outra.")
                
    elif opcao == "2":
        print("\n--- REGRAS DO JOGO ---")
        print("Dois jogadores (X e O) alternam-se marcando")
        print("uma casa vazia por rodada. Vence quem completar")
        print("primeiro uma linha, coluna ou diagonal com o seu símbolo.")
        
    elif opcao == "3":
        print("\n--- PLACAR ACUMULADO ---")
        print(f"Jogador X: {placar_x} | Jogador O: {placar_o} | Empates: {empates}")
        
    elif opcao == "4":
        print("\nA encerrar o programa. Até breve!")
        
    else:
        print("\n[Erro] Opção inválida! Escolha um número de 1 a 4.")
