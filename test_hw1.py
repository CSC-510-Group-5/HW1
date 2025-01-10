import pytest
from hw1 import is_even


def test_is_even():
    assert is_even(3) == False
    
  
def test_fail_is_even():
    assert is_even(2) == True
