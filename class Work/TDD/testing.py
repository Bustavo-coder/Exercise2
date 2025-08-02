dollar_exchange
import unittest

class TestDollarExchngeFunction(unittest.TestCase):
	def test_that_dollar_exchange_exists(self):
		dollar_exchange.dollar_change(2)

	def test_that_dollar_exchange_correct_result(self):
		result = dollar_exchange.dollar_change(2)
		self.assertEqual(result,3100)
		result = dollar_exchange.dollar_change(5)
		self.assertEqual(result,7750)

	def test_that_right_value_is_passed_in(self):
		 result = dollar_exchange.dollar_change(1)
		self.assertRaises(ValueError,dollar_exchange.dollar_change(result),"Basit")
		