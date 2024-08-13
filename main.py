import argparse
from random_utils import generate_random_numbers
from helper import print_numbers

def parse_args():
    parser = argparse.ArgumentParser(description="Generate a list of random even integers.")
    parser.add_argument('-limit', type=int, help="Maximum value of random integers desired.", default=1000)
    parser.add_argument('-amount', type=int, help="Number of random integers desired", default=100)
    parser.add_argument('-order', choices=['a', 'd'], help="Order of integers: 'a' for ascending, 'd' for descending.", default='d')
    parser.add_argument('-step', type=int, help="Step interval for the integers.", default=2)
    return parser.parse_args()

def main():
    try:
        args = parse_args()
        numbers = generate_random_numbers(args.amount, args.step, args.limit)
        print_numbers(numbers, args.order)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
