import pytest

pytestmark = pytest.mark.should_fail


def test_broken():
    [1, 2, 3].pop(4)


def test_failed():
    assert 2 + 2 == 7
