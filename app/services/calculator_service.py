import math

def evaluate_expression(expr: str):
    """Safely evaluate mathematical expression."""
    expr = expr.strip()
    expr = expr.replace('×', '*').replace('÷', '/').replace('^', '**')
    
    safe_dict = {
        'sin': math.sin,
        'cos': math.cos,
        'tan': math.tan,
        'asin': math.asin,
        'acos': math.acos,
        'atan': math.atan,
        'sinh': math.sinh,
        'cosh': math.cosh,
        'tanh': math.tanh,
        'sqrt': math.sqrt,
        'log': math.log,
        'log10': math.log10,
        'log2': math.log2,
        'ln': math.log,
        'exp': math.exp,
        'abs': abs,
        'round': round,
        'floor': math.floor,
        'ceil': math.ceil,
        'factorial': math.factorial,
        'pow': pow,
        'pi': math.pi,
        'e': math.e,
        'tau': math.tau,
        'deg': math.degrees,
        'rad': math.radians,
        'math': math,
    }
    
    try:
        result = eval(expr, {"__builtins__": {}}, safe_dict)
        return result
    except Exception as e:
        raise ValueError(f"计算错误: {str(e)}")
