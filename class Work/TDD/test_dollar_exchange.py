import dollar_exchange
import unittest

class TestUnitFunction(unittest.TestCase):
	def test_check_if_exchage_cal_exits (self):	
		dollar_exchange.exchange_cal(1)

	def test_check_if_exchange_cal_returns_corrrect_result(self):
		result = dollar_exchange.exchange_cal(2)
		self.assertEqual(result,3100)
		result = dollar_exchange.exchange_cal(5)
		self.assertEqual(result,7750)
	def test_check_if_excahnge_call_take_the_right_argument(self):
		self.assertRaises(ValueError,dollar_exchange.exchange_cal(),"fiyin")
	