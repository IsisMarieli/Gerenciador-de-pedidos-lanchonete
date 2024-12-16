numPedido = [] # lista vazia de numero de pedidos

def incluirPedido(pedido): # função de inclusão de pedido
    if len(numPedido) >= 10: # se a quantidade de numPedido for maior ou igual de 10 imprima...
        print("Fila Cheia - Não pode mais incluir pedidos")
    else: # senão adicione pedido
        numPedido.append(pedido)
        print(f"Pedido {pedido} incluído com sucesso!")

def atenderPedido(): # função para atender o pedido 
    if not numPedido: # se não tiver pedido imprima
        print("Lista vazia - Não existem pedidos")
    else:
        pedidoAtendido = numPedido.pop(0) # aqui esse .pop(0) vai remover o primeiro pedido que tiver na lista numPedido quando for atendido, ou seja o pedido que tiver na posição 0
        print(f"Pedido {pedidoAtendido} atendido com sucesso!")

def listarPedidos(): # função para listar os pedidos
    if not numPedido:
        print("Lista vazia - Não existem pedidos")
    else:
        print("Pedidos na fila:")
        for pedido in numPedido:
            print(f"Pedido {pedido}")

def pesquisarPedido(pedido): # função para pesquisar o status do pedido
    if pedido in numPedido: # se pedido estiver em numPedido imprima
        print(f"Pedido {pedido} está na fila")
    else: # senão...
        print(f"Pedido {pedido} não encontrado")

def menu(): # aqui é o menu das opções
    print("------ LANCHONETE ------")
    print("# 1 - INCLUIR PEDIDO   #")
    print("# 2 - ATENDER PEDIDO   #")
    print("# 3 - LISTAR PEDIDOS   #")
    print("# 4 - PESQUISAR PEDIDO #")
    print("# 5 - ENCERRAR         #")
    print("------------------------")

def main(): # a função principal para escolher as opções do menu
    while True: # estrutura de loop
        menu() 
        opcao = int(input("Escolha a operação: ")) # nessas opções abaixo vão verificar se as opções for igual aos numero do menu e imprimir a mensagem que corresponde a opção 
        if opcao == 1: 
            pedido = int(input("Digite o número do pedido: "))
            incluirPedido(pedido)
        elif opcao == 2:
            atenderPedido()
        elif opcao == 3:
            listarPedidos()
        elif opcao == 4:
            pedido = int(input("Digite o número do pedido: "))
            pesquisarPedido(pedido)
        elif opcao == 5:
            if not numPedido: # negando que tem pedido e encerrar programa, so pra quando não tiver mais pedidos e fechar a lanchonete :)
                print("Encerrando o programa...")
                break
            else:
                print("Ainda existem pedidos na fila! Não é possível encerrar.")
        else:
            print("Opção inválida! Tente novamente.")

main()
