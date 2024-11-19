import unittest
import Sample01 as ta

def test_add():
    result = ta.add(10, 18)
    assert result == 28

def test_type():
    result = ta.div(10,2)  #5.0
    assert type(result) == float

def test_div():
    result = ta.div(10, 0)
    assert result == "Error"
    


