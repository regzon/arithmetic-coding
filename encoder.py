#!/usr/bin/env python3

import math
from itertools import count
from calculations import Interval, calculate_cumulative_probs


def find_binary(left, right):
    result = ''

    def iterate(number):
        number *= 2
        number, whole = math.modf(number)
        whole = int(whole)
        return number, whole

    for _ in count():
        left, left_whole = iterate(left)
        right, right_whole = iterate(right)
        result += str(right_whole)

        if left_whole != right_whole:
            break

    return result


def encode(symbol_sequence, entries):
    cumulative_probs = calculate_cumulative_probs(entries)
    cumulative_dict = dict(cumulative_probs)
    interval = Interval(left=0, right=1)

    for symbol in symbol_sequence:
        interval_length = interval.right - interval.left
        left_offset = interval_length * cumulative_dict[symbol].left
        right_offset = interval_length * cumulative_dict[symbol].right
        interval = Interval(
            left=interval.left + left_offset,
            right=interval.left + right_offset,
        )

    print(f"Encoded interval: ({interval.left}, {interval.right})")
    binary = find_binary(interval.left, interval.right)
    print(f"Closest binary number: {binary}")


def main():
    raw_symbols = input("Enter symbols that should be encoded: ")
    symbols = raw_symbols.split()

    raw_probs = input("Enter their probabilities: ")
    probs = [float(prob) for prob in raw_probs.split()]

    if len(symbols) != len(probs):
        raise Exception("Amount of probabilities should be equal"
                        "to amount of symbols")

    message = input("Enter the message to encode (e.g. 'A B C D'): ")
    symbol_sequence = message.split()

    encode(symbol_sequence, zip(symbols, probs))


if __name__ == '__main__':
    main()
