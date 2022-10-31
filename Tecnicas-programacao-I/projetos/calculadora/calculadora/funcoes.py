def soma(a,b):
    """
    Args:
        a: (int, float)
        b: (int, float)
    
    return:
        a + b: (int, float)
    """
    if isinstance(a, (int, float)) or (b, (int, float)):
        return a+b
    
    else:
        raise TypeError(f"O input de 'a' e 'b' devem ser um número, recebido {a} ({type(a)}) e {b} ({type(b)})")
    
def subtracao(a,b):
    """
    Args:
        a: (int, float)
        b: (int, float)
    
    return:
        a + b: (int, float)
    """
    if isinstance(a, (int, float)) or (b, (int, float)):
        return a-b
    
    else:
        raise TypeError(f"O input de 'a' e 'b' devem ser um número, recebido {a} ({type(a)}) e {b} ({type(b)})")

def divisao(a,b):
    """
    Args:
        a: (int, float)
        b: (int, float)
    
    return:
        a + b: (int, float)
    """
    if isinstance(a, (int, float)) or (b, (int, float)):
        if a == 0 or b == 0:
            return 0
        else:
            return a/b
    
    else:
        raise TypeError(f"O input de 'a' e 'b' devem ser um número, recebido {a} ({type(a)}) e {b} ({type(b)})")

def multiplicacao(a,b):
    """
    Args:
        a: (int, float)
        b: (int, float)
    
    return:
        a + b: (int, float)
    """
    if isinstance(a, (int, float)) or (b, (int, float)):
        return a*b
    
    else:
        raise TypeError(f"O input de 'a' e 'b' devem ser um número, recebido {a} ({type(a)}) e {b} ({type(b)})")