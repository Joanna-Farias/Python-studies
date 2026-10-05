nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

def calcular_media(nota1, nota2, nota3):
    """
    Função para calcular a média de três notas.

    Parâmetros: nota1 (float): A primeira nota.
                nota2 (float): A segunda nota.
                nota3 (float): A terceira nota.

    Return: float: A situação do aluno. 
    """

    media = (nota1 + nota2 + nota3) / 3

    if(media < 5.0):
        return "Reprovado."
    elif(media >= 5.0 and media < 7.0):
        return "Em recuperação."
    else:
        return "Aprovado."

resultado = calcular_media(nota1, nota2, nota3)
print("A situação do aluno é: {}".format(resultado))