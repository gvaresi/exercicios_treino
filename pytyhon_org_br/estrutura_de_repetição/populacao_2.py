"""
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
Valide a entrada e permita repetir a operação.
"""

resultado = """
                ano         {0}
                pais_a      {1}
                pais_b      {2}
                """

escolha = 's'
while escolha == 's':
    pais_a = int(input('digite a populacao do Pais A: '))
    pais_b = int(input('digite a populacao do Pais B: '))

    tx_cresc_pais_a = float(input('informe a taxa de cresciemnto do pais A em %: '))
    tx_a = (tx_cresc_pais_a / 100) + 1
    tx_cresc_pais_b = float(input('informe a taxa de cresciemnto do pais B em %: '))
    tx_b = (tx_cresc_pais_b / 100) + 1

    ano = 0

    while pais_a <= pais_b:
        pais_a *= tx_a
        pais_b *= tx_b
        ano += 1

    print(resultado.format(ano, pais_a, pais_b))
