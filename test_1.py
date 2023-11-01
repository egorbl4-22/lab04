import pytest
from lib import count_common_elements

def test1_count_common_elements():
    result = count_common_elements([3, 2, 3, 4, 5],[3, 1, 3, 4, 5],[3, 2, 3, 4, 7])
    assert result == 2

def test2_count_common_elements():
    result = count_common_elements([3, 2, 3, 4, 5], [3, 2, 3, 4, 5], [3, 2, 3, 4, 7])
    assert result == 3

def test3_count_common_elements():
    result = count_common_elements([], [], [])
    assert result == 0

if __name__ == "__main__":
    pytest.main()