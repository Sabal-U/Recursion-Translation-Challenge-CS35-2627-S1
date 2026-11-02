def repeat_message_iterative(message, times):
    while times > 0:
        print(message)
        times -= 1


def repeat_message_recursive(message, times):
    # BASE CASE
    if times == 0:
        return

    # PROCESS
    print(message)

    # RECURSIVE STEP
    repeat_message_recursive(message, times - 1)


message = input("Enter a message: ")

while True:
    try:
        times = int(input("How many times should it print? "))

        if times >= 0:
            break
        else:
            print("Please enter a number that is 0 or greater.")

    except ValueError:
        print("Invalid input. Please enter a whole number.")

repeat_message_recursive(message, times)