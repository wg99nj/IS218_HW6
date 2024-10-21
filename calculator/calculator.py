# calculator/calculator.py

import os
import importlib
from calculator.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

class Calculator:
    def __init__(self):
        self.commands = {
            'add': AddCommand(),
            'subtract': SubtractCommand(),
            'multiply': MultiplyCommand(),
            'divide': DivideCommand(),
        }
    
    def repl(self):
        print("Welcome to the interactive calculator. Type 'menu' for commands.")
        
        while True:
            user_input = input("> ").strip().lower()
            if user_input == "exit":
                break
            elif user_input == "menu":
                self.show_menu()
            else:
                self.execute_command(user_input)
    
    def show_menu(self):
        print("Available commands:")
        for cmd in self.commands:
            print(cmd)
        print("Type 'exit' to quit.")

    def execute_command(self, user_input):
        try:
            command_name, a, b = user_input.split()
            a, b = float(a), float(b)
            command = self.commands.get(command_name)
            if command:
                result = command.execute(a, b)
                print(f"Result: {result}")
            else:
                print("Unknown command.")
        except ValueError:
            print("Invalid input. Use format: <command> <a> <b>")
        except ZeroDivisionError as e:
            print(e)

class CalculatorWithPlugins(Calculator):
    def __init__(self):
        super().__init__()
        self.load_plugins()

    def load_plugins(self):
        plugin_dir = 'calculator/plugins'
        for filename in os.listdir(plugin_dir):
            if filename.endswith(".py") and filename != "__init__.py":
                module_name = filename[:-3]  # Strip .py
                module = importlib.import_module(f'calculator.plugins.{module_name}')
                command_class = getattr(module, module_name.capitalize() + 'Command')
                self.commands[module_name] = command_class()
