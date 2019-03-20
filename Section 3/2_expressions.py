def expressions(expr):
    if expr[0] == '(':
        expr[:] = expr[1:]
        result = terms(expr)
        expr[:] = expr[1:]
        return result
    result = expr[0]
    expr[:] = expr[1:]
    return float(result)

def factors(expr):
    result = expressions(expr)
    while expr[0] in '*/':
        if expr[0] == '*':
            expr[:] = expr[1:]
            result *= expressions(expr)
        else:
            expr[:] = expr[1:]
            result /= expressions(expr)
    return result

def terms(expr):
    result = factors(expr)
    while expr[0] in '+-':
        if expr[0] == '+':
            expr[:] = expr[1:]
            result += factors(expr)
        else:
            expr[:] = expr[1:]
            result -= factors(expr)
    return result

print(terms(list('4+2*(3-1).')))