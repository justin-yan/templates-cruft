from hypothesis import given
import hypothesis.strategies as st

@given(st.integers())
def test_init_placeholder(number):
    assert number == number
