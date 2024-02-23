from hypothesis import given
from hypothesis.strategies import text

from encryption.caesar import caesar_cipher


@given(text())
def test_caesar_ciper_loops(s):
    assert caesar_cipher(s, 1) == caesar_cipher(s, 27)
