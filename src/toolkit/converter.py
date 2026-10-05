from .errors import(
    UnknownUnitError,
    IncompatibleUnitsError,
    InvalidValueError
)
from .constants import(
    CONVERSION
)

def convert(value: float, from_: str, to_: str ) -> float:
    if from_ not in CONVERSION:
        raise UnknownUnitError(f"Неизвестная единица измерения {from_}")
    if to_ not in CONVERSION:
        raise UnknownUnitError(F"неизвестная единица измерения {to_}")

    from_kind, from_ratio = CONVERSION[from_]
    to_kind, to_ratio = CONVERSION[to_]

    if from_kind != to_kind:
        raise IncompatibleUnitsError(f"Нельзя перевести {from_kind} в {to_kind}")

    match from_kind:
        case "mass" | "length":
            return value * from_ratio / to_ratio
        case "temperature":
            match from_:
                case "k":
                    if value < 0:
                        raise InvalidValueError("Температура ниже абсолютного нуля")
                    match to_:
                        case "f":
                            return value * 9 / 5 - 459.67
                        case "c":
                            return value - 273.15
                        case "k":
                            return value
                case "f":
                    if value < -459.67:
                        raise InvalidValueError("Температура ниже абсолютного нуля")
                    match to_:
                        case "f":
                            return value
                        case "c":
                            return (value - 32) * 5 / 9
                        case "k":
                            return (value + 459.67) * 5 / 9
                case "c":
                    if value < -273.15:
                        raise InvalidValueError("Температура ниже абсолютного нуля")
                    match to_:
                        case "f":
                            return value * 9 / 5 + 32
                        case "c":
                            return value
                        case "k":
                            return value + 273.15
    raise UnknownUnitError(f"Неизвестное преобразование: {from_} → {to_}")
