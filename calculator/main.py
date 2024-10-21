# calculator/main.py
import os
import logging
from dotenv import load_dotenv  # type: ignore
from calculator import Calculator

# Load environment variables from .env file
load_dotenv()

# Set up logging
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("calculator.log"),
        logging.StreamHandler()
    ]
)

def main():
    env_name = os.getenv("ENV_NAME")
    logging.info(f"Environment: {env_name}")

    # Initialize the calculator
    calc = Calculator()

    while True:
        try:
            # Get the user operation input
            operation = input("Enter operation (add, subtract, multiply, divide) or 'exit': ").strip()
            
            if operation == "exit":
                logging.info("Calculator session ended by user.")
                break
            
            # Get numbers from the user
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            # Execute the command
            result = calc.execute_command(operation, a, b)
            logging.info(f"Executed {operation} on {a} and {b}, result: {result}")
            print(f"Result: {result}")
        
        except ValueError as e:
            logging.error(f"Invalid input: {e}")
            print(f"Error: {e}")

        except ZeroDivisionError as e:
            logging.error(f"Attempted division by zero: {e}")
            print(f"Error: {e}")

        except Exception as e:
            logging.error(f"Unexpected error occurred: {e}")
            print(f"Error: {e}")

if __name__ == "__main__":
    main()