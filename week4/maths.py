def basic_operations(a, b):
    try:
        addition = a + b
        subtraction = a - b
        multiplication = a * b
        division = a / b
        return {f"{a}+{b}": addition, f"{a}-{b}": subtraction, f"{a}*{b}": multiplication, f"{a}/{b}": division}
    except ZeroDivisionError:
        return {'error': 'Division by zero is not allowed.'}

def power_operation(base, exponent, **kwargs):
    result = base ** exponent
    modulo_value = kwargs.get('modulo')
    if modulo_value is not None:
        result = result % modulo_value
    return result

def apply_operations(operation_list):
    results = list(map(lambda x: x[0](*x[1]), operation_list))
    return results
