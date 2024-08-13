import random

def generate_random_numbers(amount, step, limit=1000):
    if amount < 1:
        raise ValueError("Amount must be a positive integer.")
    if step < 1:
        raise ValueError("Step must be a positive integer.")

    # Generate a list of numbers from step to the specified limit that are divisible by step
    divisible_numbers = [num for num in range(step, limit + 1, step)]
    
    if len(divisible_numbers) == 0:
        raise ValueError("No numbers in the range are divisible by the step.")

    # Allow duplicates by using random choices with replacement
    return [random.choice(divisible_numbers) for _ in range(amount)]
