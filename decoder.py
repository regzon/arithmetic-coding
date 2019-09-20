#!/usr/bin/env python3

from calculations import Interval, calculate_cumulative_probs


def decode(number, entries, exit_symbol):
    cumulative_probs = calculate_cumulative_probs(entries)
    interval = Interval(left=0, right=1)
    decoded = []
    symbol = None

    while symbol != exit_symbol:
        interval_length = interval.right - interval.left
        offset = (number - interval.left) / interval_length

        for _symbol, _interval in cumulative_probs:
            if offset < _interval.right:
                entry = (_symbol, _interval)
                break
        else:
            entry = cumulative_probs[-1]

        symbol = entry[0]
        left_offset = interval_length * entry[1].left
        right_offset = interval_length * entry[1].right
        interval = Interval(
            left=interval.left + left_offset,
            right=interval.left + right_offset,
        )
        decoded.append(symbol)

    return decoded


def main():
    raw_symbols = input("Enter symbols that should be decoded: ")
    symbols = raw_symbols.split()

    raw_probs = input("Enter their probabilities: ")
    probs = [float(prob) for prob in raw_probs.split()]

    if len(symbols) != len(probs):
        raise Exception("Amount of probabilities should be equal"
                        "to amount of symbols")

    exit_symbol = input("Enter the exit symbol: ")
    if exit_symbol not in symbols:
        raise Exception("An exit symbol should be defined in symbols list")

    number = input("Enter the number to decode (e.g. '0.5138'): ")
    number = float(number)

    decoded = decode(number, zip(symbols, probs), exit_symbol)
    print(' '.join(decoded))


if __name__ == '__main__':
    main()
