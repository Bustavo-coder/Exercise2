import function_snacks
import unittest

class TestFunctionSnacks(unittest.TestCase):
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
	
	
class TestFunctionFutureInvestment(unittest.TestCase):
	def test_that_future_investment_function_exist(self):
		function_snacks.cal_future_investment(1,2,3)

	def test_that_cal_future_investment_take_in_incorrect_monthly_value(self):
		self.assertRaises(ValueError,function_snacks.cal_future_investment,2000,"monthly",30)

	def test_that_cal_future_investment_take_in_incorrect_amount_value(self):
		self.assertRaises(ValueError,function_snacks.cal_future_investment,"year",10,30)

	def test_that_cal_future_investment_take_in_incorrect_rate_value(self):
		self.assertRaises(ValueError,function_snacks.cal_future_investment,1000,10,"rate")
	
	def test_that_cal_future_investment_returns_correct_result(self):
		result = function_snacks.cal_future_investment(200,0.05,1)
		self.assertEqual(result,7.355827511386641e+27)


class TestFuntionOnlyFloat(unittest.TestCase):

	def test_that_only_float_firstnumber_take_in_incorrect_value(self):
		self.assertRaises(ValueError,function_snacks.only_floats,'firstNumber',2.2)

	def test_that_firstnumber_take_in_incorrect_value(self):
		self.assertRaises(ValueError,function_snacks.only_floats,'2.2',"secondNumber")

	def test_that_only_floats_return_2_for_two_float_input(self):
		result = function_snacks.only_floats(2.2,1.1)
		self.assertEqual(result , 2)

	def test_that_only_floats_return_1_for_one_float_input_and_one_int_input(self):
		result = function_snacks.only_floats(2.2,1)
		self.assertEqual(result , 1)

	def test_that_only_floats_return_0_for_none_float_input(self):
		result = function_snacks.only_floats(2,1)
		self.assertEqual(result , 0)

	def test_that_only_floats_return_error_for_negative_number(self):
		self.assertRaises(ValueError,function_snacks.only_floats, -1,-1)
		 	
		 	
	
		
	