import function_snacks
import unittest

class TestFuction_function_snacks(unittest.TestCase):
	def test_that_divide_or_square_exits_in_function_snacks(self) :
		function_snacks.divide_or_square(1)

	def test_that_divide_or_square_return_correcet_result(self):
		result = function_snacks.divide_or_square(10)
		self.assertEqual(result,3.16)
		result = function_snacks.divide_or_square(11)
		self.assertEqual(result,1)
		
	def test_that_divide_snacks_take_incorrect_value_and_return_value_error(self):
		self.assertRaises(ValueError,function_snacks.divide_or_square,"basit")

	def test_that_divide_snacks_takes_in_decimal_value_and_return_correct_value(self):
		result = function_snacks.divide_or_square(20.5)
		self.assertEqual(result,0.5)

	def test_that_divide_snacks_takes_in_negative_and_return_valueError(self):
		self.assertRaises(ValueError,function_snacks.divide_or_square,-1)
	
	