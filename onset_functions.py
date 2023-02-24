import itertools

import numpy as np


def gamma_1(time_series, a_1, b_1, window=5):
    pr_5day = [np.sum(time_series[i: i + window]) for i in range(len(time_series))]

    out = np.zeros(len(time_series))

    for i in range(len(time_series)):
        if pr_5day[i] <= b_1:
            out[i] = 0
        elif b_1 < pr_5day[i] < a_1:
            out[i] = (pr_5day[i] - b_1) / (a_1 - b_1)
        elif pr_5day[i] >= a_1:
            out[i] = 1
        else:
            out[i] = None

    return out


def gamma_2(time_series, a2, b2, threshold=1, window=5):
    binary = time_series >= threshold
    out = np.zeros(len(time_series))

    for i in range(len(time_series)):
        five_sum = sum(binary[i:i + window])
        if five_sum <= b2:
            out[i] = 0
        elif b2 < five_sum < a2:
            out[i] = (five_sum - b2) / (a2 - b2)
        elif five_sum >= a2:
            out[i] = 1
        else:
            out[i] = None

    return out


def gamma_3(time_series, a3, b3, threshold=1, window=30):
    binary = time_series < threshold
    out = np.zeros(len(time_series))

    for i in range(len(time_series)):
        thirty_days = binary[i:i + window]
        list_length_dry_spell = [sum(1 for _ in group) for key, group in itertools.groupby(thirty_days) if key]
        dry_spell_max = max(list_length_dry_spell)

        if dry_spell_max >= a3:
            out[i] = 0
        elif b3 < dry_spell_max < a3:
            out[i] = (dry_spell_max - b3) / (a3 - b3)
        elif dry_spell_max <= b3:
            out[i] = 1
        else:
            out[i] = None

    return out
