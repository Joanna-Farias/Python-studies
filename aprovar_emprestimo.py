valor_da_casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o seu salário: "))
anos = int(input("Digite em quantos anos você deseja pagar: "))


def aprovar_emprestimo(valor_da_casa, salario, anos):
    """
    Função para aprovar ou negar um empréstimo com base no valor da casa, salário e prazo de pagamento.

    Parâmetros: valor_da_casa (float): O valor total da casa.
                salario (float): O salário do solicitante.
                anos (int): O número de anos para pagamento.

    Return:
    str: Mensagem indicando se o empréstimo foi aprovado ou negado.
    """
    prestacao_mensal = valor_da_casa / (anos * 12)

    if prestacao_mensal > (salario * 0.3):
        return "Empréstimo negado. A prestação mensal excede 30% do seu salário."
    else:
        return "Empréstimo aprovado. A prestação mensal é de R${:.2f}.".format(prestacao_mensal)
    
resultado = aprovar_emprestimo(valor_da_casa, salario, anos)
print(resultado)