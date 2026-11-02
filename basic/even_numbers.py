def print_characters_recursive(text, index):
    # BASE CASE
    if index >= len(text):
        return

    # PROCESS
    print(text[index])

    # RECURSIVE STEP
    print_characters_recursive(text, index + 1)


def print_characters_iterative(text):
    index = 0

    while index < len(text):
        print(text[index])
        index += 1


# Testing
print("Recursive:")
print_characters_recursive("Hello", 0)

print("Iterative:")
print_characters_iterative("Hello")