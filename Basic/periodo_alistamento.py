idade = int(input("Digite a sua idade: "))


def verificar_periodo_alistamento(idade):
    """
    Função para verificar o período de alistamento militar com base na idade do usuário.

    Parâmetros: idade (int): A idade do usuário.

    Return:
    str: Mensagem indicando se o usuário está no período de alistamento, se já passou ou se ainda não chegou.
    """
    if idade < 18:
        return "Você ainda não está no período de alistamento militar. Faltam {} anos para o alistamento.".format(18 - idade)
    elif idade == 18:
        return "Você está no período de alistamento militar."
    else:
        return "Você está atrasado para o alistamento militar. Deveria ter se alistado há {} anos.".format(idade - 18)

resultado = verificar_periodo_alistamento(idade)
print(resultado)