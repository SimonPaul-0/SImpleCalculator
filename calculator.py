import re

def calculate(expression):
    """
    Evaluate a mathematical expression with basic operators: +, -, *, %, and /.

    Parameters:
    - expression (str): Mathematical expression to be evaluated.

    Returns:
    - The result of the calculation or an error message.
    """
    try:
        # Validate expression
        if not re.match(r'^[0-9+\-*/%() ]+$', expression):
            raise ValueError("Invalid characters in the expression.")

        # Resolve parentheses first
        while '(' in expression:
            match = re.search(r'\([^()]+\)', expression)
            if match:
                sub = match.group(0)[1:-1]
                sub_result = calculate(sub)
                expression = expression.replace(match.group(0), str(sub_result))

        # Perform calculation
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "Error: Division by zero"
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    """
    Main function to take user input and perform calculations.
    """
    while True:
        expr = input('Enter a mathematical expression: ')

        res = calculate(expr)
        if isinstance(res, str):
            print(res)
        else:
            print(f'Result of the expression: {res}')

        inter_choice = input('Want to see an intermediate result? (Y/N): ')
        if inter_choice.upper() == 'Y':
            inter_expr = input('Enter an intermediate expression: ')
            inter_res = calculate(inter_expr)
            print(f'Intermediate result: {inter_res}')

        choice = input('Perform another calculation? (Y/N): ')
        if choice.upper() != 'Y':
            break

if __name__ == "__main__":
    main()

