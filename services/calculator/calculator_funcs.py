def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def calc(input):
    if input['oper'] == 0:
        return add(input['op_a'], input['op_b'])
    elif input['oper'] == 1:
        return subtract(input['op_a'], input['op_b'])
    elif input['oper'] == 2:
        return multiply(input['op_a'], input['op_b'])
    elif input['oper'] == 3:
        return divide(input['op_a'], input['op_b'])

    return 'operator must be set as key=oper'