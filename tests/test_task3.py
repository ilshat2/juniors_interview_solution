import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from task3.solution import appearance


def test_appearance():
    tests = [
        {'intervals': {'lesson': [1594663200, 1594666800],
                       'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
                       'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
         'expected': 3117},

        {'intervals': {'lesson': [1594663200, 1594666800],
                       'pupil': [],
                       'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
         'expected': 0},

        {'intervals': {'lesson': [1594663200, 1594666800],
                       'pupil': [1594663340, 1594666472],
                       'tutor': []},
         'expected': 0},

        {'intervals': {'lesson': [1594663200, 1594666800],
                       'pupil': [1594663340, 1594663380],
                       'tutor': [1594663400, 1594663420]},
         'expected': 0},

        {'intervals': {'lesson': [1594663200, 1594666800],
                       'pupil': [1594663200, 1594666800],
                       'tutor': [1594663200, 1594666800]},
         'expected': 3600},

        {'intervals': {'lesson': [1594663200, 1594666800],
                       'pupil': [1594663200, 1594665000],
                       'tutor': [1594664000, 1594666800]},
         'expected': 1000},

        {'intervals': {'lesson': [1000000, 2000000],
                       'pupil': [1500000, 2500000],
                       'tutor': [1200000, 1800000]},
         'expected': 300000},

        {'intervals': {'lesson': [0, 10],
                       'pupil': [5, 15],
                       'tutor': [3, 7]},
         'expected': 2},

        {'intervals': {'lesson': [1594663200, 1594666800],
                       'pupil': [1594663100, 1594663150],
                       'tutor': [1594663100, 1594663150]},
         'expected': 0},

        {'intervals': {'lesson': [1594663200, 1594666800],
                       'pupil': [1594663100, 1594666900],
                       'tutor': [1594663100, 1594666900]},
         'expected': 3600},
    ]

    for i, test in enumerate(tests):
        result = appearance(test['intervals'])
        assert result == test['expected'], f"Test case {i} failed: got {result}, expected {test['expected']}"
        print(f"Test case {i} passed.")


if __name__ == '__main__':
    test_appearance()
