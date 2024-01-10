#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        return []
    if length == 1:
        return [0]
    else:
        fibonacci = [0, 1]
    while len(fibonacci) < length:
        next_number = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_number)
    return fibonacci

    