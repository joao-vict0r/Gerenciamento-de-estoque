import os
from criacao_estoque import gerar_id as ID
from criacao_estoque import estoque_dados as AD

# Função para limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


menu = True

while menu:
    limpar_tela()
    print('Bem-vindo ao sistema de gerenciamento de estoque')
    opcao = input(
        'Informe qual opção deseja fazer\n'
        '1 - Cadastrar item\n'
        '2 - Fazer saída de item\n'
        '3 - Fazer entrada de item\n'
        '4 - Buscar produto por nome\n'
        '5 - Ver todos os itens cadastrados\n'
        '6 - Sair do sistema\n'
        'Escolha: '
    )

    try:
        opcao = int(opcao)
    except ValueError:
        print('Opção inválida! Por favor, digite um número entre 1 e 6.')
        input('Pressione Enter para continuar...')
        continue

    if opcao == 1:
        limpar_tela()
        print('Cadastro de item para o seu estoque')
        id_item = ID.gerar_id()
        nome = input('Nome do item: ')
        descricao_item = input('Descrição: ')
        try:
            total_item = int(input('Total entrando: '))
        except ValueError:
            print('Total inválido! Por favor, digite um número inteiro.')
            input('Pressione Enter para continuar...')
            continue

        AD.estoque_inset(id_item, nome, descricao_item, total_item)
        print(f'Item: {nome} cadastrado com sucesso com ID:  {id_item}')
        input('Pressione Enter para continuar...')

    elif opcao == 2:
        limpar_tela()
        print('Fazer saída de item')
        
        id_item = input('Informe o ID do item para saída: ')
        quantidade = int(input('Quantidade saindo: '))
        AD.estoque_saida(id_item, quantidade)
           

    elif opcao == 3:
        limpar_tela()
        print('Fazer entrada de item')
        try:
            id_item = input('Informe o ID do item para entrada: ')
            quantidade = int(input('Quantidade entrando: '))
            AD.estoque_entrada(id_item, quantidade)
            print(f'{quantidade} unidades do item {id_item} entraram no estoque.')
        except ValueError:
            print('Quantidade inválida! Por favor, digite um número inteiro.')
        except KeyError:
            print('ID do item não encontrado!')
        input('Pressione Enter para continuar...')

    elif opcao == 4:
            limpar_tela()
            print('Buscar produto por nome')
            nome_produto = input('Digite o nome do produto a ser encontrado: ')
            produto = AD.achar_produto(nome_produto)
           

    elif opcao == 5:
        limpar_tela()
        AD.listar_itens()


    elif opcao == 6:
        print('Saindo do sistema...')
        menu = False
        limpar_tela()

    else:
        print('Opção inválida! Por favor, digite um número entre 1 e 6.')
        input('Pressione Enter para continuar...')
