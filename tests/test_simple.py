from .conftest import high


def test_nothing():
    pass


@high
def test_high_priority():
    pass
