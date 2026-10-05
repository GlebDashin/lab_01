class ToolkitError(Exception):
    pass

class CalculatorError(ToolkitError):
    pass

class EmptyExpressionError(CalculatorError):
    pass

class InvalidCharacterError(CalculatorError):
    pass

class FirstOrEndOperandError(CalculatorError):
    pass

class MissingOperandError(CalculatorError):
    pass

class TwoInwalidOperatorsError(CalculatorError):
    pass

class DivisionByZeroError(CalculatorError):
    pass

class ConverterError(ToolkitError):
    pass

class UnkownUnitError(ConverterError):
    pass

class IncompatibleUnitsError(ConverterError):
    pass

class InvalidValue(ConverterError):
    pass
