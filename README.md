﻿# Gerenciador de Pedidos para Lanchonete

Este é projeto acadêmico, para implementa um sistema simples de gerenciamento de pedidos para uma lanchonete. Utilizando a linguagem Python, o sistema permite adicionar, atender, listar e pesquisar pedidos, além de gerenciar uma fila com capacidade máxima.

## Funcionalidades

1. **Incluir Pedido:** Adiciona um pedido à fila, desde que a fila não esteja cheia.
2. **Atender Pedido:** Remove o primeiro pedido da fila e o marca como atendido.
3. **Listar Pedidos:** Exibe todos os pedidos na fila.
4. **Pesquisar Pedido:** Verifica se um pedido específico está na fila.
5. **Encerrar Programa:** Finaliza o programa, desde que não existam pedidos pendentes na fila.

## Estrutura do Código

O programa é composto por funções principais que realizam cada operação:

### 1. `incluirPedido(pedido)`
Adiciona um novo pedido à fila, respeitando o limite máximo de 10 pedidos.

- **Parâmetros:**
  - `pedido`: Número do pedido a ser adicionado.
- **Regras:**
  - Exibe uma mensagem se a fila estiver cheia.

### 2. `atenderPedido()`
Atende o pedido mais antigo da fila.

- Remove o primeiro pedido da lista (posição 0).
- Exibe uma mensagem se a fila estiver vazia.

### 3. `listarPedidos()`
Lista todos os pedidos na fila.

- Exibe uma mensagem caso não existam pedidos.

### 4. `pesquisarPedido(pedido)`
Pesquisa a existência de um pedido específico na fila.

- **Parâmetros:**
  - `pedido`: Número do pedido a ser pesquisado.
- Exibe uma mensagem indicando se o pedido está ou não na fila.

### 5. `menu()`
Exibe o menu principal com as opções disponíveis para o usuário.

### 6. `main()`
Executa o programa principal, exibindo o menu e processando as escolhas do usuário.

- Realiza o controle do fluxo baseado nas opções selecionadas.
- Permite encerrar o programa apenas quando não existirem pedidos pendentes.

## Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Salve o código em um arquivo chamado `lanchonete.py`.
3. No terminal, execute o comando:

   ```bash
   python lanchonete.py
   ```
4. Siga as instruções no menu para gerenciar os pedidos.

## Exemplo de Uso

1. Escolha a opção 1 para incluir um pedido.
2. Escolha a opção 2 para atender o pedido mais antigo.
3. Escolha a opção 3 para listar os pedidos na fila.
4. Escolha a opção 4 para verificar se um pedido está na fila.
5. Escolha a opção 5 para encerrar o programa (apenas se não existirem pedidos pendentes).

## Regras de Negócio

- A fila tem um limite máximo de **10 pedidos**.
- O programa não será encerrado enquanto houver pedidos pendentes.
- Apenas números inteiros podem ser utilizados como identificadores de pedidos.

## Melhorias Futuras

- Implementar interface gráfica para o gerenciamento de pedidos.
- Adicionar persistência de dados utilizando banco de dados ou arquivos.
- Expandir o limite máximo de pedidos na fila.

## Licença

Este projeto é de uso livre para fins educativos ou pessoais.
