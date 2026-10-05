from .errors import(
    EmptyExpressionError,
    InvalidCharacterError,
    MissingOperandError,
    TwoInwalidOperatorsError,
    DivisionByZeroError,
    FirstOrEndOperandError
)

def calc(expression: str) -> float:

    token_expression = tokenize(expression)
    validate(token_expression)
    result=calculation(token_expression)

    return result

def tokenize(expression: str) -> list[str]:
    token_expression: list[str] = []
    token = ""

    for i in expression:
        if i in "0123456789.":
            token += i
        elif i in "*/+-":
            if token != "":
                token_expression.append(token)
                token = ""
                token_expression.append(i)
            else:
                token_expression.append(i)
        elif i in " ":
            if token != "":
                token_expression.append(token)
                token = ""
        else:
            raise InvalidCharacterError(f"Неизвестный символ: {i}")
    if token != "":
        token_expression.append(token)

    return token_expression

def validate(token_expression: list[str]) -> None:
    if not token_expression:
        raise EmptyExpressionError("Пустое выражение")
    if token_expression[0] in "*/":
        raise FirstOrEndOperandError("Невозможная операция в начале строки")
    if token_expression[-1] in "+-*/":
        raise FirstOrEndOperandError("Невозможная операция в конце строки")
    if token_expression[0] in "+-" and token_expression[1] in "+-":
        raise TwoInwalidOperatorsError("Две операции в начале строки")
    for i in range(len(token_expression)):
        if token_expression[i].count(".")>1:
            raise InvalidCharacterError("Несколько точек в числе")
        if token_expression[i] == ".":
            raise InvalidCharacterError("Число из одной точки")
        if i>0 and isnumber(token_expression[i-1]) and isnumber(token_expression[i]):
            raise MissingOperandError("Между чисел нет операции")
        if i>0 and token_expression[i-1] in "/*+-" and token_expression[i] in "/*":
            raise TwoInwalidOperatorsError("Неправильная комбинация 2 операций")
        if i>1 and token_expression[i-2] in "/*+-" and token_expression[i-1] in "/*+-" and token_expression[i] in "*/+-":
            raise TwoInwalidOperatorsError("3 операции подряд")

def calculation(token_expression: list[str]):

    if token_expression[0] == "-":
        del token_expression[0]
        token_expression[0] = f"-{token_expression[0]}"
    elif token_expression[0] == "+":
        del token_expression[0]
        token_expression[0] = f"+{token_expression[0]}"

    i = 2
    while i < len(token_expression):
        if token_expression[i-2] in "+-*/" and token_expression[i-1] == "-" and  isnumber(token_expression[i]):
            token_expression[i]=f"-{token_expression[i]}"
            del token_expression[i-1]
        elif token_expression[i-2] in "+-*/" and token_expression[i-1] == "+" and  isnumber(token_expression[i]):
            token_expression[i]=f"+{token_expression[i]}"
            del token_expression[i-1]
        else:
            i += 1

    i = 2
    while i < len(token_expression):
        if token_expression[i-1] in "*/":
            token_expression[i-1] = str(calculate_operation(token_expression[i-2], token_expression[i-1], token_expression[i]))
            del token_expression[i]
            del token_expression[i-2]
        else:
            i += 1
    i = 2
    while i < len(token_expression):
        if token_expression[i-1] in "+-":
            token_expression[i-1] = str(calculate_operation(token_expression[i-2], token_expression[i-1], token_expression[i]))
            del token_expression[i]
            del token_expression[i-2]
        else:
            i += 1
    return float(token_expression[0])

def calculate_operation(left: str, operation: str, right: str) -> float:
    left_number = float(left)
    right_number = float(right)

    match operation:
        case "+":
            return (left_number+right_number)
        case "-":
            return (left_number-right_number)
        case "*":
            return (left_number*right_number)
        case "/":
            if operation == "/" and right_number == 0:
                raise DivisionByZeroError("Деление на 0")
            return (left_number/right_number)
        case _:
            raise InvalidCharacterError(f"Неизвестная операция {operation}")

def isnumber(token: str) -> bool:
    if token[-1] in "0123456789":
        return True
    return False
