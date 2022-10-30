import pytest
from new_folder.code import change

def test_all():
  x = 2
  assert x == 2
  assert isinstance(x, int)
  y = change(x)
  assert y == 4
  assert isinstance(y, int)
