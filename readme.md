Random Number Generator

Overview

This is a Python script that generates a specified number of random integers between 1 and 1000. The script accepts command-line arguments to define the number of integers, sorting order, step interval for divisibility, and upper numeric limit.

Features

- Command-Line Interface: Easily specify parameters like `amount`, `order`, `step`, and `limit`.
- Modular Design: Organized into separate modules for cleaner, maintainable code.
- Robust and Flexible: Handles edge cases with meaningful error messages.
- Unit Testing: Comprehensive test suite ensures reliable functionality.

Installation
To use this script, ensure you have Python 3+ installed.

Usage: python main.py -amount <number> -order <a|d> -step <number> -limit <number>

-amount: Number of random integers desired. Default is 100.
-order: Order of integers: 'a' for ascending, 'd' for descending. Default is 'd'.
-step: Step interval for divisibility. Default is 2.
-limit: Upper limit of the range. Default is 1000.

E.g. python main.py -amount 100 -order d -step 2 limit 1000
(Generate 100 random numbers between 1 and 1000, divisible by 2, in descending order.)