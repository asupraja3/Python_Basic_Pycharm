#Unit testing in Python can be done using various frameworks.
# Here are three examples using different frameworks:
#1.unittest: Uses class-based structure
#Uses class-based structure
import unittest
def add(x, y):
    return x + y

class TestAdd(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)

if __name__ == '__main__':
    unittest.main()

#2.pytest: Uses function-based structure
#Requires pip install pytest,Simple function-based syntax
import pytest
def add(x, y):
    return x + y
def test_add_positive():
    assert add(2, 3) == 5
def test_add_negative():
    assert add(-1, -1) == -2

#3.nose2: Similar to unittest, but with additional features
import nose2
def add(x, y):
    return x + y
class TestAdd:
    def test_add_positive(self):
        assert add(2, 3) == 5

    def test_add_negative(self):
        assert add(-1, -1) == -2
if __name__ == '__main__':
    nose2.main()