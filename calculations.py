from collections import namedtuple

Interval = namedtuple('Interval', ['left', 'right'])


def calculate_cumulative_probs(entries):
    cumulative_probs = []
    total_prob = 0

    for symbol, prob in entries:
        interval = Interval(total_prob, total_prob + prob)
        cumulative_probs.append((symbol, interval))
        total_prob += prob

    return cumulative_probs
