def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def calc(input):
    answer = 0
    if input['oper'] == 0:
        answer = add(input['op_a'], input['op_b'])
    elif input['oper'] == 1:
        answer = subtract(input['op_a'], input['op_b'])
    elif input['oper'] == 2:
        answer = multiply(input['op_a'], input['op_b'])
    elif input['oper'] == 3:
        answer = divide(input['op_a'], input['op_b'])
    else:
        return 'operator must be set as key=oper'

    return {'answer' : answer}