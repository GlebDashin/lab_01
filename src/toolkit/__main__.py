import argparse
import sys

from .calculator import calc
from .errors import CalculatorError

def create_parser () -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()

    commands = parser.add_subparsers(dest="command", required=True)

    calc_parser = commands.add_parser("calc", prefix_chars="/")
    calc_parser.add_argument("expression", type = str)

    convert_parser = commands.add_parser("convert")
    convert_parser.add_argument("value", type=float)
    convert_parser.add_argument("--from", dest="from_unit", required=True)
    convert_parser.add_argument("--to", dest="to_unit", required=True)
    return parser

def main() -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """
    parser = create_parser()
    args = parser.parse_args()


    if args.command == "calc":
        try:
            print(calc(args.expression))
        except CalculatorError as error:
            print (error, file=sys.stderr)
            sys.exit(2)


    if args.command == "convert":
        pass


if __name__ == "__main__":
    main()
