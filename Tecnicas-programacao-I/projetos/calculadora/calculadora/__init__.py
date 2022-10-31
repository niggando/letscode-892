from .funcoes import soma, subtracao, divisao, multiplicacao

def calcule():
    a = float(input("Insira um número: "))
    b = float(input("Insira um número: "))
    operacao = input("Insira uma Operação válida: ")
    
    switcher = {
        "soma": soma,
        "subtracao": subtracao,
        "divisao": divisao,
        "+": soma,
        "-": subtracao,
        "/": divisao,
        "*": multiplicacao,
    }
    
    if operacao in switcher.keys():
        resultado = switcher[operacao](a,b)
    
    else:
        raise KeyError(f"Operação desconhecida {operacao}, escolha entre {list(switcher.keys())}")
    return resultado

