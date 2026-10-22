# Trabalho de Coding - Jogo da Velha
# Integrantes: Nicolas Sá Soares, [Colega 2] e [Colega 3]

tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

opcao = ""

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
                
    elif opcao == "2":
        print("\n--- REGRAS DO JOGO ---")
        print("Dois jogadores (X e O) se alternam marcando")
        print("uma casa vazia por rodada. Vence quem completar")
        print("primeiro uma linha, coluna ou diagonal com o seu símbolo.")
        
    elif opcao == "3":
        print("\n--- PLACAR ACUMULADO ---")
        print("Jogador X: 0 | Jogador O: 0 | Empates: 0")
        
    elif opcao == "4":
        print("\nEncerrando o programa. Até mais!")
        
    else:
        print("\n[Erro] Opção inválida! Escolha um número de 1 a 4.")
