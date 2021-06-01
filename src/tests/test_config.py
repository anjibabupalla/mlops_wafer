
import pytest





def test_generic():
    a = 2
    b = 2
    assert a == b


def test_not_in_ange():
    a = 5
    with pytest.raises(NotInRangeError):
        if a not in range(10, 20):
            raise NotInRangeError
