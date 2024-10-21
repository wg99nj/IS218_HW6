# calculator/commands.py

from abc import ABC, abstractmethod

# Abstract Command Class
class Command(ABC):
    @abstractmethod
    def execute(self, a: float, b: float) -> float:
        pass

# Command for Addition
class AddCommand(Command):
    def execute(self, a: float, b: float) -> float:
        return a + b

# Command for Subtraction
class SubtractCommand(Command):
    def execute(self, a: float, b: float) -> float:
        return a - b

# Command for Multiplication
class MultiplyCommand(Command):
    def execute(self, a: float, b: float) -> float:
        return a * b

# Command for Division
class DivideCommand(Command):
    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b