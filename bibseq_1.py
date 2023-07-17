#!/usr/bin/env python


def bibseq(sequence):
    subsequences = []
    current_subsequence = []
    leading_element = float(
        "inf"
    )  # Initialize to positive infinity to handle the first subsequence

    for element in sequence:
        if element < leading_element:
            if current_subsequence:
                subsequences.append(current_subsequence)
            current_subsequence = [element]
            leading_element = element
        else:
            current_subsequence.append(element)

    # Add the last subsequence after the loop finishes
    if current_subsequence:
        subsequences.append(current_subsequence)

    return subsequences
