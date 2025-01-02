import mercadopago

public_key = "APP_USR-eec39469-c75d-471d-be3d-a5ee1c58c37e"
token = "APP_USR-3104191355613675-121709-faed7d099e1633614baec7c3eeaf55aa-2161819691"


def criar_pagamento(itens_pedido, link):
    # Configure as credenciais
    sdk = mercadopago.SDK(token)
    # Crie um item na preferência

    # itens que ele está comprando no formato de dicionário
    itens = []
    for item in itens_pedido:
        quantidade = int(item.quantidade)
        nome_produto = item.item_estoque.produto.nome
        preco_unitario = float(item.item_estoque.produto.preco)
        itens.append({
            "title": nome_produto,
            "quantity": quantidade,
            "unit_price": preco_unitario,
        })

    # valor total
    preference_data = {
        "items": itens,
        "auto_return": "all",
        "back_urls": {
            "success": link,
            "pending": link,
            "failure": link,
        }
    }
    resposta = sdk.preference().create(preference_data)
    link_pagamento = resposta["response"]["init_point"]
    id_pagamento = resposta["response"]["id"]
    return link_pagamento, id_pagamento