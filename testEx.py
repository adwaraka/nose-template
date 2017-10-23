import sys
import nose
import unittest
from nose import with_setup
from Plugins.htmlReport import HtmlOutput

class MyTest(unittest.TestCase):
    def my_setup_function():
        pass

    def my_teardown_function():
        pass

    @with_setup(my_setup_function, my_teardown_function)
    def test_a_test(self):
        assert False

    @with_setup(my_setup_function, my_teardown_function)
    def test_b_test(self):
        assert True

    @with_setup(my_setup_function, my_teardown_function)
    def test_c_test(self):
        assert False

    @with_setup(my_setup_function, my_teardown_function)
    def test_d_test(self):
        assert True

    @with_setup(my_setup_function, my_teardown_function)
    def test_e_test(self):
        assert True

    @with_setup(my_setup_function, my_teardown_function)
    def test_f_test(self):
        assert True

    @with_setup(my_setup_function, my_teardown_function)
    def test_g_test(self):
        assert True

if __name__ == '__main__':
    nose.main(addplugins=[HtmlOutput()])
