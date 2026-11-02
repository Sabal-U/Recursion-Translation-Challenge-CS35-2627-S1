def double_until_limit_recursive(number, limit):
    # BASE CASE
    if number > limit:
        return

    # PROCESS
    print(number)

    # RECURSIVE STEP
    double_until_limit_recursive(number * 2, limit)


def double_until_limit_iterative(number, limit):
    while number <= limit:
        print(number)
        number = number * 2


# Testing
print("Recursive:")
double_until_limit_recursive(2, 20)

print("Iterative:")
double_until_limit_iterative(2, 20)