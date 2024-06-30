estoque_dados = []

def estoque_inset(id, nome, desc_item, qnt_estq):
    item_cadastrado = False
    for item in estoque_dados:
        if item[0] == id:
            item_cadastrado = True
            break
    if item_cadastrado:
        print("Item já cadastrado, ação não permitida.")
    else:
        estoque_dados.append([id, nome, desc_item, qnt_estq])
        print('Cadastro realizado.')


# gerencia quantidade
def estoque_saida(id_item, quantidade):
    item_encontrado = False
    for item in estoque_dados:
        if item[0] == id_item:
            item_encontrado = True
            if item[3] >= quantidade:
                item[3] -= quantidade
                print(f'{quantidade} unidades do item {id_item} saíram do estoque.')
            else:
                print(f'Quantidade insuficiente para saída de {quantidade} unidades do item {id_item}.')
            break
    if not item_encontrado:
        print('ID do item não encontrado.')


def estoque_entrada(id_item, quantidade):
    item_encontrado = False
    for item in estoque_dados:
        if item[0] == id_item:
            item_encontrado = True
            item[3] += quantidade  # Adiciona a quantidade ao estoque
            break
    if not item_encontrado:
        print('ID do item não encontrado.')
    input('Pressione Enter para continuar...')




# parte de achar produtos
def achar_produto(nome_produto):
    for item in estoque_dados:
        print(f"Item atual: {item}")
        if item[1].lower() == nome_produto.lower():
            print(f"Produto encontrado: {item}")
            return item
    print("Produto não encontrado.")
    return None

def listar_itens():
    print("Lista de Itens no Estoque:")
    for item in estoque_dados:
        id_item = item[0]
        nome = item[1]
        qnt_estq = item[3] 
        print(f"ID: {id_item}, Nome: {nome}, Quantidade: {qnt_estq}")

