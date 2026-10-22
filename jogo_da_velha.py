# Trabalho de Coding - Jogo da Velha
# Integrantes: Nome 1, Nome 2 e Nome 3

tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

print("=== JOGO DA VELHA ===")
print("     0    1    2 ") # Índices das colunas visíveis para o jogador

# Exibição da matriz utilizando for aninhado (exigência do professor)
for i in range(3):
    linha_formatada = ""
    for j in range(3):
        linha_formatada += f" {tabuleiro[i][j]} "
        if j < 2:
            linha_formatada += "|"
            
    print(f"  {i}  {linha_formatada}") # Exibe o número da linha e o conteúdo
    
    if i < 2:
        print("     ---|---|---")
