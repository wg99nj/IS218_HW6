from calculator.commands import Command

class ModCommand(Command):
    def execute(self, a: float, b: float) -> float:
        return a % b