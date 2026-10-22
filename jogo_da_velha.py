# Trabalho de Coding - Jogo da Velha
# Integrantes: Nome 1, Nome 2 e Nome 3

tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

print("JOGO DA VELHA")
print("Tabuleiro inicial:")
print("  1 2 3")

for i in range(3):
    print(i + 1, end=" ")
    for j in range(3):
        print(tabuleiro[i][j], end=" ")
    print()
