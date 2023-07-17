#!/usr/bin/env python3


def startpoints(sequence):
    startpoints = []
    smallest_so_far = float(
        "inf"
    )  # Initialize to positive infinity to get first startpoint
    for element in sequence:
        if element < smallest_so_far:
            startpoints.append(element)
            smallest_so_far = element
    return startpoints


def bibseqs(sequence):
    subsequences = []
    previous_startpoint = 0
    for startpoint in startpoints(sequence):
        subsequences.append(sequence[previous_startpoint : startpoint - 1])
        previous_startpoint = startpoint
    subsequences.append(sequence[previous_startpoint:-1])
    return subsequences
