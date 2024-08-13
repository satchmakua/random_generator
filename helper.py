def print_numbers(numbers, order):
    if order == 'a':
        numbers.sort()  # Sort in ascending order
    elif order == 'd':
        numbers.sort(reverse=True)  # Sort in descending order
    else:
        raise ValueError("Order must be 'a' for ascending or 'd' for descending.")

    for number in numbers:
        print(number)
