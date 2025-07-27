import assignment.quicksort as qs

def test_quicksort():
    assert qs.quicksort([3, 1, 4, 1, 5, 9]) == [1, 1, 3, 4, 5, 9]
    assert qs.quicksort([]) == []
    assert qs.quicksort([5]) == [5]
    assert qs.quicksort([10, -1, 2, 8, 0]) == [-1, 0, 2, 8, 10]
