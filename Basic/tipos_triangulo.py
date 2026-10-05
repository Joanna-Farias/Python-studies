a = float(input('Digite o valor do lado A: '))
b = float(input('Digite o valor do lado B: '))
c = float(input('Digite o valor do lado C: '))


def tipos_triangulo(a, b, c):
    """
    Função para determinar o tipo de triângulo com base nos lados fornecidos.
    
    Parâmetros: a (float): O valor do lado A.
                b (float): O valor do lado B.
                c (float): O valor do lado C.
    
    Return: str: Mensagem indicando o tipo de triângulo (equilátero, isósceles ou escaleno).
    
    """

    if(a == b == c):
        return "O triângulo é equilátero."
    elif(a != b and a != c and b != c):
        return "O triângulo é escaleno."
    else:
        return "O triângulo é isósceles."

resultado = tipos_triangulo(a, b, c)
print(resultado)