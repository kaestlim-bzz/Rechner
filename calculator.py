# Erstellen Sie hier die Klasse Calculator entsprechend dem Klassendiagramm.
# Beachten Sie, dass hier keine Exceptions verarbeitet werden. Sie werden dem
# Hauptprogramm (main) weitergereicht und dort zentral verwaltet.
# Halten Sie sich ganz genau an die Vorgaben, damit die Testfälle aus
# test_calculator.py korrekt ablaufen.
from math_operations import *
from reader import Reader
class Calculator:
    def __init__(self, tokenizer):
        self._tokenizer = tokenizer
        self._math_op = None
        self._my_reader = Reader()

    @property
    def math_op(self):
        return self._math_op

    def read_input(self):
        self._my_reader.screen_info()
        value = self._my_reader.read()
        self._tokenizer.split(value)


    def create_concrete_op(self):
        operator = self._tokenizer.operation
        if operator == "+":
            self._math_op = Adder()

        elif operator == "-":
            self._math_op = Subtractor()

        elif operator == "*":
            self._math_op = Multiplier()

        elif operator == "/":
            self._math_op = Divider()

        elif operator == "^":
            self._math_op = Exposer()

    def calculate(self):
        ref_value = self.math_op
        if ref_value is not None:
            val1 = self._tokenizer.value1
            val2 = self._tokenizer.value2
            ref_value.execute_op(val1, val2)
            print(ref_value.result)

