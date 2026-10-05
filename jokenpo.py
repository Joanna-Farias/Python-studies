import random


def jokenpo():
    """
        Função para jogar o jogo de Jokenpô (Pedra, Papel, Tesoura) entre o usuário e o computador.

        Parâmetros: Nenhum.

        Retorno: str: Mensagem indicando o resultado do jogo (vitória, derrota ou empate).
    """
    opcoes = ['Pedra', 'Papel', 'Tesoura']
    computador = random.randint(0, 2)

    usuario = opcoes.index(input("Escolha Pedra, Papel ou Tesoura: ").capitalize())

    print(f"Computador escolheu: {opcoes[computador]}")

    if usuario == computador:
        return "Empate!"
    elif usuario == 0:                       
        if computador == 2:                  
            return "Você ganhou!"
        else:
            return "Você perdeu!"
    elif usuario == 1:                       
        if computador == 0:                 
            return "Você ganhou!"
        else:
            return "Você perdeu!"
    else:                                   
        if computador == 1:                  
            return "Você ganhou!"
        else:
            return "Você perdeu!"

resultado = jokenpo()
print(resultado)