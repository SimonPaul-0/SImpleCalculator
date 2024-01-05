def calculate_result(num_list, operator):
    if operator == '+':
        return sum(num_list)
    elif operator == '-':
        return num_list[0] - sum(num_list[1:])
    elif operator == '*':
        result = 1
        for num in num_list:
            result *= num
        return result
    elif operator == '%':
        return num_list[0] % num_list[1]
    elif operator == '/':
        result = num_list[0]
        for num in num_list[1:]:
            if num != 0:
                result /= num
            else:
                return "Cannot divide by zero"
        return result

def main():
    num_list = [int(input(f'Enter number {i + 1}: ')) for i in range(5)]

    while True:
        operator = input('Enter the operator you want to use (+, -, *, %, /): ')

        result = calculate_result(num_list, operator)
        if isinstance(result, str):
            print(f"Error: {result}")
        else:
            print(f'The result of the operation is: {result}')

        choice = input('Do you want to perform another calculation? (Y/N): ')
        if choice.upper() != 'Y':
            break

if __name__ == "__main__":
    main()
