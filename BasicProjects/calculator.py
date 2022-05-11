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

first_num = float(input("\tPlease select your first number: "))
initial_num = first_num

numbers = []
operators = []

while True:
    chosen_2 = input("\t\tChoose operator and number, separated with a space,\n"
                   "\t\t\tor '0' to finish -> ").split()
    operator = chosen_2[0]
    if operator == '0':
        break
    second_num = float(chosen_2[1])
    if operator not in ('-', '+', '/', '*'):
        print("\tInvalid operator, please select a new one!")
        continue

    numbers.append(second_num)
    operators.append(operator)

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

print(initial_num, end=' ')
result = zip(operators, numbers)
for res in result:
    print(*res, end=' ')
print(f"-> {first_num}")