# Jogo da Velha em Python

**Projeto da 2ª Avaliação — Disciplina de Coding**  
**Curso:** Bacharelado em Ciência da Computação  
**Instituição:** UNINASSAU — Teresina (PI)  
**Ano:** 2026

## Sobre o projeto

Este projeto apresenta um **Jogo da Velha para dois jogadores**, desenvolvido em **Python 3** e executado no terminal. O objetivo é aplicar conceitos estudados na disciplina de Coding, como variáveis, operadores, estruturas condicionais, laços de repetição e matrizes.

O código segue uma abordagem procedural, sem bibliotecas externas.

## Funcionalidades

- Partida local entre os jogadores **X** e **O**.
- Tabuleiro **3 × 3**, representado por uma matriz.
- Alternância automática dos turnos, começando pelo jogador **X**.
- Validação de coordenadas e bloqueio de casas já ocupadas.
- Verificação de vitória por linha, coluna ou diagonal.
- Identificação de empate ao fim da partida.
- Placar acumulado durante a sessão.
- Nova partida com o tabuleiro limpo e o placar preservado.
- Estatísticas com percentuais de vitórias e empates.

## Como executar

### 1. Requisitos

- **Python 3** instalado no computador.
- Terminal ou prompt de comando (Windows, Linux ou macOS).
- Nenhuma biblioteca externa é necessária.

Confira se o Python está instalado:

```bash
python --version
```

Em alguns sistemas, utilize `python3 --version`.

### 2. Baixar o projeto

É possível baixar o ZIP pelo botão **Code → Download ZIP** na página do repositório ou cloná-lo com Git:

```bash
git clone https://github.com/guilheme3006-ux/jogo-da-velha-coding.git
```

### 3. Abrir a pasta e iniciar o jogo

```bash
cd jogo-da-velha-coding
python jogo_da_velha.py
```

Se o comando `python` não funcionar, tente:

```bash
python3 jogo_da_velha.py
```

## Menu principal

Ao iniciar, o programa apresenta cinco opções:

```text
==============================
         JOGO DA VELHA
==============================
1. Jogar
2. Ver Regras
3. Ver Placar e Estatísticas
4. Desafio: Estatísticas da Sessão
5. Sair
```

**O que faz cada opção:**

1. **Jogar:** inicia uma partida com o tabuleiro vazio.
2. **Ver Regras:** explica as regras do jogo.
3. **Ver Placar e Estatísticas:** exibe as vitórias de X, de O e os empates.
4. **Estatísticas da Sessão:** apresenta o total de partidas, os percentuais de resultados e o líder da sessão.
5. **Sair:** encerra o programa.

> **Importante:** durante a partida, as coordenadas de linha e coluna vão de `0` a `2`. Na solicitação da **linha**, é possível digitar `9` para interromper a partida e voltar ao menu.

## Regras do jogo

1. O jogador **X** começa; depois, os participantes alternam os turnos.
2. Em cada turno, é escolhida uma linha e uma coluna, de `0` a `2`.
3. Não é permitido marcar uma posição já ocupada.
4. Ganha quem formar uma linha, coluna ou diagonal com três símbolos iguais.
5. Caso todas as casas sejam preenchidas sem vencedor, ocorre empate.

### Exemplo de tabuleiro

```text
    0   1   2
0   X | O | X
   ---+---+---
1   O | X | O
   ---+---+---
2     |   | X
```

No exemplo, **X vence pela diagonal principal**.

## Organização do código

O projeto é composto pelo arquivo principal `jogo_da_velha.py` e por este `README.md`.

O programa trabalha com estes blocos:

- **Inicialização:** cria a matriz 3 × 3 e os contadores do placar.
- **Menu principal (`while`):** exibe as opções até a escolha de sair.
- **Validação de entradas:** aceita apenas coordenadas válidas e impede jogadas em casas ocupadas.
- **Exibição do tabuleiro (`for` aninhados):** percorre linhas e colunas da matriz.
- **Verificação do resultado:** identifica vitórias e empates.
- **Reinício da partida:** limpa a matriz sem zerar o placar.
- **Estatísticas da sessão:** calcula os percentuais dos resultados.

### Matriz do tabuleiro

O tabuleiro é armazenado como uma lista com três listas, uma para cada linha:

```python
tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
```

Cada posição pode conter `"X"`, `"O"` ou `" "` (espaço vazio) e é acessada por `tabuleiro[linha][coluna]`.

## Desafio de lógica: estatísticas da sessão

O jogo registra quantas partidas terminaram com vitória de **X**, vitória de **O** ou empate. A partir desses valores, calcula as porcentagens correspondentes:

```python
total_partidas = placar_x + placar_o + empates

if total_partidas > 0:
    porc_x = (placar_x / total_partidas) * 100
    porc_o = (placar_o / total_partidas) * 100
    porc_empate = (empates / total_partidas) * 100
```

O programa também indica quem possui mais vitórias na sessão ou se o placar está empatado.

> O placar permanece disponível enquanto o programa estiver aberto. **Os dados não são salvos em arquivo** após o encerramento.

## Cenários de teste

Estes são os principais cenários para conferir o funcionamento:

- **Vitória:** completar três símbolos iguais em uma linha, coluna ou diagonal.
- **Empate:** preencher o tabuleiro sem formar uma sequência vencedora.
- **Letra ou campo vazio:** verificar se a entrada inválida é recusada.
- **Número fora do intervalo:** testar coordenadas diferentes de `0`, `1` e `2`.
- **Casa ocupada:** tentar jogar duas vezes na mesma posição.
- **Opção de menu inválida:** digitar uma opção fora de `1` a `5`.
- **Nova partida:** verificar a limpeza do tabuleiro e a preservação do placar.
- **Retorno ao menu:** digitar `9` quando o programa solicitar a linha.

## Estrutura do repositório

```text
jogo-da-velha-coding/
├── jogo_da_velha.py    # Código do jogo
└── README.md           # Documentação
```

## Integrantes

**Nicolas Sá Soares**  
Lógica de matrizes, placar acumulado e limpeza do tabuleiro.

**Guilherme Rodrigues Silva Galvão**  
Estruturação inicial, laços de repetição e estatísticas da sessão.

As contribuições registradas podem ser consultadas no histórico de commits do repositório.

---

**UNINASSAU — Bacharelado em Ciência da Computação**  
**Disciplina:** Coding · **2ª Avaliação** · **Teresina (PI), 2026**
