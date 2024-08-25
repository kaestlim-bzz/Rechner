# Im Hauptprogramm erzeugen Sie ein Tokenizer- und ein Calculator-Objekt.
# Führen Sie dann den Ablauf
# - Wert einlesen
# - Operation erzeugen
# - Berechnung ausführen
# durch.
# Hier müssen alle auftretenden Exceptions zentral verwaltet werden.
from calculator import *
from tokenizer import Tokenizer
from exceptions import *
def main():
    hi = Tokenizer()
    hi.add_operation('%')
    calc = Calculator(Tokenizer())
    try:
        calc.read_input()
        calc.create_concrete_op()
        calc.calculate()
    except NumberFormatException as err:
        print(err)
    except OperationException as orr:
        print(orr)
    except ZeroDivisionError as Zer:
        print('Error nicht durch null teilen')
        pass


if __name__ == '__main__':
    main()
