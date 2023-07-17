from bibseq_1 import bibseq


# Pytest unit tests
def test_sunny_day():
    sequence = [31, 41, 59, 26, 53, 58, 97, 93, 23, 84, 62, 64, 33]
    expected_result = [[31, 41, 59], [26, 53, 58, 97, 93], [23, 84, 62, 64, 33]]
    assert bibseq(sequence) == expected_result


def test_descending():
    sequence = [5, 4, 3, 2, 1]
    expected_result = [[5], [4], [3], [2], [1]]
    assert bibseq(sequence) == expected_result


def test_ascending():
    sequence = [10, 20, 30, 40, 50]
    expected_result = [[10, 20, 30, 40, 50]]
    assert bibseq(sequence) == expected_result


def test_mixed():
    sequence = [35, 50, 25, 40, 15, 30, 10, 20]
    expected_result = [[35, 50], [25, 40], [15, 30], [10, 20]]
    assert bibseq(sequence) == expected_result


def test_empty():
    sequence = []
    expected_result = []
    assert bibseq(sequence) == expected_result
