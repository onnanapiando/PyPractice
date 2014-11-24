import unittest
from calculate import Calculate


class TestCalculate(unittest.TestCase):
# setUp method - which is excuted before each test, so that you need define your
# instance only once and have it created before each test.   
    def setUp(self):
      self.calc = Calculate()

    def test_add_method_returns_correct_result(self):
# assertEqual method checks if the first argument is equal to the second.
     # self.assertEqual("HelloWorld", self.calc.add("Hello","World"))
      print 'Hello'
      self.assertEqual(4, self.calc.add("Hello", "World"))
      self.assertAlmostEquals(1,1)

    def test_add_method_raises_typeerror_if_not_ints(self):
# unittest method assertRaises takes 3 arguments. 1 - the type of exception you
# expect to be raised. 2 - the method under test. 3 - the value passed in the
#argument to the method under test. 
      self.assertRaises(TypeError, self.calc.add, "Hello","World")


if __name__ == '__main__':
    unittest.main()

