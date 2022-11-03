#from times import compute_overlap_time
from times import time_range
from pytest import raises
import times
import datetime


def compute_overlap_time(range1, range2):
    overlap_time = []
    for start1, end1 in range1:
        for start2, end2 in range2:
            low = max(start1, start2)
            high = min(end1, end2)
            if(high >= low):
                overlap_time.append((low, high))
            else:
                raise ValueError("Not include each pther")
    return overlap_time

def tset_same(range1, range2):
    for start1, end1 in range1:
        for start2, end2 in range2:
            if start1 != start2 and end1 == end2:
                con = True
    return con

def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)

    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]


    assert result == expected


def test_not_overloap():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 13:30:00", "2010-01-12 14:45:00", 2, 60)

    #result = compute_overlap_time(large, short)
    with raises(ValueError):
         result = compute_overlap_time(large, short)

    #expected = [(0, 0), (0, 0)]

   # assert result == expected


def test_end_same():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 11:30:00", "2010-01-12 12:00:00", 2, 60)

    result = tset_same(large, short)
    expected = 1

    assert result == expected


def test_intervals():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 2, 60)
    short = time_range("2010-01-12 11:30:00", "2010-01-12 12:00:00", 2, 60)

    result = tset_same(large, short)
    expected = 1

    assert result == expected




