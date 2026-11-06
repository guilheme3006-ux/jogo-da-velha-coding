
Jogo da Velha em Python
Projeto avaliativo da disciplina de Coding — 2ª Avaliação
Curso: Bacharelado em Ciência da Computação
Instituição: UNINASSAU — Teresina (PI)
Ano: 2026

Sobre o projeto
Este projeto consiste no desenvolvimento de um Jogo da Velha para dois jogadores, executado diretamente no terminal e implementado em Python 3. Seu objetivo é aplicar, na prática, conteúdos de lógica de programação, como variáveis, operadores, estruturas de decisão, laços de repetição e matrizes bidimensionais.

O programa foi organizado de maneira procedural, com blocos de código controlados por estruturas como if, elif, else, while e for, sem depender de bibliotecas externas.

Funcionalidades
Partida local entre dois jogadores, identificados por X e O.
Tabuleiro de 3 linhas por 3 colunas, representado por uma matriz.
Menu interativo para jogar, consultar regras, visualizar placar, acessar estatísticas e sair.
Alternância automática de turnos, começando pelo jogador X.
Leitura das coordenadas de linha e coluna, de 0 a 2.
Validação de entradas inválidas, incluindo letras, campos vazios e números fora do intervalo.
Bloqueio de jogadas em casas já ocupadas.
Verificação de vitória nas linhas, colunas e diagonais.
Identificação automática de empate quando o tabuleiro está completo e não há vencedor.
Placar acumulado de vitórias de X, vitórias de O e empates durante a execução.
Reinício do tabuleiro a cada nova partida, sem apagar o placar da sessão.
Estatísticas da sessão com percentuais e indicação do jogador com mais vitórias.
Regras do jogo
O jogo é disputado por dois jogadores: X e O.
O jogador X inicia a partida.
A cada rodada, o jogador escolhe uma linha e uma coluna, ambas de 0 a 2.
Só é possível marcar uma casa que esteja vazia.
Vence quem alinhar três símbolos iguais na horizontal, vertical ou diagonal.
Se todas as casas forem preenchidas sem uma combinação vencedora, a partida termina em empate.
Após o término, é possível iniciar outra partida pelo menu, mantendo o placar da sessão.
Exemplo de tabuleiro
    0   1   2
0   X | O | X
   ---|---|---
1   O | X | O
   ---|---|---
2     |   | X
Neste exemplo, X venceu pela diagonal principal.

Requisitos
Python 3 instalado no computador.
Um terminal ou prompt de comando (Windows, Linux ou macOS).
Nenhuma biblioteca externa é necessária.
Para conferir a instalação do Python, execute:

python --version
Em alguns sistemas, o comando é python3 --version.

Como instalar e executar
1. Baixe o projeto pelo botão Code > Download ZIP do GitHub ou clone o repositório:

git clone https://github.com/guilheme3006-ux/jogo-da-velha-coding.git
2. Acesse a pasta do projeto:

cd jogo-da-velha-coding
3. Execute o arquivo principal:

python jogo_da_velha.py
Se necessário, utilize python3 jogo_da_velha.py.

Como usar o menu
Ao iniciar, o programa exibe as opções:

==============================
        JOGO DA VELHA
==============================
1. Jogar
2. Ver Regras
3. Ver Placar e Estatísticas
4. Desafio: Estatísticas da Sessão
5. Sair
Opção	Ação
1	Inicia uma nova partida, limpando o tabuleiro.
2	Exibe as regras do Jogo da Velha.
3	Mostra o placar acumulado de X, O e empates.
4	Mostra o total de partidas, os percentuais de resultados e o líder da sessão.
5	Encerra o programa.
Durante uma partida: informe as coordenadas solicitadas. Na pergunta da linha, digitar 9 permite interromper a partida em andamento e voltar ao menu. Essa opção não se aplica ao campo da coluna.

Organização do código
O projeto está implementado no arquivo jogo_da_velha.py. As principais partes do programa são:

Bloco	Conteúdo aplicado	Responsabilidade
Inicialização	Variáveis e matriz (lista de listas)	Criar o tabuleiro vazio e iniciar os contadores do placar.
Menu principal	while, if e elif	Apresentar as opções e manter o programa ativo até a saída.
Partida e validação	while, for e condições	Ler coordenadas válidas e impedir a sobrescrita de casas.
Exibição do tabuleiro	Matriz e for aninhados	Percorrer e apresentar as nove posições do jogo.
Fim da partida	for, condições e operadores	Verificar vitórias nas linhas, colunas e diagonais e detectar empates.
Reinício	for aninhados	Limpar a matriz ao iniciar outra partida.
Estatísticas	Variáveis e operadores aritméticos	Calcular resultados acumulados e percentuais da sessão.
Representação do tabuleiro
O tabuleiro é uma matriz 3 × 3, criada como uma lista contendo três listas:

tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
Cada posição é acessada pelo formato tabuleiro[linha][coluna]. Os valores podem ser "X", "O" ou um espaço em branco (" ").

Desafio de lógica: estatísticas da sessão
O desafio implementado registra o número de vitórias de cada jogador e os empates. A partir desses contadores, o programa calcula o total de partidas e a porcentagem de cada resultado:

total_partidas = placar_x + placar_o + empates

if total_partidas > 0:
    porc_x = (placar_x / total_partidas) * 100
    porc_o = (placar_o / total_partidas) * 100
    porc_empate = (empates / total_partidas) * 100
O menu também informa qual jogador lidera o placar ou se ambos estão empatados. As estatísticas são mantidas enquanto o programa estiver aberto; elas não são gravadas em arquivo.

Cenários de teste
Para verificar o funcionamento do projeto, podem ser executados os seguintes cenários:

Cenário	Comportamento esperado
Vitória de X ou O	Identificar o vencedor e atualizar seu placar.
Partida empatada	Informar o empate e atualizar o contador correspondente.
Letra em vez de coordenada	Recusar a entrada e solicitar um valor válido.
Campo vazio	Recusar a entrada e solicitar um valor válido.
Coordenada fora de 0 a 2	Informar que a entrada é inválida.
Casa já ocupada	Impedir a jogada e manter o turno.
Opção inexistente no menu	Exibir aviso e solicitar outra opção.
Nova partida	Limpar o tabuleiro e preservar o placar acumulado.
Opção 9 na escolha da linha	Voltar ao menu principal.
Opção 5 no menu	Encerrar o programa.
Estrutura do repositório
jogo-da-velha-coding/
├── jogo_da_velha.py   # Código-fonte principal
└── README.md          # Documentação do projeto
Integrantes e divisão de tarefas
O projeto foi desenvolvido por dois integrantes do curso de Bacharelado em Ciência da Computação da UNINASSAU:

Integrante	Responsabilidades descritas no relatório
Nicolas Sá Soares	Lógica de matrizes, placar acumulado e limpeza do tabuleiro.
Guilherme Rodrigues Silva Galvão	Estruturação inicial do programa, laços de repetição e estatísticas avançadas.
O histórico de alterações e contribuições pode ser consultado na aba Commits do repositório.

Objetivo acadêmico
Este projeto integra a 2ª Avaliação da disciplina de Coding e demonstra a utilização conjunta de:

Tipos de dados e variáveis;
Operadores aritméticos, relacionais e lógicos;
Estruturas condicionais;
Estruturas de repetição;
Matrizes bidimensionais e laços for aninhados;
Validação de entradas e resolução de problemas de lógica.
UNINASSAU — Ciência da Computação | Teresina (PI), 2026
Autores: Nicolas Sá Soares e Guilherme Rodrigues Silva Galvão.

