import pytest

from main_program.fibonacci import generateFibonacci


@pytest.mark.fibo
class TestClass(object):

    def test_fibonachi_1(self):
        assert generateFibonacci(0) == 0, "Should be 0"

    def test_fibonachi_2(self):
        assert generateFibonacci(1) == 1, "Should be 1"

    def test_fibonachi_3(self):
        assert generateFibonacci(2) == 1, "Should be 2"

    def test_fibonachi_4(self):
        assert generateFibonacci(3) == 2, "Should be 3"

    def test_fibonachi_5(self):
        assert generateFibonacci(10) == 55, "Should be 55"

