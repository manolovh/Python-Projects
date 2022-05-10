def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


print("\t\t\tWelcome to our basic calculator.\n\tYou can use it to perform just one or multiple operations:\n"
      "\t- Add(+)\n\t- Subtract(-)\n\t- Multiply(*)\n\t- Divide(/)\n")

chosen = input("\tPlease select your first number and the symbol of your chosen operation,\n"
                   "\t\tseparated with a space: ").split()
first_num = float(chosen[0])
operator = chosen[1]

while operator not in ('-', '+', '/', '*'):
    print("\tInvalid operator, please select a new one!")
    operator = input("\t\t -> ")

numbers = []
numbers.append(first_num)

while True:
    second_num = float(input("Select your next number or '0' to finish: "))
    if second_num == 0:
        break
    numbers.append(second_num)

    if operator == '+':
        add(first_num, second_num)
        first_num += second_num

    elif operator == '-':
        subtract(first_num, second_num)
        first_num -= second_num

    elif operator == '*':
        multiply(first_num, second_num)
        first_num *= second_num

    elif operator == '/':
        divide(first_num, second_num)
        first_num /= second_num

print(f"{f' {operator} '.join(map(str, numbers))} is -> {first_num}")