# Hier realisieren Sie alle Klassen für den Rechner.
# Ausgehend von der abstrakten Klasse MathOp werden die
# konkreten Ableitungen (Adder, Subtractor usw.) realisiert.
# Halten Sie sich ganz genau an die Vorgaben, damit die Testfälle aus
# test_mathop_class_instantiation.py und test_math_operations.py korrekt ablaufen.
from abc import ABC, abstractmethod
class MathOp(ABC):

    def __init__(self):
        super().__init__()
        self._result = 0.0


    @abstractmethod
    def execute_op(self, val1: float, val2: float):
        pass
    @property
    def result(self):
        return self._result

class Adder(MathOp):

    def execute_op(self, val1: float, val2: float):
        self._result = val1 + val2

class Subtractor(MathOp):

    def execute_op(self, val1: float, val2: float):
        self._result = val1 - val2

class Multiplier(MathOp):

    def execute_op(self, val1: float, val2: float):
        self._result = val1 * val2

class Divider(MathOp):
 try:
    def execute_op(self, val1: float, val2: float):
        self._result = val1 / val2

 except ZeroDivisionError as Zerr:
     raise (Zerr)

class Exposer(MathOp):

    def execute_op(self, val1: float, val2: float):
        self._result = val1 ** val2


