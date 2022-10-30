import pytest

def let_s_test_it(x: int) -> int:
  return x

def test_intially():
  x = 2
  assert isinstance(x, int)
  assert let_s_test_it(x) == 3
  assert isinstance(let_s_test_it(x), int)
