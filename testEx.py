import sys
import nose
import unittest
from Plugins.htmlReport import HtmlOutput

class MyTest(unittest.TestCase):
    def test_a_test(self):
        assert False
    def test_b_test(self):
        assert True
    def test_c_test(self):
        assert False
    def test_d_test(self):
        assert True

if __name__ == '__main__':
    nose.main(addplugins=[HtmlOutput()])
