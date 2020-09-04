"""
O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências.

Faça um programa que implemente uma caixa registradora rudimentar.

O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias.

Um valor zero deve ser informado pelo operador para indicar o final da compra.

O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu,
para então calcular e mostrar o valor do troco.

Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra.

A saída deve ser conforme o exemplo abaixo:

    Lojas Tabajara
    Produto 1: R$ 2.20
    Produto 2: R$ 5.80
    Produto 3: R$ 0
    Total: R$ 9.00
    Dinheiro: R$ 20.00
    Troco: R$ 11.00
    ...
"""
cabecalho_recibo = """Lojas Tabajara """
recebido_recibo = """Total:        R$  {0}
Dinheiro:     R$ {1}
Troco:        R$ {2} """
texto_produto = 'qual o valor do produto {0}: '

texto_produto_1 = 'produto {0}'

comecar_venda = 's'
mais_produtos = ''

while comecar_venda == 's':
    comecar_venda = str(input('Começar nova venda? s - sim: '))
    x = 0
    total = []
    venda = {}
    while not mais_produtos == 's':
        x += 1
        preco_produto = float(input(texto_produto.format(x)))
        venda[texto_produto_1.format(x)] = preco_produto

        if preco_produto == 0:
            break
    for total_1 in venda.values():
        total.append(total_1)
    print()
    print('Subtotal', '% .2f' % (sum(total)))
    print()
    pagamento = float(input('qual valor em dinheiro: '))
    print()
    troco = pagamento - sum(total)
    print(cabecalho_recibo)
    for produto, valor in venda.items():
        print(produto, '    R$ ', '% .2f' % valor)
    print(recebido_recibo.format('% .2f' % (sum(total)), '% .2f' % pagamento, '% .2f' % troco))
    print()
